import os
import shutil

# Path to the directory containing your images
image_directory = "D:/newdataframes"

# Create a new directory to store the folders
output_directory = "D:/New folder"
os.makedirs(output_directory, exist_ok=True)

# Set the start and end image indices
start_image = 1
end_image = 3622  # 186284-192253

# Number of persons to divide the images among
num_persons = 5

# Calculate the range of images each person will get
images_per_person = (end_image - start_image + 1) // num_persons

# Iterate through the range of image numbers for each person
for person in range(1, num_persons + 1):
    person_output_directory = os.path.join(output_directory, f"person_{person}")
    os.makedirs(person_output_directory, exist_ok=True)

    # Create subfolders for each person
    for subfolder in range(1000):
        subfolder_path = os.path.join(person_output_directory, f"{subfolder * 1000}-{(subfolder + 1) * 1000 - 1}")
        os.makedirs(subfolder_path, exist_ok=True)

    # Determine the start and end image indices for the current person
    person_start_image = start_image + (person - 1) * images_per_person
    person_end_image = min(person_start_image + images_per_person - 1, end_image)

    # Copy images to the corresponding subfolders for the current person
    for image_number in range(person_start_image, person_end_image + 1):
        image_filename = f"{image_number}.jpg"  # Adjust the file extension if needed
        source_path = os.path.join(image_directory, image_filename)
        
        # Calculate the subfolder index based on the image number
        subfolder_index = (image_number - start_image) // 1000
        destination_path = os.path.join(person_output_directory, f"{subfolder_index * 1000}-{(subfolder_index + 1) * 1000 - 1}", image_filename)

        # Check if the source image file exists before copying
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
        else:
            print(f"Warning: Image {image_number} not found.")

print("Images moved to respective folders successfully.")
