from time import sleep
from datetime import datetime, timedelta
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os

# Now I'm making my own linter, wonderful, just wonderful, goorm.
# Referenced Following:
# https://stackoverflow.com/questions/18599339/python-watchdog-monitoring-file-for-changes
# https://pythonhosted.org/watchdog/quickstart.html#a-simple-example

# TODO: in-depth understanding of how this works.
# TODO: add autopep8 with some function call, no concrete plan yet.
# autopep8 --in-place --aggressive --aggressive .py

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        global out
        self.event_quene = []
        self.last_modified = datetime.now()

    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()

        if not event.is_directory:
            self.event_quene.append((event.event_type, event.src_path))
            print(self.event_quene)
            
            
        if out:

            print(f'!! Type: {event.event_type} At {datetime.now()}')
            print(f'!! Path: {event.src_path}')


class PEP8_Handler(FileChangeHandler):
    def __init__(self):
        super().__init__()
        
        if self.event_quene:
            event_type, source = self.event_quene.pop()

            if str(event_type) == 'modified':
                print(source)
                
                source_array = source.split('//')

                if '.py' in source_array[-1]:
                    os.system('PEP8 ' + source)
                    _ = input("Press Enter to skip")
                    os.system('clear')


if __name__ == '__main__':
    global out
    print('< PEP8 auto linter >')
    
    option = input('Do you want to show Filechange logs? (y/n):')
    if option == 'y':
        out = True
    else:
        out = False
    
    
    event_handler = PEP8_Handler()
    observer = Observer()
    observer.schedule(event_handler, path='../', recursive=True)
    observer.start()

    try:
        while True:
            sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()
