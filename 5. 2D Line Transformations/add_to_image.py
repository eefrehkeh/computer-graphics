# This file sets the color of
# a location in the image
import index_translation
import copy


def main(image,points,r,g,b):
    L = len(points)
    
    for j in range(L):
        # translate x and y location to a pixel number
        x = points[j].x
        y = points[j].y
        xd = image[0].x
        yd = image[0].y
        
        i = index_translation.main(x,y,xd,yd)
        
        # set the color
        
        image[i].r = r
        image[i].g = g
        image[i].b = b
    #end for loop
    return image
