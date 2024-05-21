import os

images_directory = "C:/Users/minal/PycharmProjects/DEA-Net/dataset/UIEB_DATASET/clear"

image_filenames = sorted(os.listdir(images_directory))[:400]

for i, filename in enumerate(image_filenames, start=1):
    old_path = os.path.join(images_directory, filename)
    new_path = os.path.join(images_directory, f"{i}.png")

    # Check if the new filename already exists
    if not os.path.exists(new_path):
        os.rename(old_path, new_path)
    else:
        print(f"Skipped renaming {old_path} because {new_path} already exists.")


#n01664065_312.jpg
