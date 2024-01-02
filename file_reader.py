import os

from pickle import dump,load

class FileReader:
    def __init__(self, base_path=""):
        self.base_path = base_path

    # Write the data inside the file with file_name
    def write_file(self, file_name, data):
        folder_path = os.path.join(self.base_path, "dataset")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Combine folder and file path
        file_path = os.path.join(folder_path, file_name)

        # Write the cleaned data to a new text file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

    # Open the file with file_name, extract the file data, and return it
    def open_file(self, file_name):
        file_path = os.path.join(self.base_path, "dataset", file_name)

        if os.path.exists(file_path):
            with open(file_path, 'r', encoding="utf-8") as file:
                f = file.read()
            return f
        else:
            print(f"File '{file_name}' not found.")
            return None



    # opne the file with file_name, extract the file data, and return it 
    def write_file_binary(self, file_name, data):
        folder_path = os.path.join(self.base_path, "dataset")

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Combine folder and file path
        file_path = os.path.join(folder_path, file_name)

        # Write the cleaned data to a new text file
        with open(file_path, 'wb') as file:
            dump(data, file)



    def open_file_binary(self, file_name):
        file_path = os.path.join(self.base_path, "dataset", file_name)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                f = load(file)
            return f
        else:
            print(f"File '{file_name}' not found")
            return None

