import os

def rename_dataset(base_path):
    current_id = 1

    subsets = ['train', 'val']
    
    for subset in subsets:
        img_dir = os.path.join(base_path, 'images', subset)
        lbl_dir = os.path.join(base_path, 'labels', subset)
        
        if not os.path.exists(img_dir) or not os.path.exists(lbl_dir):
            print(f"Skipping {subset} because the directory was not found.")
            continue
        image_files = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

        print(f"--- Processing {subset}: Starting from ID {current_id} ---")

        for img_name in image_files:
            name_only, extension = os.path.splitext(img_name)
            old_lbl_name = name_only + '.txt'
            old_img_path = os.path.join(img_dir, img_name)
            old_lbl_path = os.path.join(lbl_dir, old_lbl_name)
            new_img_path = os.path.join(img_dir, f"{current_id}{extension}")
            new_lbl_path = os.path.join(lbl_dir, f"{current_id}.txt")
            os.rename(old_img_path, new_img_path)
            if os.path.exists(old_lbl_path):
                os.rename(old_lbl_path, new_lbl_path)
            else:
                print(f"Warning: Label file not found for {img_name}")
            current_id += 1

    print(f"Completion! The last ID is {current_id - 1}")

script_dir = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.join(script_dir, 'extracted_data')
rename_dataset(root_path)