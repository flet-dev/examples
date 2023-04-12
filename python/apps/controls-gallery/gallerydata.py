import os
from os.path import isfile, join
from pathlib import Path
import importlib.util
import sys
import flet as ft

class GridItem():
    def __init__(self, id):
        self.id = id
        self.name = None
        self.image_file_name = None
        self.examples = []
        self.description = None

class ExampleItem():
    def __init__(self):
        self.name = None
        self.example = None
        self.source_code = None

class ControlGroup():
    def __init__(self, name, label, icon, selected_icon):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon
        self.grid_items = []


class GalleryData():
    def __init__(self):
        self.import_modules()


    destinations_list = [
        ControlGroup(name='layout', label='Layout', icon=ft.icons.GRID_VIEW, selected_icon=ft.icons.GRID_VIEW_SHARP),
        ControlGroup(name='navigation', label='Navigation', icon=ft.icons.MENU, selected_icon=ft.icons.MENU),
        ControlGroup(name='display', label='Display', icon=ft.icons.INFO_OUTLINED, selected_icon=ft.icons.INFO_SHARP),
        ControlGroup(name='buttons', label='Buttons', icon=ft.icons.SMART_BUTTON, selected_icon=ft.icons.SMART_BUTTON),
        ControlGroup(name='input', label='Input', icon=ft.icons.GRID_VIEW, selected_icon=ft.icons.GRID_VIEW_SHARP),
        ControlGroup(name='dialogs', label='Dialogs', icon=ft.icons.INPUT, selected_icon=ft.icons.INPUT),
        ControlGroup(name='charts', label='Charts', icon=ft.icons.MESSAGE_OUTLINED, selected_icon=ft.icons.MESSAGE_SHARP),
        ControlGroup(name='animations', label='Animations', icon=ft.icons.ANIMATION, selected_icon=ft.icons.ANIMATION),
        ControlGroup(name='utility', label='Utility', icon=ft.icons.PAN_TOOL_OUTLINED, selected_icon=ft.icons.PAN_TOOL_SHARP),
        ControlGroup(name='colors', label='Colors', icon=ft.icons.FORMAT_PAINT_OUTLINED, selected_icon=ft.icons.FORMAT_PAINT_SHARP)
    ]
    
    def list_control_dirs(self, dir):
        file_path = os.path.join(str(Path(__file__).parent), dir)
        control_dirs = [f for f in os.listdir(file_path) if not isfile(f) and f not in ['index.py','images', '__pycache__', '.venv', '.git']]
        return control_dirs

    def list_example_files(self, control_group_dir, control_dir):
        file_path = os.path.join(str(Path(__file__).parent), control_group_dir, control_dir)
        example_files = [f for f in os.listdir(file_path) if f not in ['__pycache__']]
        return example_files


    def import_modules(self):
        
        def format_code(code_text, example_name):
            new_str = code_text.split("def example():")
            #print(new_str[1])
            middle_code = new_str[1].replace("return ", "page.add(")
            start_code = f"""import flet as ft

def main(page: ft.Page):
    page.title = "{example_name}"            
"""

            end_code = f"""
    )
ft.app(target=main)            
"""
            #new_code = "\n```python\n" + start_code + middle_code + end_code + "\n```\n"
            new_code = start_code + middle_code + end_code
            return new_code

        for control_group_dir in self.destinations_list:
            for control_dir in self.list_control_dirs(control_group_dir.name):
                
                grid_item = GridItem(control_dir)
                
                for file in self.list_example_files(control_group_dir.name, control_dir):
                    file_name = os.path.join(control_group_dir.name, control_dir, file)
                    module_name = file_name.replace("/", ".").replace(".py", "")
                    
                    if module_name in sys.modules:
                        print(f"{module_name!r} already in sys.modules")
                    else:
                        file_path = os.path.join(str(Path(__file__).parent), file_name)
                        spec = importlib.util.spec_from_file_location(module_name, file_path)
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[module_name] = module
                        spec.loader.exec_module(module)
                        print(f"{module_name!r} has been imported")
                        if file =='index.py':
                            grid_item.name = module.name
                            grid_item.image_file_name = module.image_file
                            grid_item.description = module.description
                        else:
                            example_item = ExampleItem() 
                            with open(file=file_path) as file_to_read:
                                code_text = format_code(file_to_read.read(), module.name)
                                example_item.source_code = code_text
                            example_item.example = module.example
                            example_item.name = module.name
                            grid_item.examples.append(example_item)
                control_group_dir.grid_items.append(grid_item)