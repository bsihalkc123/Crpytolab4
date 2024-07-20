import os
import shutil

def copy_self(destination_file):
    # Get the path of the current script
    current_script = __file__
    
    # Copy itself to the destination file
    shutil.copy(current_script, destination_file)

def main():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # List of target files to copy to
    target_files = ['copy1.py', 'copy2.py', 'copy3.py']
    
    # Copy the current script to each target file
    for target in target_files:
        destination_file = os.path.join(current_dir, target)
        copy_self(destination_file)
        print(f"Copied to {destination_file}")

if __name__ == "__main__":
    main()
