# Creates a PPM image of size 320 x 240. The background
# is light grey and contains a horizontal red line and
# a vertical green line that have been rotated, scaled,
# and translated.

import one_color
import write_ppm
import add_to_image
import copy
import math

vertexes=[[60,120],[110,200],[110,150],[200,220],[160,120]]

# list holding red and green lines.
# line_list[0] = red, line_list[1] = green

line_list = [
    [[60,120,],[160,120]],
    [[160,120],[160,220]]
    ]

x_translation = 50
y_translation = -30

rotation_point = [160,120]
rotation_angle = -80

fixed_point = [160,120]
x_scale = 1.5
y_scale = 1.5

def fill_polygon(vertex_array):

    temp = one_color.struc()
    points = [copy.deepcopy(one_color.struc)]

    #find min y-value (ymin) and max y-value (y-max)
    smallest = vertex_array[0][1]
    smallest_index = 0
    largest = vertex_array[0][1]
    largest_index = 0
    
    for i in range(0, len(vertex_array)):
        if vertex_array[i][1] < smallest:
            smallest = vertex_array[i][1]
            smallest_index = i
        if vertex_array[i][1] > largest:
            largest = vertex_array[i][1]
            largest_index = i
    
    smallest_holder = smallest

    #For all the scan lines from ymin to ymax:
    for k in range(smallest, largest+1):

        intersections = []

        #For each edge:
        for j in range(0, len(vertex_array)):

            x_one = vertex_array[j][0]
            y_one = vertex_array[j][1]

            if j == len(vertex_array)-1:
                x_two = vertex_array[0][0]
                y_two = vertex_array[0][1]
            else:
                x_two = vertex_array[j+1][0]
                y_two = vertex_array[j+1][1]

            if y_two - y_one != 0:
                if (y_two <= smallest_holder <= y_one) or (y_one <= smallest_holder <= y_two):
                    y_max = y_one

                    # Find the y-value of the maximal vertex point

                    if y_one >= y_two :
                        y_max = y_one
                    elif y_one < y_two :
                        y_max = y_two

                    if (smallest_holder != y_max) and ((y_two <= smallest_holder <= y_one) or (y_one <= smallest_holder <= y_two)):
                        m_inverse = float(x_two-x_one)/float(y_two-y_one)       # slope inverse

                        x_value = m_inverse*smallest_holder - m_inverse*y_one + x_one
                        x_value = int(round(x_value))

                        temp.x = x_value
                        temp.y = smallest_holder

                        intersections.append([temp.x, temp.y])

        sorted(intersections, key=lambda x: x[0])
        
        for i in range(0, len(intersections), 2):
            
            counter = 0

            big_x = 0
            small_x = 0
            
            if intersections[i][0] > intersections[i+1][0]:
                big_x = intersections[i][0]
                small_x = intersections[i+1][0]
            else:
                big_x = intersections[i+1][0]
                small_x = intersections[i][0]
            
            for x in range(small_x, big_x+1):
                temp.x = small_x + counter
                temp.y = intersections[i][1]

                #add updated/finalized points to data structure
                points.append(copy.deepcopy(temp))

                counter = counter + 1

        smallest_holder = smallest_holder + 1

    del points[0]   # remove unused location
    return points


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

# draw light gray background
image = one_color.main(320,240,245,245,245)

# 1. Translate the lines of the polygon
# add xt, yt to the x values, y values
for i in range(0, len(vertexes)):
    vertexes[i][0] = vertexes[i][0] + x_translation
    vertexes[i][1] = vertexes[i][1] + y_translation

# 2. Scale the results
# translate end and start pts to origin using translation algorithm
for i in range(0, len(vertexes)):
    vertexes[i][0] = vertexes[i][0] - fixed_point[0]
    vertexes[i][1] = vertexes[i][1] - fixed_point[1]

# Scale x values, y values, round them
for i in range(0, len(vertexes)):
    vertexes[i][0] = int(round((vertexes[i][0])*(x_scale)))
    vertexes[i][1] = int(round((vertexes[i][1])*(y_scale)))

# translate end and start pts back
for i in range(0, len(vertexes)):
    vertexes[i][0] = vertexes[i][0] + fixed_point[0]
    vertexes[i][1] = vertexes[i][1] + fixed_point[1]

# 3. Rotate the results
# translate end and start pts to origin using translation algorithm
for i in range(0, len(vertexes)):
    vertexes[i][0] = vertexes[i][0] - rotation_point[0]
    vertexes[i][1] = vertexes[i][1] - rotation_point[1]

# Rotate x values, y values, round them
for i in range(0, len(vertexes)):
    x = vertexes[i][0]
    y = vertexes[i][1]
    vertexes[i][0] = int(round((x)*(math.cos(math.radians(rotation_angle))) - (y)*(math.sin(math.radians(rotation_angle)))))
    vertexes[i][1] = int(round((y)*(math.cos(math.radians(rotation_angle))) + (x)*(math.sin(math.radians(rotation_angle)))))

# translate end and start pts back
for i in range(0, len(vertexes)):
    vertexes[i][0] = vertexes[i][0] + rotation_point[0]
    vertexes[i][1] = vertexes[i][1] + rotation_point[1]

# fill the polygon
image = add_to_image.main(image,fill_polygon(vertexes),255,0,0)

# re-draw the polygon
for i in range(0, len(vertexes)):
    if i == len(vertexes)-1:
        image = add_to_image.main(image,line(vertexes[i][0],vertexes[i][1],vertexes[0][0],vertexes[0][1]),255,0,0)
    else:
        image = add_to_image.main(image,line(vertexes[i][0],vertexes[i][1],vertexes[i+1][0],vertexes[i+1][1]),255,0,0)

write_ppm.main(image,'Chap3_Exercise8')

print 'printing done'
