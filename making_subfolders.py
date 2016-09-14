import os
import glob
import shutil

file_directory="H:/Experiments/NIVL_rename"

for png_file in glob.glob(os.path.join(file_directory, "*.png")):
    filename=png_file[-14:-4]
    new1_filename=filename.replace("\\","")
    new_filename=new1_filename.replace("e","")
    print new_filename
    subject_name=new_filename.split('d')[0]
    print subject_name

    if os.path.exists(file_directory+ "\\" +subject_name):
        print "directory existed"
        print file_directory+"/"+new_filename+".png"
        print file_directory+"/"+subject_name+ "/" + new_filename + ".png"
        shutil.move((file_directory+"/"+new_filename+".png"),(file_directory+"/"+subject_name+ "/" + new_filename + ".png") )
        print "file moved to existing directory"
    else:
        os.makedirs(file_directory+ "\\" +subject_name)
        print "directory created"
        shutil.move((file_directory + "/" + new_filename + ".png"),
                    (file_directory + "/" + subject_name + "/" + new_filename + ".png"))
        print "file moved to created directory"