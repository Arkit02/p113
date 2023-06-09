import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir="C:/Users/Arkit/Downloads"
class fileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hii, {event.src_path} has been created")
    def on_deleted(self,event):
        print(f"oops someone deleted {event.src_path} ")
    def on_modified(self,event):
        print(f"hii there, {event.src_path} has been modified")
    def on_moved(self,event):
        print(f"someone Moved {event.src_path} to {event.dest_path} ")
event_handler=fileEventHandler()
observer=Observer()
observer.schedule(event_handler,fromdir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running....")
except KeyboardInterrupt:
    print("stop")
    observer.stop()