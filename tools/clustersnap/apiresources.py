'''
MIT License
Copyright (c) 2023 Atul Thosar (atulthosar@gmail.com)
'''

import execute
import constants

configs = ['current-context', 'get-contexts', 'get-users', 'view']

def apiresources_snap(baseDir):
    configDir = baseDir + constants.SLASH + constants.CONFIG_SUB_DIR 
    file = execute.prepFile(configDir, constants.API_RESOURCE_FILE)
    execute.log_cmd_output(constants.CMD_GET_API_RESOURCES, file)
