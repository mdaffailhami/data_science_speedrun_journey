from wand.image import Image


def display_pdf(src):
    with Image(filename=src) as img:
        images = img.sequence

        for i in range(len(images)):
            display(Image(images[i]))
