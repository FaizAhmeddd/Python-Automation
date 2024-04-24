import os

folder_path = r'D:/Automatic-License-Plate-Recognition-using-YOLOv8-main/images'
start_number = 1

# Get the list of jpg files in the folder
jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

# Rename the files
for i, old_name in enumerate(jpg_files):
    new_name = f'{start_number + i}.jpg'  # Modify this line if you want a different naming convention
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)

    # Check if the destination file already exists
    if not os.path.exists(new_path):
        os.rename(old_path, new_path)
        print(f'Renamed: {old_name} to {new_name}')
    else:
        print(f'Skipped: {new_name} already exists')
