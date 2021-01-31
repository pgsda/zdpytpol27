import os


class FilesHandling:
    def __init__(self):
        self.file_name_pattern = 'files/{}.ddb'

    def write(self, file_name, content):
        with open(self.file_name_pattern.format(file_name), 'a') as f:
            f.write(content + '\n')

    def if_exists(self, file_name):
        return os.path.isfile(self.file_name_pattern.format(file_name))
