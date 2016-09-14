import glob
import os
import cv2

faces_folder_path = "H:\Experiments\Aureus_Experiments\IJB-A\Split-7\Images"
new_folder_path="H:\Experiments\Aureus_Experiments\IJB-A\Split-7\Images_cropped"

for png_file in glob.glob(os.path.join(faces_folder_path, "*.png")):
    name, ext = os.path.splitext(os.path.basename(png_file))
    new_filename_path=name + ext
    with open(os.path.join(faces_folder_path, '{}.txt'.format(name))) as f_text:
       for line in f_text:
           values= [float(num) for num in line.split()]
           top_left_x= values[0]
           top_left_y= values[1]
           width     = values[2]
           height    =  values[3]
           new_top_left_x=top_left_x-(0.2*top_left_x)
           new_top_left_y=top_left_y-(0.1*top_left_y)
           new_width=width+(0.7*width)
           new_height=height+(0.3*height)
           img=cv2.imread(png_file)
           cv2.imshow('img',img)
           crop_image=img[top_left_y:(top_left_y+new_height),top_left_x:(top_left_x+width)]
           # crop_image=img[new_top_left_y:(new_top_left_y+new_height),new_top_left_x:(new_top_left_x+new_width)]
           cv2.imwrite(os.path.join(new_folder_path,new_filename_path),crop_image)
           cv2.waitKey(1)



# topleftx=coordinates[0]
    # toplefty=coordinates[1]
    # width=coordinates[2]
    # height=coordinates[3]


# except IOError as e:
#     print '"{}" has no matching txt file'.format(png_file)