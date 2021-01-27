import os
import shutil

curent_dir = os.getcwd()

for f in os.listdir(r'C:\Users\zinck\Downloads'):
    edit2, file_ext = os.path.splitext(f)

    try:
        if not file_ext:
            pass
        elif file_ext in ('.mp4', '.mov', '.avi', '.mpg', '.mpeg', '.flv', '.h264'):
            shutil.move(
                os.path.join(r'C:\Users\zinck\Downloads', f'{edit2}{file_ext}'),
                os.path.join(r'C:\Users\zinck', 'Videos', f'{edit2}{file_ext}'))
        elif file_ext in ('.jpg', '.img', '.jpeg', '.gif', '.png', '.ps',):
            shutil.move(
                os.path.join(r'C:\Users\zinck\Downloads', f'{edit2}{file_ext}'),
                os.path.join(r'C:\Users\zinck', 'Pictures', f'{edit2}{file_ext}'))
        elif file_ext in ('.mp3', '.wav', '.mpa', '.aif'):
            shutil.move(
                os.path.join(r'C:\Users\zinck\Downloads', f'{edit2}{file_ext}'),
                os.path.join(r'C:\Users\zinck', 'Music', f'{edit2}{file_ext}'))
        elif file_ext in ('.txt', '.doc', '.docx', '.pdf', '.tex'):
            shutil.move(
                os.path.join(r'C:\Users\zinck\Downloads', f'{edit2}{file_ext}'),
                os.path.join(r'C:\Users\zinck\Documents', 'skole', f'{edit2}{file_ext}'))

    except (FileNotFoundError, PermissionError):
        pass