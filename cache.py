import os
import shutil


path_cache = 'C:\\Users\\<username>\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\nahd6ha2.default\\cache2\\entries'
norm_path_cache = os.path.normpath(path_cache)
path_target_dir = 'C:\\Users\\booya\\Desktop\\music'
norm_path_target_dir = os.path.normpath(path_target_dir)

print(norm_path_cache)

for _, _, filenames in os.walk(norm_path_cache):
    for filename in filenames:
        full_path = os.path.join(norm_path_cache, filename)
        if 11500 > os.path.getsize(full_path)/1024 > 6000:
            print(f'{filename} - {os.path.getsize(full_path) / 1024} кб')
            os.rename(full_path, full_path + '.mp3')
            shutil.move(full_path + '.mp3', norm_path_target_dir)



