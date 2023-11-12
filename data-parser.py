import os
import shutil

data_directory = "./dataset/"

# missing O
directories = os.listdir(data_directory)

for class_label, class_name in enumerate(directories):
    if class_name == class_name.lower():
        continue
    class_path = os.path.join(data_directory, class_name)
    for image_file in os.listdir(class_path):
        if "_" in image_file:
            old_class_path = os.path.join(class_path, image_file)
            new_class_path = os.path.join(data_directory, "@_" + class_name, image_file)
            if os.path.exists(old_class_path):
                os.makedirs(
                    os.path.join(data_directory, "@_" + class_name),
                    exist_ok=True,
                )
                shutil.copy(old_class_path, new_class_path)
                os.remove(old_class_path)

        elif not (image_file[:-4].isnumeric()):
            print(image_file)
            continue


target_directory = data_directory

min_file_count = float("inf")

subdirectories = [
    d
    for d in os.listdir(target_directory)
    if os.path.isdir(os.path.join(target_directory, d))
]

for directory in subdirectories:
    current_dir = os.path.join(target_directory, directory)
    files = os.listdir(current_dir)
    current_file_count = len(files)

    if current_file_count < min_file_count:
        file = directory
        min_file_count = current_file_count

# Set the desired file count based on the minimum found
desired_file_count = min_file_count

print(f"Minimum file count: {min_file_count, file}")

# Now, adjust all directories to have the desired file count
for directory in subdirectories:
    current_dir = os.path.join(target_directory, directory)
    files = os.listdir(current_dir)
    current_file_count = len(files)

    if current_file_count > desired_file_count:
        # Remove excess files
        for i in range(current_file_count - desired_file_count):
            file_to_remove = os.path.join(current_dir, files[i])
            os.remove(file_to_remove)

print(f"All directories now have the same number of files ({desired_file_count}).")
