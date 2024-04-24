import os
import shutil

def read_yolo_labels(label_path):
    with open(label_path, 'r') as label_file:
        # Process the content of the label file as needed
        labels = label_file.readlines()
        # Example: Return the class and bounding box information
        return [label.strip() for label in labels]

def read_images_and_labels(image_directory, label_directory, output_image_directory, output_label_directory, image_extensions=["jpg", "jpeg", "png"]):
    image_paths = []
    label_paths = []

    # Walk through the image directory and its subdirectories
    for root, dirs, files in os.walk(image_directory):
        # Filter files based on image extensions
        image_paths.extend([os.path.join(root, file) for file in files if file.lower().endswith(tuple(image_extensions))])

    # Walk through the label directory and its subdirectories
    for root, dirs, files in os.walk(label_directory):
        # Filter files based on label extensions (assuming label files have the same name as images but with a ".txt" extension)
        label_paths.extend([os.path.join(root, file) for file in files if file.lower().endswith('.txt')])

    # Create output directories if they don't exist
    os.makedirs(output_image_directory, exist_ok=True)
    os.makedirs(output_label_directory, exist_ok=True)

    return image_paths, label_paths

def process_images_and_labels(image_paths, label_paths, output_image_directory, output_label_directory):
    for image_path in image_paths:
        # Extract the base name (excluding extension) of the image
        image_name = os.path.splitext(os.path.basename(image_path))[0]

        # Find corresponding label path based on the image name
        matching_label_paths = [label_path for label_path in label_paths if os.path.splitext(os.path.basename(label_path))[0] == image_name]

        if matching_label_paths:
            # If matching label paths are found, process the image and labels
            label_path = matching_label_paths[0]  # Assuming there's only one matching label file
            print("Processing image and labels:", image_path, label_path)

            # Add your image processing logic here

            # Example: Copy the image to the output image directory
            output_image_path = os.path.join(output_image_directory, os.path.basename(image_path))
            shutil.copy(image_path, output_image_path)

            # Example: Get labels and save them to a text file in the output label directory
            labels = read_yolo_labels(label_path)
            label_output_path = os.path.join(output_label_directory, os.path.basename(label_path).replace('.txt', '') + '.txt')

            with open(label_output_path, 'w') as label_output_file:
                label_output_file.write('\n'.join(labels))
        else:
            print("No matching label found for image:", image_path)

# Replace 'your_image_directory', 'your_label_directory', 'your_output_image_directory', and 'your_output_label_directory'
image_directory = "D:/license_plate_data/Images"
label_directory = "D:/license_plate_data/Labels"
    
output_image_directory = 'D:/images'
output_label_directory = 'D:/labels'
image_paths, label_paths = read_images_and_labels(image_directory, label_directory, output_image_directory, output_label_directory)

# Process images and labels
process_images_and_labels(image_paths, label_paths, output_image_directory, output_label_directory)
