'''
MIT License
Copyright (c) 2023 Atul Thosar (atulthosar@gmail.com)
'''

import shlex, subprocess, constants

def log_cmd_output(cmd, file):
        '''
        Not the good way to open filetwo times
        But somehow
        '''
        with open(file, 'w') as f:
            f.write('$ ' + cmd + '\n')

        with open(file, 'a') as stdout_file:
            subprocess.run(shlex.split(cmd), stdout=stdout_file, stderr=stdout_file, text=True)

def prepFile(dirName, fileName):
     file = dirName + '/' + fileName + constants.FILE_EXT
     return file