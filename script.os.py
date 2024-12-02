import os.path
import shutil

# возвращает абсолютный путь к текущему исполняемому файлу
CURRENT_FILE = os.path.abspath(__file__)
print(CURRENT_FILE)

# возвращает директорию, в которой расположен текущий файл
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

# объединяет путь к текущей директории и строку 'tmp', создавая полный путь к временному каталогу tmp в текущей директории
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
print(TMP_DIR)

# создание новой директории
if not os.path.exists('tmp'):
    os.mkdir('tmp')
    print('tmp directory created')
else:
    print('tmp directory already exists')

shutil.rmtree(os.path.join(CURRENT_DIR, 'tmp')) # удаление директории