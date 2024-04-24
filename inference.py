from ultralytics import YOLO
from pathlib import Path
import os
from PIL import Image
import cv2
import numpy as np  # Add this import statement for NumPy

# Define your paths
weights_path = "kangaroo.pt"
img_dir = "Kangaroo/Images"
output_dir = "predicted"  # Output directory for saving results
class_names = ['Kangaroo', 'Kangaroo Face', 'Non Kangaroo']  # Class names

# Initialize YOLOv5 model
model = YOLO(weights_path)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of image paths in the directory
img_paths = [str(img_path) for img_path in Path(img_dir).rglob("*.jpg")]

# Process each image in the directory
for img_path in img_paths:
    # Load the image
    img0 = Image.open(img_path)

    # Perform inference
    results = model(img0)

    # Convert image to OpenCV format
    img_cv2 = cv2.cvtColor(np.array(img0), cv2.COLOR_RGB2BGR)

    # Process each result in the list
    for i, result in enumerate(results.xyxy):
        for box in result:
            # Extract box coordinates and confidence
            x1, y1, x2, y2, confidence, cls = box

            # Adjust confidence threshold
            if confidence >= 0.4:
                # Convert coordinates to integer values
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Draw bounding box
                cv2.rectangle(img_cv2, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # Draw class name
                class_name = class_names[int(cls)]
                org = (x1, y1 - 10)
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 0.5
                color = (255, 0, 0)
                thickness = 2
                cv2.putText(img_cv2, class_name, org, font, fontScale, color, thickness)

    # Save the result with a unique filename in the output directory
    filename = os.path.join(output_dir, f"{Path(img_path).stem}_result.jpg")
    cv2.imwrite(filename, img_cv2)

print("Prediction results saved in the 'predicted' folder.")
