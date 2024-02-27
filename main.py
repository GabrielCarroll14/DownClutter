import os
import shutil

downloads = r"C:\Users\Gabriel\Downloads"
photos_path = r"C:\Users\Gabriel\Pictures"
docs_path = r"C:\Users\Gabriel\Documents"
vid_path = r"C:\Users\Gabriel\Videos"
music_path = r"C:\Users\Gabriel\Music"


with os.scandir(downloads) as entries:
    for entry in entries:
        
        if entry.name.endswith((".png", ".jpeg", ".jpg")) and entry.is_file():
            file_path = os.path.join(downloads, entry.name)
            destination_path = os.path.join(photos_path, entry.name)
            shutil.move(file_path, destination_path)
            
        elif entry.name.endswith((".txt", ".pdf")) and entry.is_file():
            file_path = os.path.join(downloads, entry.name)
            destination_path = os.path.join(docs_path, entry.name)
            shutil.move(file_path, destination_path)
            
        elif entry.name.endswith(".mp4") and entry.is_file():
            file_path = os.path.join(downloads, entry.name)
            destination_path = os.path.join(vid_path, entry.name)
            shutil.move(file_path, destination_path)
            
        elif entry.name.endswith((".mp3", ".wav")) and entry.is_file():
            file_path = os.path.join(downloads, entry.name)
            destination_path = os.path.join(music_path, entry.name)
            shutil.move(file_path, destination_path)
            
        print("Your downloads has been decluttered!")
        
