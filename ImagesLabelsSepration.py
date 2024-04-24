import os
import shutil

def separate_images_and_labels(input_folder, output_image_folder, output_label_folder):
    # Create output folders if they don't exist
    if not os.path.exists(output_image_folder):
        os.makedirs(output_image_folder)
    if not os.path.exists(output_label_folder):
        os.makedirs(output_label_folder)

    # Traverse through all subdirectories recursively
    for root, _, files in os.walk(input_folder):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)

            # Check if the file is an image file
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Move the image file to the output image folder
                print(f"Moving image file: {file_path}")
                shutil.move(file_path, os.path.join(output_image_folder, file))
            
            # Check if the file is a label file (text file)
            elif file.lower().endswith('.txt'):
                # Move the label file to the output label folder
                print(f"Moving label file: {file_path}")
                shutil.move(file_path, os.path.join(output_label_folder, file))

if __name__ == "__main__":
    input_folder = "D:/yolo_plate_dataset"
    output_image_folder = "D:/license_plate_data/Images"
    output_label_folder = "D:/license_plate_data/Labels"
    
    separate_images_and_labels(input_folder, output_image_folder, output_label_folder)
    print("Images and labels separated successfully.")
