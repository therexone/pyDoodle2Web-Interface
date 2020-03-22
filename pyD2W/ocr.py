try:
    from PIL import Image
except ImportError:
    import PIL.Image
import PIL
import pytesseract
import os

class OCR:
    def __init__(self, imageName: str):
        self.imageName = imageName
        self.allowed_tags = ['container', 'row', 'coloumn', 'navbar', 'image', 'card', 'column', 'cofoumm']

    def formater(self, line: str):
        if line not in ['', ' ']:
            return line


    def biulder(self, text: str):
        main_list = []
        for line in filter(self.formater, text.splitlines()):
            for i in line.strip().split():
                if i.lower().split('-')[0] in self.allowed_tags:
                    main_list.append(i)
        return main_list


    def readText(self):
        try:
            path = os.path.join(os.path.abspath('../'), 'media', self.imageName)
            print(path)
            text = pytesseract.image_to_string(path)
            tags = self.biulder(text)
            print(tags)
            return tags

        except PIL.UnidentifiedImageError:
            print('Could not read the image file, check filetype.')

        except Exception as e:
            print(e)
            

OCR('complex.png').readText()