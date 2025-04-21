import PIL.Image
import os
from os import system, name

if name == "nt":
    slash = "\\"
else:
    slash = "/"

ASCIIchars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÁÉÍÓÚ'.,!?/;()<>@"

dirPath = os.path.dirname(os.path.realpath(__file__))
fontDir = dirPath + slash + "systemBold.png"
fontImg = PIL.Image.open(dirPath + slash + "systemBold.png")


def getText():
    bifur = int(input("""Choose an option:
    [1] Turn a quick text into ascii art
    [2] Turn a .txt file into ascii art
    : """))

    while bifur not in [1, 2]:
        bifur = int(input("""Choose an option:
    [1] Turn a quick text into ascii art
    [2] Turn a .txt file into ascii art
    (invalid): """))

    if bifur == 1:
        text = str(input("Insert the text you wish\n: "))
    elif bifur == 2:
        file = str(input("Insert the file you wish: "))
        with open(file, "r") as f:
            text = f.read()
    
    return text

def rmvPunct(txt):
    for char in txt:
        if char not in characters:
            txt.replace("char", "")

def grayify(img):
    grayscaleImg = img.convert("L")
    return grayscaleImg

#DIVFONT: Splits the font image into different images each containing the corresponding character. 
def divFontS1(y1, y2, w, row, column):
    x1 = (column-1)*w
    x2 = x1+w
    subimg = grayify(fontImg).crop((x1, y1, x2, y2))
    subimg.save(f"{row}x{column}.png")

def divFontS2(w, h):
    for row in range(1, 5):
        y1 = (row-1)*h
        y2 = y1+h
        if row == 1:
            for column in range(1, 17):
                divFontS1(y1, y2, w, row, column)
        elif row == 2:
            for column in range(1, 11):
                divFontS1(y1, y2, w, row, column)
        elif row == 3:
            for column in range(1, 16):
                divFontS1(y1, y2, w, row, column)
        elif row == 4:
            for column in range(1, 13):
                divFontS1(y1, y2, w, row, column)

def divFont():
    xmargin = 80
    ymargin1 = 63
    divFontS2(ymargin1, xmargin)

#Conversion 
def pixelToChar(img):
    image = PIL.Image.open(img)
    pixels = image.getdata()
    chars = "".join([ASCIIchars[pixel//25] for pixel in pixels])
    return chars

def convertASCII(img):
    Nimg = pixelToChar(img)
    pixelCount = len(Nimg)
    ASCIIimg = "\n".join([Nimg[i:(i+63)] for i in range(0, pixelCount, 63)])
    return ASCIIimg

fontImg = grayify(fontImg)

divFont()

charsDir = {
    "alphabet" : [],
    "numbers" : [],
    "specialChars" : [],
}

#Defines the directory of the images
for row in range(1, 5):
    if row == 1:
        for column in range(1, 17):
            charsDir["alphabet"].append(dirPath + slash + str(row) + "x" + str(column) + ".png")
    elif row == 2:
        for column in range(1, 11):
            charsDir["alphabet"].append(dirPath + slash + str(row) + "x" + str(column) + ".png")
    elif row == 3:
        for column in range(1, 16):
            charsDir["numbers"].append(dirPath + slash + str(row) + "x" + str(column) + ".png")
    elif row == 4:
        for column in range(1, 13):
            charsDir["specialChars"].append(dirPath + slash + str(row) + "x" + str(column) + ".png")

chars = []
for row in range(1, 5):
    if row == 1:
        for column in range(1, 17):
            ASCIIimg = convertASCII(charsDir["alphabet"][column-1])
            chars.append(ASCIIimg)
    elif row == 2:
        for column in range(1, 11):
            ASCIIimg = convertASCII(charsDir["alphabet"][column+15])
            chars.append(ASCIIimg)
    elif row == 3:
        for column in range(1, 16):
            ASCIIimg = convertASCII(charsDir["numbers"][column-1])
            chars.append(ASCIIimg)
    elif row == 4:
        for column in range(1, 13):
            ASCIIimg = convertASCII(charsDir["specialChars"][column-1])
            chars.append(ASCIIimg)

text = getText()
text = text.upper()
rmvPunct(text)

ASCIItext = ""
for char in text:
    ASCIItext += chars[characters.find(char)]

print(ASCIItext)

#Saves to a file (better to visualize) 
with open("text.txt", "w") as f:
        f.write(ASCIItext)

while True:
    pass

#---------------------------------------------------------------------
