import os
import shutil
import cv2

edge_dir = 'edges'
drops_dir = 'Output_image'
labels_dir = 'Output_label'

destination_dir = os.path.join("repo", "dataset", "rain_train")

def make_edges(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)

        img = cv2.imread(filepath)

        if img is not None:
            
            #! TO DO
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 10, 255)

            destination_path = os.path.join(destination_dir, f"{filename}")
            cv2.imwrite(destination_path, edges)
            print(f"Edge-detected image saved: {destination_path}")
        else:
            print(f"Could not read image: {filepath}")

def rename_and_move(source_dir, destination_dir, file_type):
    for root, _, files in os.walk(source_dir):
        for filename in files:
            source_file = os.path.join(root, filename)
            new_filename = f"{filename}_{file_type}.png"
            destination_file = os.path.join(destination_dir, new_filename)
            shutil.move(source_file, destination_file)

make_edges(drops_dir, edge_dir)
rename_and_move(edge_dir, destination_dir, "E")
rename_and_move(drops_dir, destination_dir, "B")
rename_and_move(labels_dir, destination_dir, "M")