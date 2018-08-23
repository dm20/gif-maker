import imageio
import os

path = '/Users/username/Desktop/sample/' # on Mac: right click on a folder, hold down option, and click "copy as pathname"
image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png', '.gif') ):
        filenames.append(filename)
        
filenames.sort() # this iteration technique has no built in order, so sort the frames

images = list(map(lambda filename: imageio.imread(filename), filenames))

imageio.mimsave(os.path.join('my_very_own_gif.gif'), images, duration = 0.04) # modify the frame duration as needed
