import os

def file_counter(input_folder):
    extension_count = {}
    total_files = 0
    
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            total_files += 1
            
            extension = os.path.splitext(file)[1].lower()
            if extension in extension_count:
                extension_count[extension] += 1
            else:
                extension_count[extension] = 1
    
    print(f"total_files = {total_files}")

    for ext, count in extension_count.items():
        ext = ext[1:] if ext.startswith('.') else ext
        print(f"total_{ext}_files = {count}")

file_counter('input_folder')
