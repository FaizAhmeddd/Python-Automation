import os
import cv2
import numpy as np
import glob

def enhance_and_reduce_noise(input_folder, output_folder):
    """
    Enhances and reduces noise in images within the specified input folder and saves the processed images
    to the specified output folder. The enhancement is applied only to images with a brightness threshold
    below 80. The function uses various image processing techniques such as contrast enhancement, denoising,
    and gamma correction to improve image quality.

    Parameters:
    - input_folder (str): Path to the folder containing input images.
    - output_folder (str): Path to the folder where processed images will be saved.
    """
    def read_image(image_path):
        return cv2.imread(image_path)

    def calculate_brightness_threshold(image):
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculate the mean pixel value as the brightness threshold
        brightness_threshold = np.mean(gray_image)
        
        return brightness_threshold

    def save_image(image, folder, filename):
        output_path = os.path.join(folder, filename)
        cv2.imwrite(output_path, image)

    def enhance_image(image, clip_limit=4.0, tile_size=(8, 8), gamma=5.0):
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_size)
        l_eq = clahe.apply(l)
        lab_eq = cv2.merge((l_eq, a, b))
        output_image = cv2.cvtColor(lab_eq, cv2.COLOR_LAB2BGR)
        output_image = np.power(output_image/255.0, gamma)
        output_image = (output_image * 255).astype(np.uint8)

        return output_image

    def reduce_noise(image):
        return cv2.fastNlMeansDenoisingColored(image, None, 5, 5, 3, 9)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over each image file in the input folder
    for image_path in glob.glob(os.path.join(input_folder, '*.jpg')) + glob.glob(os.path.join(input_folder, '*.png')):
        # Read the image
        image = read_image(image_path)

        # Calculate brightness threshold
        brightness_threshold = calculate_brightness_threshold(image)

        # Check if brightness is below 80
        if brightness_threshold < 80:
            # Enhance the image
            enhanced_image = enhance_image(image, clip_limit=2.0, tile_size=(2, 2), gamma=0.7)
            # Reduce noise in the enhanced image
            denoised_image = reduce_noise(enhanced_image)
            # Extract filename
            filename = os.path.basename(image_path)
            # Save the denoised image with the same name in the output folder
            save_image(denoised_image, output_folder, filename)
            print(f"Enhanced and reduced noise for {filename}")
        else:
            # Save the original image
            filename = os.path.basename(image_path)
            save_image(image, output_folder, filename)
            print(f"Copied {filename} without enhancement")

# Replace 'D:/New folder' with the actual path to your input folder
input_folder = r'D:/New folder'
# Replace 'D:/Enhanced_Images' with the actual path to your output folder
output_folder = r'D:/Enhanced_Images'
enhance_and_reduce_noise(input_folder, output_folder)
