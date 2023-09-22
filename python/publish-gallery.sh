pip install flet
flet --version
flet publish python/apps/todo/todo.py --distpath python/dist/todo --base-url todo --app-name "Flet To-Do" --app-description "A classic To-Do app inspired by TodoMVC project."
flet publish python/apps/icons-browser/main.py --distpath python/dist/icons-browser --base-url icons-browser --app-name "Flet Icons Browser" --app-description "Quickly search through icons collection to use in your app."
flet publish python/tutorials/calc/calc.py --distpath python/dist/calculator --base-url calculator --app-name "Calculator" --app-description "A simple calculator app written in Flet."
flet publish python/tutorials/solitaire/solitaire-final-part1/main.py --distpath python/dist/solitaire --base-url solitaire --assets assets --app-name "Solitaire" --app-description "Learn how to handle gestures and position controls on a page."
flet publish python/apps/trolli/src/main.py --distpath python/dist/trolli --base-url trolli --assets ../assets --route-url-strategy "hash" --app-name "Trolli" --app-description "A clone of Trello."
flet publish python/apps/routing-navigation/home-store.py --distpath python/dist/simple-routing --base-url simple-routing --route-url-strategy "hash" --app-name "Flet routing example" --app-description "An example of routing in Flet."
flet publish python/apps/counter/counter.py --distpath python/dist/counter --base-url counter --app-name "Counter" --app-description "Counter to get an idea of Flet."
flet publish python/apps/flet-animation/main.py --distpath python/dist/flet-animation --base-url flet-animation --app-name "Flet animation" --app-description "An example of implicit animations in Flet."
flet publish python/apps/greeter/greeter.py --distpath python/dist/greeter --base-url greeter --app-name "Greeter" --app-description "A basic example of interactive forms in Flet."
flet publish python/apps/hello-world/hello.py --distpath python/dist/hello-world --base-url hello-world --app-name "Hello, world!" --app-description "A very minimal example of Flet app."
