import pytesseract
from PIL import Image
import os as os


def run(path):
    files = os.listdir(path)
    files.sort()
    print(files)
    outfile = open("A Foreign Boys Reaction To America pagebreak.txt", "a")
    for file in files:
        decode(path + file, outfile)


def decode(path, outfile):
    img = Image.open(path)
    decoded_text = pytesseract.image_to_string(img)
    print("\n---------------------------------------\n")
    print(decoded_text)
    outfile.write("\n---------------------------------------\n")
    outfile.write(decoded_text)


if __name__ == '__main__':
    run(directory)
