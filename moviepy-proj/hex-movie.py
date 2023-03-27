import time
import moviepy.editor as mp
from moviepy.editor import *


def hex_loop(start,end):
  for i in range(start,end):
    print(i))
    time.sleep(0.01)
    
a=hex_loop(0,10001)
obj=TextClip(a,font='Arial',fontsize=24)

clip.write_videofile("hex.mp4")
