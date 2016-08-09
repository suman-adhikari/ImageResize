import imghdr
import os
import tkFileDialog

from PIL import Image

source_location = tkFileDialog.askdirectory(title="Select The source folder")
list = os.listdir(source_location)
no_of_item = len(list)
unit_percent  = 100/no_of_item
destination_location = tkFileDialog.askdirectory(title="Select the Destination Folder")

img_ext = ["jgp","jpeg","png","bmp"]
complete = 0
item_processed = 0
original_size = 0
reduced_size = 0

for item in list:
    item_processed+=1
    img_location = source_location+"/"+item
    image_size =  os.path.getsize(img_location)
    image_size_kb = image_size/1024
    print "processing "+ item + " "+  str(image_size_kb) + " Kb"
    ext = imghdr.what(img_location)

    if ext in img_ext:
        save_img_location = destination_location + "/"+item
        img = Image.open(img_location)
        img_size = img.size

        if img_size[0] >3000:
            img = img.resize((int(img_size[0]*0.5),int(img_size[1]*0.5)),Image.ANTIALIAS)
        else:
            img = img.resize((img_size[0],img_size[1]),Image.ANTIALIAS)

        img.save(save_img_location, quality =85, optimize=True)
        reduced_image_size =  os.path.getsize(save_img_location)
        reduced_image_size_kb =  str(reduced_image_size/1024)

    else:
        print item+ " is not a image type"

    complete += unit_percent
    if(item_processed==no_of_item):
        complete=100
    print  str(complete) + "% complete " +  reduced_image_size_kb +   " kb  ["+str(item_processed)+ "/"+ str(no_of_item) + "]"

    original_size +=image_size
    reduced_size +=reduced_image_size


original_size = (original_size/float(1024*1024))
reduced_size = (reduced_size/float(1024*1024))
saved = original_size-reduced_size
saved_percent = ((saved/original_size)*100)

print  "==============================================================="
print "Original Size: " +  str(round(original_size,2))  + " Mb"
print "Reduced Size: " +  str(round(reduced_size,2))  + " Mb"
print "Saved: " + str(round(saved,2)) + " Mb [" + str(round(saved_percent,2)) + " %]"
print "================================================================"
