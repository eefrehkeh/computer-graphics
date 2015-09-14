# This file takes an RGB image and creates a .ppm file.
# The input to this file is the image and a name for the image


def main(image, name): # finds the number of pixels in the image
    L = image[0].x*image[0].y
    # Adds .ppm to file name
    name = name + '.ppm'
    s = ' '
    n = '\n'
    f = open(name,'w')
    
    # Write header information to PPM file
    
    f.write('P3\n')
    f.write('# Created by Ifreke Okpokowuruk.\n')
    x = str(image[0].x)
    y = str(image[0].y)
    temp = x + s + y + n
    f.write(temp)
    f.write('255\n')
    
    # Write image data to PPM file
    c = 0
    for i in range(1,L+1):
        temp = str(image[i].r) + s + str(image[i].g) + s
        temp = temp + str(image[i].b) + '\t'
        f.write(temp)
        c = c + 1
        if c == 4: # Puts only 4 pixels per line
            c = 0
            f.write(n)
        #end of if statement
    # end of for loop
    f.close()

