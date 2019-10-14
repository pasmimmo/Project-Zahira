import schedule, time, subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
path = "/home/pi/Desktop/BT"
boolen = True
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    print(f"Fai qualcosa quando creano un files in {event.src_path}")

def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    
def screen_manager():
    global boolen
    print("Codice per spegnere lo schermo")
    if(boolen):
        subprocess.call(["vcgencmd", "display_power", "0"])
        boolen= False
    else:
        subprocess.call(["vcgencmd", "display_power", "1"])
        boolen= True
        
def screen_off():
    subprocess.call(["vcgencmd", "display_power", "0"])

def screen_on():
    subprocess.call(["vcgencmd", "display_power", "1"])

        
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved
subfolder_monitoring = False
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=subfolder_monitoring)
my_observer.start()
schedule.every(10).seconds.do(screen_manager)
schedule.every().day.at("08:30").do(screen_off)
schedule.every().day.at("22:30").do(screen_on)



try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()