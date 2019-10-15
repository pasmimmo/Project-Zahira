import os, subprocess
subprocess.call(['ffmpeg','-framerate','1/3','-pattern_type','glob','-i','*.jpg','out.mp4'])