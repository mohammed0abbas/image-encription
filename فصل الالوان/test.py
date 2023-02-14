from PIL import Image



##  open file image from path
image_org = Image.open('./test1.png')


## copy 3 varibals from orginal image
img_red = image_org.copy()

img_green = image_org.copy()

img_blue = image_org.copy()


img_enc = image_org.copy()



## size of image
width = image_org.size[0]
height =image_org.size[1]


## loop in the pixils of image
for row in range(height):
    for col in range(width):

        ## copy for orginale pixile
        p = image_org.getpixel((col,row))


        color1 = skew_tent_map(p[0],2.0)



        ## put pixils in copy image
        img_red.putpixel((col,row),(color1,0,0))

        img_green.putpixel((col,row),(0,p[1],0))

        img_blue.putpixel((col,row),(0,0,p[2]))


## image show        
img_red.show()
img_green.show()
img_blue.show()

       
