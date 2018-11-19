import os
import time


class FileWatcher:
    def __init__(self, path_of_file_to_watch):
        self.path_of_file_to_watch = path_of_file_to_watch
        self.new_size = self.file_size = os.stat(self.path_of_file_to_watch).st_size
        self.subscribers = []

    def subscribe(self, observer):
        # print("subscriber added {}".format(observer.name))
        self.subscribers.append(observer)

    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def check_file_size(self):
        print("File watch begins for file : {} ".format(self.path_of_file_to_watch))
        while True:
            # print("File check started with objects {}".format(self.subscribers))
            self.new_size = os.stat(self.path_of_file_to_watch).st_size
            if self.file_size != self.new_size:
                for name in self.subscribers:
                    # print("calling {}".format(name))
                    name.observer_message(self.new_size)
                self.file_size = self.new_size
            time.sleep(30)


class FileObserver:
    def __init__(self, name):
        self.name = name

    def observer_message(self, new_size):
        print("{} noticed that the file is now {} bytes".format(self.name, new_size))


if __name__ == "__main__":
    bob = FileObserver("Bob")
    john = FileObserver("John")
    stacy = FileObserver("Stacy")
    fw = FileWatcher("C:\\Users\\vadal\\Desktop\\housedata.txt")
    fw.subscribe(bob)
    fw.subscribe(john)
    fw.subscribe(stacy)
    fw.check_file_size()
