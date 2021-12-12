from PIL import Image
import os


with open("program.hex", "w") as program:
    with open("ascii.hex", "w") as ASCII:
        commands = 0
        startingString = '''00FF00 000009 000003 061200 020100 030100 2C0100 2D0000 7A0800
002B04  100908 2D2B0C  002B07  012C04  037A0B 00030A  100902
0000FF\n\n02100B 00100A 03110B 00110A 111006 200002\n\n\n'''
        commands += len(startingString.strip().split()) - 1
        startingString = "v2.0 raw\n\n" + startingString

        program.write(startingString)
        ASCII.write("v2.0 raw\n")

        pictures = os.listdir("pngs")

        whereA = 65
        ASCII.write(("0 " * whereA) + "\n")

        for a in range(26):
            with Image.open("pngs/" + str(a) + ".png") as image:
                pixels = image.load()
                width, height = image.size

                ASCII.write(format(commands + 1, "02X") + "\n")

                for w in range(width):
                    for h in range(height):
                        r, g, b, q = image.getpixel((w, h))

                        if r == 255 and g == 255 and b == 255:
                            program.write("10" + format(h, "02X") + "00 11" + format(w, "02") + "00 010602 ")
                            commands += 3

                program.write("200002\n\n")
                commands += 1