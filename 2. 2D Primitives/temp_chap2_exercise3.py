# Creates a PPM image of size 320 x 240. The background
# is light grey and contains a black ellipse

import one_color
import write_ppm
import add_to_image
import copy
import math

#Function to gather all points -> pixels needed, returns structure
def ellipse(a,b, center_x, center_y):
    # a == major axis
    # b == minor axis
    
    biglist = []        #data structure to hold points

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #initialize starting point to (a,0)
    temp.x = a
    temp.y = 0
    
    biglist.append([temp.x, temp.y])
    biglist.append([-(temp.x), temp.y])

    while True:

        #check to see if in region 2
        if ((pow(a, 2.0))*(temp.y +1)) < ((pow(b, 2.0))*(temp.x - 0.5)):

            #compute next y location for region 2
            temp.y = temp.y +1

            #compute the corresponding x value for y + 1 using Eq. 2.8
            temp.x = math.sqrt( (pow(a, 2.0)) * ( 1 - ((pow(temp.y, 2.0))/(pow(b, 2.0)))  ) )

            #Round to the nearest integer value
            temp.x = int(round(temp.x))

            #compute other points on the circle  by symmetry
            biglist.append([temp.x, temp.y])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([temp.x, -(temp.y)])

            #check if still in region 2, if not move on
            if ((pow(a, 2.0))*(temp.y+1)) >= ((pow(b, 2.0))*(temp.x-.5)):
                break
        #if not in region 2, move on to region 1
        else:
            break

    while True:

        #compute next x location for region 1
        temp.x = temp.x - 1

        #compute the y value for x - 1 using Eq. 2.9
        temp.y = math.sqrt( (pow(b, 2.0)) * ( 1 - ((pow(temp.x, 2.0))/(pow(a, 2.0)))  ) )

        #Round to the nearest integer
        temp.y = int(round(temp.y))

        #if x > 0, keep looping through looking to compute y values
        if temp.x == 0:
            biglist.append([temp.x, temp.y])
            biglist.append([temp.x, -(temp.y)])
        else:
            biglist.append([temp.x, temp.y])
            biglist.append([-(temp.x), temp.y])
            biglist.append([-(temp.x), -(temp.y)])
            biglist.append([temp.x, -(temp.y)])

        if temp.x <= 0:
            break

    #add center point to all points
    for i in range(0, len(biglist)):
        temp.x = biglist[i][0] + center_x
        temp.y = biglist[i][1] + center_y

        biglist[i][0] = biglist[i][0] + center_x
        biglist[i][1] = biglist[i][1] + center_y

        #add updated/finalized points to data structure
        points.append(copy.deepcopy(temp))

    del points[0]   # remove unused location
    return points

image = one_color.main(320,240,245,245,245)
image = add_to_image.main(image,ellipse(50,100,160,120),0,0,0)
write_ppm.main(image,'Chap2_Exercise3')
