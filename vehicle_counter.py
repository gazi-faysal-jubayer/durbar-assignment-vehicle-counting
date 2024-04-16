import cv2
import glob
from vehicle_detector import VehicleDetector
import pandas as pd

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folder
images_folder = glob.glob("images/*.jpg") + glob.glob("images/*.jpeg")

total_vehicles_count = 0

my_dict = {
    "Image Path": [],
    "Number of Vehicles": []
}

# Loop through all the images
for img_path in images_folder:
    # print("Img path", img_path)
    img = cv2.imread(img_path)

    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    total_vehicles_count += vehicle_count
    
    my_dict["Image Path"].append(img_path)
    my_dict["Number of Vehicles"].append(vehicle_count)

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    cv2.imshow("Cars", img)
    cv2.waitKey(1)

my_dict["Image Path"].append('Total vehicle in the folder')
my_dict["Number of Vehicles"].append(total_vehicles_count)

# Convert dictionary to DataFrame
df = pd.DataFrame(my_dict)

# Save DataFrame to CSV
df.to_csv('no_car_.csv', index=False)