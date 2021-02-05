#! /usr/bin/env python3
from PIL import Image
import random
import os
import math


def main():

    file = open("sample.bin", "rb")
    size = os.path.getsize('sample.bin')
    byte = file.read(1)
    testImage = Image.new("RGB", (math.isqrt(round(size / 3)) + 1,math.isqrt(round(size / 3))+1), (255,255,255))
    pixel = testImage.load()
    x = 0
    y = 0
    while byte:
            #print(byte)
            red = int.from_bytes(byte, "big")
            byte = file.read(1)
            #print(byte)
            green = int.from_bytes(byte, "big")
            byte = file.read(1)
            #print(byte)
            blue = int.from_bytes(byte, "big")
            byte = file.read(1)
            pixel[x,y]=(red,blue,green)
            x += 1
            if(x > math.isqrt(round(size / 3)) ):
                x = 0
                y +=1

    testImage.save("finalImage.jpg")
if __name__ == "__main__":
    main()
