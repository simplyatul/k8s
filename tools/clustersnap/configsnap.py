'''
MIT License
Copyright (c) 2023 Atul Thosar (atulthosar@gmail.com)
'''

import execute
import constants

configs = ['current-context', 'get-contexts', 'get-users', 'view']

def config_snap(baseDir):
    configDir = baseDir + constants.SLASH + constants.CONFIG_SUB_DIR 
    for c in configs:
        cmd = 'kubectl config ' + c
        file = configDir + constants.SLASH + c + constants.FILE_EXT
        # print(cmd, file)
        execute.log_cmd_output(cmd, file)
