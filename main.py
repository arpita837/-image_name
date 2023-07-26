import os
import shutil
from PIL import Image

def add_image(image_path, image_name, destination_folder):
    # Check if the destination folder exists; if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Copy the image to the destination folder
    destination_path = os.path.join(destination_folder, image_name)
    shutil.copy(image_path, destination_path)
    print(f"Image '{image_name}' added successfully.")

def remove_image(image_name, folder):
    image_path = os.path.join(folder, image_name)
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Image '{image_name}' removed successfully.")
    else:
        print(f"Image '{image_name}' not found in the folder.")

def display_all_images(folder):
    image_names = os.listdir(folder)
    print("Images in the folder:")
    for image_name in image_names:
        print(image_name)

def display_image(image_name, folder):
    image_path = os.path.join(folder, image_name)
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img.show()
    else:
        print(f"Image '{image_name}' not found in the folder.")

# Example usage:

# Add an image to the repository
add_image("path/to/image.jpg", "image1.jpg", "repository_folder")

# Display all images in the repository
display_all_images("repository_folder")

# Display a specific image
display_image("image1.jpg", "repository_folder")

# Remove an image from the repository
remove_image("image1.jpg", "repository_folder")
