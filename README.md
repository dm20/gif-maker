## Inspired by <a href="https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python"> this Stack Overflow post</a>

<img src="https://github.com/dm20/gif-maker/blob/master/ron.gif" gif>

### 1) install imageio  
  
    pip install -m python3 imageio
    
### 2) put the script and all of the frames (images) in a folder
- You'll want to make sure the frames have some ordering to them in the filenames (see the sample)
- The frames can be any image type: PNG, JPEG, or even individual GIF frames as in the sample

### 3) get the pathname of the folder and change the path variable on line 4 in gif_maker.py
    
    path = '/path/to/your/pics/'
    
### 4) make a gif!
    
    cd /directory_with_frames_and_script/
    python3 gif_maker.py
