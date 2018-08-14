import imageio
import os

path = '/Users/danielmcgrath/Desktop/test_giffy'

image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png', '.gif') ):
        filenames.append(filename)
        
filenames.sort()

images = list(map(lambda filename: imageio.imread(filename), filenames))

imageio.mimsave(os.path.join('movie.gif'), images, duration = 0.04)
