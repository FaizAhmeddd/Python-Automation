import os
import shutil

# Path to the directory containing your images
image_directory = "D:/outside data/0-78167"

# Create a new directory to store the folders
output_directory = "D:/outside data"
os.makedirs(output_directory, exist_ok=True)

# Set the start and end image indices
start_image = 0
end_image = 78167 # 186284-192253

# Iterate through the range of image numbers
for start in range(start_image, end_image + 1, 9999):
    end = min(start + 10000, end_image)  # Ensure the end image is within the specified range

    # Create the folder name (e.g., "274472-275471")
    folder_name = f"{start}-{end}"

    # Create the folder in the output directory
    folder_path = os.path.join(output_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Copy images to the corresponding folder
    for image_number in range(start, end + 1):
        image_filename = f"{image_number}.jpg"  # Adjust the file extension if needed
        source_path = os.path.join(image_directory, image_filename)
        destination_path = os.path.join(folder_path, image_filename)

        # Check if the source image file exists before copying
        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            print(f"Warning: Image {image_number} not found.")

print("Images moved to respective folders successfully.")
