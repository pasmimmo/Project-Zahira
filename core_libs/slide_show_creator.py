import os, subprocess
os.chdir('/home/pi/Desktop/tmp')
subprocess.call(["ffmpeg","-r","1/5","-pattern_type","glob","-i","*.png","-c:v","libx264","-r", "30", "-pix_fmt", "yuv420p", 'video.mp4'])
