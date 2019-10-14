import subprocess,os
count=0
input_dir='/home/pi/Desktop/imgSources'
output_dir='/home/pi/Desktop/tmp/'
for img in os.listdir(input_dir):
    count+=1
    resized=output_dir+str(count)+"_IMG.png"
    subprocess.call(['ffmpeg', '-i', input_dir+'//'+img, '-vf', 'scale=1920:-1', resized])