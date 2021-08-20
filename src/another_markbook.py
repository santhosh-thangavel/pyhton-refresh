import os


class MarkBook:

    def __init__(self, cache_directory):  #temporary directory
        self.marks = {}
        self.filename = os.path.join(cache_directory, "markbook.txt") # pass temporary directory to the constructor,cache file
        self.cache = open(self.filename, "w") # open cache file in constructor

    def add(self, name, mark):
        self.marks[name] = mark

    def lookup(self, name):
        return self.marks[name]

    def get_names(self):
        return set(self.marks.keys())

    def clear(self):
        self.cache.close()  # close the file
        os.remove(self.filename) # remove it from the file system