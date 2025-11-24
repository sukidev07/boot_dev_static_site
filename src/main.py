import os

import shutil

# Delete all files and folders in the public directory then copy all files and folders from the static directory to the public directory
# the function should be recursive and handle nested folders
def main():
    public_dir = "public"
    static_dir = "static"

    # Delete all files and folders in the public directory
    if os.path.exists(public_dir):
        # Remove the public directory and all its contents
        shutil.rmtree(public_dir)
    # Recreate the public directory
    os.makedirs(public_dir, exist_ok=True)

    # Copy all files and folders from the static directory to the public directory recursively
    if os.path.exists(static_dir):
        # Copytree requires the destination to not exist, so we copy contents individually
        for item in os.listdir(static_dir):
            s = os.path.join(static_dir, item)
            d = os.path.join(public_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
if __name__ == "__main__":
    main()
