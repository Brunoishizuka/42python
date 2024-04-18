# program.py

# Import the path.py module from the installed location
import sys
sys.path.append("local_lib")  # Add the local_lib directory to the Python path
from path import Path

def main():
    # Create a folder and a file inside it
    folder_path = Path("output_folder")
    folder_path.mkdir(exist_ok=True)
    file_path = folder_path / "output_file.txt"
    
    # Write something in the file
    with open(file_path, "w") as file:
        file.write("Hello, this is written in the file!")

    # Read and display the file's content
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)

if __name__ == "__main__":
    main()
