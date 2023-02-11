## Image Carousel
Automatic image carousel (UserControl)

### Usage
The class takes in:
- `image_list`:*list[tuples]* : list of tuples, each tuple is made of image and image description or only the image
- `perseverace_time`:*float* : seconds of each image perseverance on screen
- `animations`:*list*: list made of 2 animations, IN and OUT
- `descriptive`:*bool*: specify if the carousel needs to show the images description. 
    - default: **True**
    - **[**NOTE**]**: if the images_list's tuples do not contain the image description is needs to be set to **False**

### Demo
> descriptive: True

https://user-images.githubusercontent.com/81587335/218256446-d8d1be25-7bdf-476a-9dd3-85588b4ba829.mov

> descriptive: False

https://user-images.githubusercontent.com/81587335/218256505-f1ef25c9-6d95-402f-af00-ecbb99e9c623.mov
