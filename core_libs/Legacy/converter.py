import ffmpeg
(
ffmpeg
.input('*.png',pattern_type='glob',framerate=1/3)
#.filter('scale', size='hd720', force_original_aspect_ratio='increase')
.drawtext('SlideScripty Created By Pasmimmo')
.output('slideshow.mp4')
.overwrite_output()
.run()
)
