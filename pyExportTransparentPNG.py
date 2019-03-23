from PIL import Image
import numpy as np
from os import listdir

# Params to set
# Directory with raw images
dirname = "directory"
# Output directory
output_dir = "directory_masked"
# Area to crop (x_min, y_min, x_max, y_max)
area = (800,350,1140,730)

files = sorted(listdir(dirname))

# Iterate through all files in the directory
for f in files:
    fname = f.split(".")[0]
    img = Image.open(dirname+"/"+f)
    img = img.convert("RGBA")
    w,h = img.size

    # Crop image
    cropped = img.crop(area)

    datas = cropped.getdata()
    newData = []
    tolerance = 25
    for item in datas:
        if item[0] > 95 - tolerance and item[0] < 95 + tolerance \
            and item[1] > 80 - tolerance and item[1] < 80 + tolerance \
            and item[2] > 170 - 2.5*tolerance and item[2] < 170 + 2.5*tolerance: 
            
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    cropped.putdata(newData)
    cropped.save(output_dir+"/"+fname+".png", "PNG")
    print(fname + " done")
