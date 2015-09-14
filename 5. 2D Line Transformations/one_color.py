# This function creates an image with
# just one color given by RGB
# and size of xd and yd

import copy

# allows any variable to be a flexible structure
class struc:
    pass

def main(xd, yd, r, g, b):
    # xd = width of image
    # yd = height of image
    # r = red color
    # g = green color
    # b = blue color
    
    L = xd*yd # Number of pixel in image
    
    image_size = copy.deepcopy(struc())
    pixel = copy.deepcopy(struc())
    
    # Set width and height
    
    image_size.x = xd
    image_size.y = yd
    image = [image_size]
    
    # Set pixel color
    
    pixel.r = r
    pixel.g = g
    pixel.b = b
    
    # Set all pixels to the same color

    for i in range(L):
            image.append(copy.deepcopy(pixel))
    # end for loop on i
    
    return image
