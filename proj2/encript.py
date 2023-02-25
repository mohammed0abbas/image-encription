from PIL import Image
import numpy as np



def skew_tent_map(x, r=5.0):
    return r * abs(x)


def bernulli_map(x):
    if x < 0.5:
        return x*2
    else:
        return 2 * (1-x)


def henon_map(x, y, a=3.4, b=0.6):
    x_new = 1 - a * x**2 + y
    y_new = b * x
    return x_new, y_new


def encript_image_henon(image):
    image_array = np.array(image)
    rows, columns, _ = image_array.shape
    encrypted_image = np.zeros((rows, columns, 3))
    for i in range(rows):
        for j in range(columns):
            x, y = henon_map(i, j)
            encrypted_image[i][j] = image_array[int(x) % rows][int(y) % columns]

    img = Image.fromarray(np.uint8(encrypted_image))
    return img



def convert_to_rgb(image):
    image.load()
    size = image.size
    img_red = Image.new("RGB", size)
    img_green = Image.new("RGB", size)
    img_blue = Image.new("RGB", size)
    
    width, height = size
    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            img_red.putpixel((i, j), (pixel[0], 0, 0))
            img_green.putpixel((i, j), (0, pixel[1], 0))
            img_blue.putpixel((i, j), (0, 0, pixel[2]))
    return img_red, img_green, img_blue


def encript_image_red(image, arr):
    width, height = image.size
    if arr[0] == 1:
        image = encript_image_henon(image)
    if arr[1] == 1:
       
        for i in range(width):
            for j in range(height):
                pixel = image.getpixel((i, j))
                image.putpixel((i, j), (int(skew_tent_map(pixel[0])), 0, 0))

    if arr[2] == 1:
        for i in range(width):
            for j in range(height):
                pixel = image.getpixel((i, j))
                image.putpixel((i, j), (int(bernulli_map(pixel[0])), 0, 0))
    return image

def encript_image_green(image, arr):
    width, height = image.size
    if arr[0] == 1:
        image = encript_image_henon(image)
    if arr[1] == 1:
       
        for i in range(width):
            for j in range(height):
                pixel = image.getpixel((i, j))
                image.putpixel((i, j), (0,int(skew_tent_map(pixel[0])), 0))

    if arr[2] == 1:
        for i in range(width):
            for j in range(height):
                pixel = image.getpixel((i, j))
                image.putpixel((i, j), ( 0,int(bernulli_map(pixel[0])), 0))
    return image




def encript_image_blue(img, arr):
    image = img.copy()
    width, height = image.size

    if arr[0] == 1:
        image1 = encript_image_henon(image)
    else:
        image1 = image

    if arr[1] == 1:
        image2 = image1.copy()
        for i in range(width):
            for j in range(height):
                pixel = image.getpixel((i, j))
                image2.putpixel((i, j), (0, 0, int(skew_tent_map(pixel[0]))))
    else:
        image2 = image1

    
    if arr[2] == 1:
        image3 = image2.copy()
        for i in range(width):
            for j in range(height):
                pixel = image.getpixel((i, j))
                image.putpixel((i, j), ( 0,0,int(bernulli_map(pixel[0]))))
    else:
        image3 = image2
    return image3

#r = [1, 0, 0]
def Encrypt(path, r, g, b):
    image = Image.open(path)
    red, green, blue = convert_to_rgb(image)
    red = encript_image_red(red, r)
    green = encript_image_green(green, g)
    blue = encript_image_blue(blue, b)
    
    width, height = image.size
    encrypted_image = Image.new(image.mode, image.size)
    for i in range(width):
        for j in range(height):
            pixel_red = red.getpixel((i, j))
            pixel_green = green.getpixel((i, j))
            pixel_blue = blue.getpixel((i, j))
            encrypted_image.putpixel((i, j), (pixel_red[0], pixel_green[1], pixel_blue[2]))
    return encrypted_image



