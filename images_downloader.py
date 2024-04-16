from simple_image_download import simple_image_download as simp
import time
import os
from PIL import Image

response = simp.simple_image_download

keywords = ["cars"]

# Download images
for kw in keywords:
    response().download(kw, 50)
    time.sleep(5)  # Delay of 5 seconds

# Function to convert images to JPG
def convert_to_jpg(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            f, e = os.path.splitext(filepath)
            if e.lower() not in [".jpg", ".jpeg"]:
                try:
                    img = Image.open(filepath)
                    img.convert('RGB').save(f + '.jpg', 'JPEG')
                    os.remove(filepath)  # Remove the original file if not a jpg
                except Exception as e:
                    print(f"Error converting {file}: {e}")

# Convert downloaded images to JPG
for kw in keywords:
    download_path = os.path.join("./simple_images/", kw.replace(' ', '_'))
    convert_to_jpg(download_path)

print("Image download and conversion to JPG completed.")
