import os
from PIL import Image
import numpy as np

# Function to add an image to the repository
def add_image(image_path, image_name, repository_folder):
    # Copy the image to the repository folder with the given image name
    destination_path = os.path.join(repository_folder, image_name)
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    os.rename(image_path, destination_path)
    print(f"Image '{image_name}' added to the repository.")

# Function to remove an image from the repository
def remove_image(image_name, repository_folder):
    image_path = os.path.join(repository_folder, image_name)
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Image '{image_name}' removed from the repository.")
    else:
        print(f"Image '{image_name}' not found in the repository.")

# Function to display all image names in the repository folder
def display_image_names(repository_folder):
    image_names = os.listdir(repository_folder)
    if image_names:
        print("Image names in the repository:")
        for name in image_names:
            print(name)
    else:
        print("No images found in the repository.")

# Function to display an image from the repository
def display_image(image_name, repository_folder):
    image_path = os.path.join(repository_folder, image_name)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image.show()
    else:
        print(f"Image '{image_name}' not found in the repository.")

# Function to rotate an image
def rotate_image(image_name, repository_folder, degrees):
    image_path = os.path.join(repository_folder, image_name)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        rotated_image = image.rotate(degrees)
        return rotated_image
    else:
        print(f"Image '{image_name}' not found in the repository.")
        return None

# Main program
if __name__ == "__main__":
    repository_folder = "image_repository"
    
    while True:
        print("\nImage Repository Menu:")
        print("1. Add Image")
        print("2. Remove Image")
        print("3. Display Image Names")
        print("4. Display Image")
        print("5. Rotate Image")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            image_path = input("Enter the path of the image to add: ")
            image_name = input("Enter the image name: ")
            add_image(image_path, image_name, repository_folder)
        elif choice == "2":
            image_name = input("Enter the image name to remove: ")
            remove_image(image_name, repository_folder)
        elif choice == "3":
            display_image_names(repository_folder)
        elif choice == "4":
            image_name = input("Enter the image name to display: ")
            display_image(image_name, repository_folder)
        elif choice == "5":
            image_name = input("Enter the image name to rotate: ")
            degrees = int(input("Enter the rotation angle (positive for clockwise, negative for anticlockwise): "))
            rotated_image = rotate_image(image_name, repository_folder, degrees)
            
            if rotated_image:
                rotated_image.show()
                
                display_choice = input("Do you want to display the rotated image? (yes/no): ")
                if display_choice.lower() == "yes":
                    rotated_image.show()
                    
                save_choice = input("Do you want to save the rotated image? (yes/no): ")
                if save_choice.lower() == "yes":
                    new_folder = input("Enter the folder to save the rotated image: ")
                    new_image_name = input("Enter the new image name: ")
                    new_image_path = os.path.join(new_folder, new_image_name)
                    
                    os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
                    rotated_image.save(new_image_path)
                    print(f"Rotated image saved as '{new_image_name}' in '{new_folder}'.")
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
