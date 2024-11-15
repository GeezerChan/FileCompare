import os

def compare_mp3_files(folder1, folder2, desktop_path):
    # Get lists of .mp3 files in each folder
    files1 = {file for file in os.listdir(folder1) if file.endswith('.mp3')}
    files2 = {file for file in os.listdir(folder2) if file.endswith('.mp3')}
    
    # Find duplicates and non-duplicates
    duplicates = list(files1 & files2)
    unique_in_folder1 = list(files1 - files2)
    unique_in_folder2 = list(files2 - files1)
    
    # Write results to text files on the desktop with UTF-8 encoding
    with open(os.path.join(desktop_path, 'duplicates.txt'), 'w', encoding='utf-8') as file:
        file.write("Duplicates:\n" + "\n".join(duplicates))
        
    with open(os.path.join(desktop_path, 'unique_in_folder1.txt'), 'w', encoding='utf-8') as file:
        file.write("Unique in Folder 1:\n" + "\n".join(unique_in_folder1))
        
    with open(os.path.join(desktop_path, 'unique_in_folder2.txt'), 'w', encoding='utf-8') as file:
        file.write("Unique in Folder 2:\n" + "\n".join(unique_in_folder2))

# Example usage:
folder1 = 'F:\MyStuff\Music\SpotifyJapanese'
folder2 = 'F:\MyStuff\Music\Music(Sorted)'
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

compare_mp3_files(folder1, folder2, desktop_path)

print("Text files with results have been created on the desktop.")

