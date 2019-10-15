import subprocess, os
class Beatrice:
    def __init__(self, path, *args, **kwargs):
        self.path=path
    def make_video(self,video_name='Slideshow_temp.mp4'):
        os.chdir(self.path)
        subprocess.run([f'ffmpeg -framerate 1/5 -pattern_type glob -i "*.jpg" {video_name} -y'], shell=True)
    def start_video(self,video_name='Slideshow.mp4'):
        os.chdir(self.path)
        #subprocess.run([f'cvlc -q {video_name}'],shell=True)
if __name__ == "__main__":
    test=Beatrice(os.getcwd()).make_video()
    subprocess.run(['vlc Slideshow.mp4'],shell=True)
    os.rename('Slideshow_temp.mp4','Slideshow.mp4')