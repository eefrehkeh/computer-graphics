# Creates a PPM image of size 100 x 100. Each 10 x 10
# block of pixels alternates between blue and red
# to form a checker broad pattern

import one_color
import write_ppm
import add_to_image
import copy

def checker(boardsize_x,boardsize_y,blocksize_x,blocksize_y):
    print 'Starting'
    
    xwt = 0
    ywt = 0
    temp = one_color.struc()
    bluepoints = [copy.deepcopy(one_color.struc)]
    redpoints = [copy.deepcopy(one_color.struc)]
    
    for y in range(boardsize_y):
        t2 = y%blocksize_y
        if t2 == 0: 
            ywt = ywt + 1
        # end if on t2
        
        ywt2 = ywt%2
        
        if ywt2 == 1:
            n = 1
        elif ywt2 == 0:
            n = 2
        # end if on ywt2
        
        for x in range(boardsize_x):
            temp.x = x
            temp.y = y
            t = x%blocksize_x
            if t == 0:
                xwt = xwt + 1
            # end if on t
            
            xwt2 = xwt%2

            if n == 1:
                if xwt2 == 1:
                    bluepoints.append(copy.deepcopy(temp))
                elif xwt2 == 0:
                    redpoints.append(copy.deepcopy(temp))
                # end if on xwt2
            elif n == 2:
                if xwt2 == 1:
                    redpoints.append(copy.deepcopy(temp))
                elif xwt2 == 0:
                    bluepoints.append(copy.deepcopy(temp))
                # end if on xwt2
            # end if on n
        # end for loop on x
    # end for loop on y
    
    del redpoints[0] # remove unused location
    del bluepoints[0] # remove unused location
    
    image = one_color.main(boardsize_x,boardsize_y,255,255,255)
    image = add_to_image.main(image,redpoints,255,0,0)
    image = add_to_image.main(image,bluepoints,0,0,255)
    
    write_ppm.main(image,'Exercise3')
    print 'Finish'
# end checker function

# Run checker function
checker(100,100,10,10)
