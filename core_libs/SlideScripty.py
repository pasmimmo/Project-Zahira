import schedule, time, subprocess,os, threading, json
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from pathlib import Path


settings_path=Path.joinpath(Path.home(),'.SlideScripty','SlideSettings.json')
with open(settings_path) as settings_file:
    settings=json.load(settings_file)
monitoring_path = settings['img_path']
print(monitoring_path)
boolen = True
vlc_pid=None

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    print(f'Fai qualcosa quando creano un files in {event.src_path}')

def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    global vlc_pid
    #os.chdir(monitoring_path)
    subprocess.run([f'ffmpeg -framerate 1/3 -pattern_type glob -i "*.jpg" {monitoring_path}/Video/out.mp4 -y'],shell=True)
    #os.chdir(os.getcwd().join('vid'))
    os.remove(f'{monitoring_path}/Video/slideshow.mp4')
    os.rename(f'{monitoring_path}/Video/out.mp4',f'{monitoring_path}/Video/slideshow.mp4')
    temp_pid=lanch_vlc()
    time.sleep(15)
    vlc_pid.kill()
    vlc_pid=temp_pid

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")


def lanch_vlc():
    return subprocess.Popen([f'vlc --loop --no-osd -q {monitoring_path}/Video slideshow.mp4'],shell=True)


def screen_off():
    subprocess.call(['xrandr','--output','Virtual1','--off']) 

def screen_on():
    subprocess.call(['xrandr','--auto'])

#assegno le callback
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved
subfolder_monitoring = False
#setto l'Observer
my_observer = Observer()
my_observer.schedule(my_event_handler, monitoring_path, recursive=subfolder_monitoring)
#Avvio la monitorizzazione
my_observer.start()

#schedule.every(10).seconds.do(screen_manager)
schedule.every().day.at("08:30").do(screen_off)
schedule.every().day.at("22:30").do(screen_on)



try:
    os.chdir(monitoring_path)
    vlc_pid=lanch_vlc()
    while True:
        schedule.run_pending()
        time.sleep(1)
        print('[*]SlideScript in esecuzione ...')
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
