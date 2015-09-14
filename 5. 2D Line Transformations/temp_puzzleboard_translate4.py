# Creates a PPM image of size 150 x 150. Draws an 8-way yellow
# puzzle board with line drawings of numbers 1-8 in different
# boxes. Each box is 50 x 50.

import one_color
import write_ppm
import add_to_image
import copy

x_translation = -50
y_translation = 0

# list containing points to draw number board lines
line_list = [[[0,50],[149,50]],
             [[0,100],[149,100]],
             [[49,0],[49,149]],
             [[99,0],[99, 149]]
             ]

# list containing vertexes for each number to be drawn
number_list = [
    # number 1
    [[24,134],[24,114]],
    # number two
    [[64,134],[84,134],[84,124],[64,124],[64,114],[84,114]],
    # number five
    [[134,134],[114,134],[114,124],[134,124],[134,114],[114,114]],
    # number three
    [[14,84],[34,84],[34,74],[14,74],[34,74],[34,64],[14,64]],
    # number four
    [[114,84],[114,74],[134,74],[134,84],[134,64]],
    # number six
    [[14,34],[14,14],[34,14],[34,24],[14,24]],
    # number seven
    [[64,34],[84,34],[69,14]],
    # number eight
    [[114,24],[114,14],[134,14],[134,24],[114,24],[114,34],[134,34],\
     [134,24]]
    ]


#Function to gather all points -> pixels needed, returns structure
def line(x1, y1, x2, y2):

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #Find absolute value of x length, y length
    x_length = abs(x1 - x2)
    y_length = abs(y1 - y2)

    #compare x length, y length, if x length is longer...
    if x_length >= y_length:
        m = float(y2-y1)/float(x2-x1)               # slope
        b = (-(float(y2-y1)/float(x2-x1)))*x1 + y1  # y-intercept

        #Find integer values from x1 to x2
        big_x = 0
        small_x = 0
        
        if x1 > x2+1:
            big_x = x1
            small_x = x2
        else:
            big_x = x2
            small_x = x1
        
        for x in range(small_x, big_x+1):
            temp.x = x

            #solve for corresponding y values using Eq. 2.1
            y_value = m * x + b

            #Round y values to nearest integer value
            y_value = round(y_value)
            temp.y = int(y_value)

            #add x and y values to data structure
            points.append(copy.deepcopy(temp))

    #compare x length, y length, if y length is longer...        
    elif y_length > x_length:
        m_inverse = float(x2-x1)/float(y2-y1)       # slope inverse

        #Find integer values from y1 to y2
        big_y = 0
        small_y = 0
        
        if y1 > y2+1:
            big_y = y1
            small_y = y2
        else:
            big_y = y2
            small_y = y1
        
        for y in range(small_y, big_y+1):
            temp.y = y

            #solve for corresponding x values using Eq. 2.4
            x_value = m_inverse*y - m_inverse*y1 + x1

            #Round x values to nearest integer value
            x_value = round(x_value)
            temp.x = int(x_value)

            #add x and y values to data structure
            points.append(copy.deepcopy(temp))

    del points[0]   # remove unused location
    return points

# draw yellow background
image = one_color.main(150,150,255,255,58)

# draw black lines to differentiate 9 50x50 blocks
for i in range(0, len(line_list)):
    image = add_to_image.main(image,line(line_list[i][0][0],line_list[i][0][1],line_list[i][1][0],line_list[i][1][1]),0,0,0)

# 1. Translate the lines for the number 4
# add xt, yt to the x values, y values
for i in range(0, len(number_list[4])):
    number_list[4][i][0] = number_list[4][i][0] + x_translation
    number_list[4][i][1] = number_list[4][i][1] + y_translation

#draw each number 1-8 according to number_list vertexes
for i in range(0, len(number_list)):
    for k in range(0, len(number_list[i])):
        if k == len(number_list[i])-1:
            pass
        else:
            image = add_to_image.main(image,line(number_list[i][k][0],number_list[i][k][1],number_list[i][k+1][0],number_list[i][k+1][1]),0,0,0)
    
write_ppm.main(image,'Chap3_Exercise9')

print 'printing done'
