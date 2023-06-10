import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        heic_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".heic")
        im.save(heic_path, format="HEIC", quality_mode="lossless")

def choose_folder(message):
    folder_path = input(message + "\nEnter the path to the folder: ")
    while not os.path.exists(folder_path):
        folder_path = input("The folder doesn't exist. Please enter a valid path to the folder: ")
    return folder_path

def main():
    print("Welcome to JPG to HEIC Converter!")
    jpg_folder = choose_folder("Enter the path to the folder containing the .jpg images:")
    heic_folder = choose_folder("Enter the path to the output folder for the .heic images:")
    # Create the output folder if it doesn't exist yet
    if not os.path.exists(heic_folder):
        os.makedirs(heic_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, heic_folder)
    print("All images converted successfully to HEIC format and saved in the chosen folder!")

if __name__ == "__main__":
    main()

# softy_plug