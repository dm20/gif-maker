# Read <a href="https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python"> this Stack Overflow post</a>, which seems to provide an almost-working solution.

#### 1) install imageio  
  
    pip install -m python3 imageio
    
#### 2) put the script and your gif images in a folder

#### 3) get the pathname of the folder and change the path variable on line 4
    
    path = '/path/to/your/pics/'
    
#### 4) make a gif!
    
    python3 gif_maker.py
