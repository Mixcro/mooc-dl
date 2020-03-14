#!usr/bin/env python3
import os


save_path = '/nfs/course/'

if __name__ == '__main__':
    while True:
        url = input('course url: ')
        if url:
            old_dirs = [i for i in os.listdir('./') if os.path.isdir(i)]
            os.system('python3 mooc-dl.py %s' % url)
            new_dirs = [i for i in os.listdir('./') if os.path.isdir(i)]
            target_dir = [i for i in new_dirs if i not in old_dirs][0]
            print('fond target dir %s, now moving.' % target_dir)
            os.system('rsync -avP %s %s' % (target_dir, save_path))
            print('done!\n\n')
        else:
            break
