import os


class FileReader:
    
    # write the data inside the file with file_name
    def write_file(self,file_name, data):
        if not os.path.exists("dataset"):
            os.makedirs("dataset")
        # Combine folder and file path
        file_path = os.path.join("dataset", file_name)
        
        # Write the cleaned data to a new text file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

    # opne the file with file_name, extract the file data, and return it 
    def open_file(self, file_name):
        file_path = os.path.join("dataset", file_name)
        f = open(file_path, 'r', encoding="utf-8").read()
        return f
