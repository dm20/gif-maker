# Read <a href="https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python"> this Stack Overflow post</a>

#### 1) install imageio  
  
    pip install -m python3 imageio
    
#### 2) put the script and all of the frames (images) in a folder

#### 3) get the pathname of the folder and change the path variable on line 4 in gif_maker.py
    
    path = '/path/to/your/pics/'
    
#### 4) make a gif! (it'll take a few seconds)
    
    python3 gif_maker.py
