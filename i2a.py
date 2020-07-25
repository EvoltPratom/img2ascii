import os ,sys
try:
    from PIL import Image
except:
    os.system('pip install pillow numpy')
finally:
    from PIL import Image
    import numpy as np

# import numpy as np
# import sys


def img2ascii(imagefile, file_name=None):
    '''
        - takes the name of image file as an argument and makes a text file of the same name as an output
        - also returns the ascii as a string
        eg:
        >>> from i2a import img2ascii
        >>> imguascii('test.png','text_file_name.txt')
        Saving test.png to text_file_name.txt
        >>>
    '''
    im = Image.open(imagefile, 'r').convert('L')
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    gscale2 = '@%#*+=-:. '
    new_size = (int(im.size[0] / 10), int(im.size[1] / 20))
    im = im.resize(new_size, Image.ANTIALIAS)
    im = np.array(im)
    if file_name == None:
        file_name = imagefile.split('.')[0] + '.txt'

    print(f'Saving {imagefile} to {file_name}')
    with open(file_name, 'w') as file:
        for row in im:
            for pixel in row:
                file.write(str(gscale2[int(int(pixel) * 9 / 255)]))
            file.write('\n')
    with open(file_name, 'r') as file2:
        x = file2.read()
    return x


if __name__ == '__main__':
    for i in sys.argv[1:]:
        img2ascii(i)
