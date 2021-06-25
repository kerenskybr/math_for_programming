from coordinate_vectors import *
from PIL import Image

class ImageVector(Vector):
    size = (300, 300)
    def __init__(self, input):
        """Resizes the image to 300x300 and get vectors"""
        try:
            img = Image.open(input).resize(ImageVector.size)
            self.pixels = img.getdata()
        except:
            self.pixels = input
    
    def image(self):
        # Recreates the image
        img = Image.new("RGB", ImageVector.size)
        img.putdata([(int(r), int(g), int(b)) for (r,g,b) in self.pixels])
        return img
    
    def add(self, img2):
        # performs a vector addition
        return ImageVector([(r1+r2,g1+g2,b1+b2) for ((r1,g1,b1),(r2,g2,b2)) in zip(self.pixels,img2.pixels)])
        
    def scale(self, scalar):
        # Performs a scalar scale, multiplying each pixel to a scalar value
        return ImageVector([(scalar*r,scalar*g,scalar*b) for (r,g,b) in self.pixels])

    @classmethod
    def zero(cls):
        # The zero image has zero red, green, or blue content at any pixel.
        total_pixels = cls.size[0] * cls.size[1]
        return ImageVector([(0,0,0) for _ in range(0,total_pixels)])
    
    def save(self, img_name):
        return self.image().save(img_name)

    def _repr_png_(self):
        # To use the images in a jupter notebook
        return self.image()._repr_png_()

    
# Combine both images
new = 0.5 * ImageVector("inside.jpg") + 0.5 * ImageVector("outside.jpg")
new.save('processed.jpg')

# Inverts the image, like a camera film
white = ImageVector([(255,255,255) for _ in range(0,300*300)])
white = white - ImageVector("melba_toy.jpg")
white.save('white_img.jpg')