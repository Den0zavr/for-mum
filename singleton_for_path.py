class FilePathSingleton(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.file_path = None
        return cls._instance

    def set_file_path(self, new_path):
        self.file_path = new_path

    def set_file_suffix(self, new_suffix):
        self.file_suffix = new_suffix

    def get_file_path(self):
        return self.file_path

    def get_file_path_only(self):
        return self.file_path.strip()[:self.file_path.rindex("/")+1]
    
    def get_file_name(self):
        return self.file_path.strip()[self.file_path.rindex("/")+1:]

    def get_file_suffix(self):
        return self.file_path.strip()[self.file_path.rindex("."):]
    
    def get_file_name_only(self):
        return self.file_path.strip()[self.file_path.rindex("/")+1:self.file_path.rindex(".")]
    
    def remove_file_path(self):
        self.file_path = None
