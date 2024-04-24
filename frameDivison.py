import os
import shutil

# Path to the directory containing your images
image_directory = "D:/newdataframes"

# Create a new directory to store the folders
output_directory = "D:/divison"
os.makedirs(output_directory, exist_ok=True)



# Set the start and end image indices
start_image = 1
end_image = 3622

# Calculate the number of images for each person
total_images = end_image - start_image + 1
images_per_person = total_images // 5
remainder = total_images % 5

# Iterate through each person
for person_index in range(1, 6):
    # Create a folder for each person
    person_folder_name = f"Person_{person_index}"
    person_folder_path = os.path.join(output_directory, person_folder_name)
    os.makedirs(person_folder_path, exist_ok=True)

    # Calculate the start and end image indices for this person
    person_start_image = start_image + (person_index - 1) * images_per_person
    person_end_image = person_start_image + images_per_person - 1

    # Adjust the end image index for the last person to account for remainder
    if person_index == 5:
        person_end_image += remainder

    # Iterate through the range of image numbers for this person
    for start in range(person_start_image, person_end_image + 1, 1500):
        end = min(start + 1499, person_end_image)  # Ensure the end image is within the specified range

        # Create the folder name (e.g., "274472-275471")
        folder_name = f"{start}-{end}"

        # Create the folder in the output directory
        folder_path = os.path.join(person_folder_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Create directories for images and labels inside the batch folder
        images_folder_path = os.path.join(folder_path, "images")
        labels_folder_path = os.path.join(folder_path, "labels")
        os.makedirs(images_folder_path, exist_ok=True)
        os.makedirs(labels_folder_path, exist_ok=True)

        # Copy images to the corresponding folder for this person
        for image_number in range(start, end + 1):
            image_filename = f"{image_number}.jpg"  # Adjust the file extension if needed
            source_path = os.path.join(image_directory, image_filename)
            destination_path = os.path.join(images_folder_path, image_filename)

            # Check if the source image file exists before copying
            if os.path.exists(source_path):
                shutil.copy(source_path, destination_path)
            else:
                print(f"Warning: Image {image_number} not found.")

print("Images and labels directories created successfully.")