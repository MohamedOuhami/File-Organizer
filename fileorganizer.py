import os
import shutil

# Setting the designed file to transfer
# As far I just want to transfer 1 file to my music folder
file_source = r"/home/mohamed/Downloads/"
folder_dest = r"/home/Documents/Music/"

print("Here are your files : ")

def fetching_files(src,dst):
    for file in os.listdir(src): # Fetching all of the files presented in the source path
        source = os.path.join(src, file)
        destination = os.path.join(dst, file)

        print(file)

def copying_files(src,dst):
    

    for file in os.listdir(src): # Fetching all of the files presented in the source path
        source = os.path.join(src, file)
        destination = os.path.join(dst, file)

        shutil.move(source, destination)

fetching_files('Downloads', 'destination')
copying_files('Downloads', 'destination')