try:
    from PIL import Image
except ImportError:
    import PIL.Image
import PIL
import pytesseract
import os


image = os.path.join(os.path.abspath('../'), 'media', os.listdir('../media')[0])

element_list = []

def get_elements():
    try:
        elements = pytesseract.image_to_string(Image.open(image))
        element_list = elements.split()
        print(element_list)
    except PIL.UnidentifiedImageError:
        print('Could not read the image file, check filetype.')

# get_elements()