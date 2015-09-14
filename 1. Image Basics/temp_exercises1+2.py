import one_color
import write_ppm

image = one_color.main(320,240,255,0,0)
write_ppm.main(image,'Exercise2')
