class FilesHandling:
    def create_and_write(self, file_name, content):
        with open(file_name, 'w') as f:
            f.write(content)
