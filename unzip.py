import zipfile
import os


# Lấy thư mục chứa script
script_dir = os.path.dirname(os.path.abspath(__file__))
zip_path = os.path.join(script_dir, 'archive.zip')
extract_folder = os.path.join(script_dir, 'extracted_data')

os.makedirs(extract_folder, exist_ok=True)

try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Unzipped '{zip_path}' into folder '{extract_folder}/'")
    
except FileNotFoundError:
    print(f"Error: File '{zip_path}' not found. Please check if the file is in the same directory as the script.")
except zipfile.BadZipFile:
    print(f"Error: File '{zip_path}' is corrupted or not a valid .zip file.")