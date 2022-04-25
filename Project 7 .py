"""
Project 7

"""

#import image 
from PIL import Image
#define main method
def invert(image):
    #from image size get the values of wigth and height
    width, height = image.size
    for i in range(width):
        for j in range(height):
            #get (r,g,b) values from each pixel of an image
            (r,g,b) = image.getpixel((i,j))
            #invert image to negative image, subtract from maximum value of the color
            r = 255 - r
            g = 255 - g
            b = 255 - b
            #to generate a negative image set the changed rgb values to the image
            image.putpixel((i,j),(r,g,b))
def main():
    filepath = "/Users/josuemarante/Downloads/CE2BB07A-7BCB-4128-8B8D-60338A155CFC.jpeg"
    #Open the image
    image = Image.open(filepath)
    #Call the function invert to change the image to negative
    invert(image)
    image.show()
#Call main function
main()
