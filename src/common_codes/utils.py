import os

class Utils:
    @staticmethod
    def get_file_path(filename, search_directory='resources'):
        """
        Search for a file in the current directory and parent directories,
        within the 'search_directory' folder.
        
        :param filename: Name of the file you're searching for.
        :param search_directory: Folder where the file is located.
        :return: Absolute file path if found, None otherwise.
        """
        current_directory = os.getcwd()

        while True:
            # Construct the path to the search directory
            target_directory = os.path.join(current_directory, search_directory)
            file_path = os.path.join(target_directory, filename)
            
            if os.path.exists(file_path):
                # If file exists, return its absolute path
                return os.path.abspath(file_path)

            # Move one level up
            parent_directory = os.path.dirname(current_directory)
            
            # If reached the root directory, stop searching
            if current_directory == parent_directory:
                print(f"File '{filename}' not found.")
                return None

            current_directory = parent_directory
