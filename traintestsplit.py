import os
import shutil
from sklearn.model_selection import train_test_split

def split_data(images_folder, labels_folder, output_path, train_ratio=0.8, random_seed=42):

    """
This script defines a function 'split_data' that takes as input the paths to folders containing images and their corresponding labels,
and splits the data into training and validation sets. The script uses the scikit-learn library's 'train_test_split' function to achieve
this split based on a specified training ratio. The resulting data is organized into new folders for training and validation sets.

The script can be executed independently, and it includes a main block where the function 'split_data' is called with specific paths for
images, labels, and the desired output directory. The main block specifies the source paths for the images and labels, as well as the
output directory where the split data will be stored.

Functions:
- split_data(images_folder, labels_folder, output_path, train_ratio=0.8, random_seed=42):
  - Parameters:
    - images_folder: Path to the folder containing the images.
    - labels_folder: Path to the folder containing the corresponding labels.
    - output_path: Path to the desired output directory where the split data will be stored.
    - train_ratio: The ratio of data to be used for training (default is 0.8).
    - random_seed: Seed for randomization to ensure reproducibility (default is 42).
  - Functionality:
    - Lists image and label filenames, sorts them to match pairs, and splits the data into training and validation sets.
    - Creates new folders for training and validation sets within the specified output directory.
    - Moves the images and labels to their respective folders in the training and validation sets.

Main block:
- Defines paths to the images and labels folders, as well as the desired output directory.
- Calls the 'split_data' function with the specified paths.

Note: Ensure that the script is executed in an environment with the required dependencies, including scikit-learn.
    """

    # Get the list of image and label filenames
    image_filenames = os.listdir(images_folder)
    label_filenames = os.listdir(labels_folder)

    # Make sure the lists are sorted to match image-label pairs
    image_filenames.sort()
    label_filenames.sort()

    # Split the data into training and validation sets
    image_train, image_val, label_train, label_val = train_test_split(
        image_filenames, label_filenames, train_size=train_ratio, random_state=random_seed
    )

    # Create new folders for training and validation sets
    train_data_folder = os.path.join(output_path, "train_data")
    train_images_folder = os.path.join(train_data_folder, "images", "train")
    val_images_folder = os.path.join(train_data_folder, "images", "validation")
    train_labels_folder = os.path.join(train_data_folder, "labels", "train")
    val_labels_folder = os.path.join(train_data_folder, "labels", "validation")

    os.makedirs(train_data_folder, exist_ok=True)
    os.makedirs(train_images_folder, exist_ok=True)
    os.makedirs(val_images_folder, exist_ok=True)
    os.makedirs(train_labels_folder, exist_ok=True)
    os.makedirs(val_labels_folder, exist_ok=True)

    # Move training data to new folders
    for img_filename, label_filename in zip(image_train, label_train):
        shutil.move(os.path.join(images_folder, img_filename), os.path.join(train_images_folder, img_filename))
        shutil.move(os.path.join(labels_folder, label_filename), os.path.join(train_labels_folder, label_filename))

    # Move validation data to new folders
    for img_filename, label_filename in zip(image_val, label_val):
        shutil.move(os.path.join(images_folder, img_filename), os.path.join(val_images_folder, img_filename))
        shutil.move(os.path.join(labels_folder, label_filename), os.path.join(val_labels_folder, label_filename))

if __name__ == "__main__":
    # Specify the paths to your images and labels folders



    images_folder_path = "D:/images"
    labels_folder_path = "D:/labels"
    
    # Specify the output directory path
    output_directory_path = "D:/train_data"

    # Call the split_data function
    split_data(images_folder_path, labels_folder_path, output_directory_path)

