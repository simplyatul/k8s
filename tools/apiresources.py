'''
MIT License
Copyright (c) 2023 Atul Thosar (atulthosar@gmail.com)
'''
import execute
import constants

configs = ['current-context', 'get-contexts', 'get-users', 'view']

def apiresources_snap(dirName):
    file = execute.prepFile(dirName, constants.API_RESOURCE_FILE)
    execute.log_cmd_output(constants.CMD_GET_API_RESOURCES, file)
