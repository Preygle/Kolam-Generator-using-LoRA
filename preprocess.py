from PIL import Image
import os

input_folder = "input_images" # change to ur input folder
output_folder = "black_white" # change to ur output folder

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith((".jpg", ".png", ".jpeg")):
        img = Image.open(os.path.join(input_folder, file)).convert("L")  # grayscale
        img.save(os.path.join(output_folder, file))
