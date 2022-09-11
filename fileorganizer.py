import os
import shutil
import pathlib

# Setting the designed file to transfer
# Detect the file extension

# Before you can work with this file organizer you need to have the folders " Downloads ", " Images", "Videos", "Music" added
# If you know what you're doing, you can change this code according to your needs

def copying_files(src,dst,file):
    
        source = os.path.join(src, file)
        destination = os.path.join(dst, file)

        shutil.move(source, destination)

def file_type(src):
    for file in os.listdir(src):
        source = os.path.join(src, file)

        if pathlib.Path(source).suffix == '.png': # Adding Images
            copying_files('Downloads', 'Images',file)

        elif pathlib.Path(source).suffix == '.mp3': # Adding Music
            copying_files('Downloads', 'Music',file)

        elif pathlib.Path(source).suffix == '.mp4': # Adding Vidos
            copying_files('Downloads', 'Videos',file)

        elif pathlib.Path(source).suffix == '.pdf': # Adding PDFs
            copying_files('Downloads', 'PDFs',file)


try :
    file_type('Downloads')
except:
    print(" There is an error in the directories. Please check that you have the following folders in your root : Images, Videos, Music, PDFs")