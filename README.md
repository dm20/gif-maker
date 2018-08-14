# Read <a href="https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python"> this Stack Overflow post</a>, which seems to provide an almost-working solution.

 - install imageio  
 #   
    pip install -m python3 imageio
    
- put the script and your gif images in a folder

-  get the pathname of the folder and change the path variable on line 4
#    
    path = '/path/to/your/pics/'
    
- make a gif!
#    
    python3 gif_maker.py
