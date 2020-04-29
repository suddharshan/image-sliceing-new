from PIL import Image  
# Opens a image in RGB mode 
p=input("Enter page number : ")
p=str(p)
a='C:/Users/suddharshan/Downloads/'+p+'.png'
im = Image.open(a)
# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 
left=51
a=7
b=0
c=1
top=120
# Setting the points for cropped image
for top in range(121,1600,190):
    b=1
    for left in range(51,1150,190):
        right = left+187
        bottom = height-122-(a*190)-47

        # Cropped image of above dimension 
        # (It will not change orginal image) 
        im1 = im.crop((left, top, right, bottom)) 

        # Shows the image in image viewer 
        #im1.show()
        name=str(p)+"_"+str(c)+'_'+str(b)
        im1.save('C:/Users/suddharshan/Downloads/images/'+name+'.png')
        print(name)
        b=b+1
    a=a-1
    c=c+1