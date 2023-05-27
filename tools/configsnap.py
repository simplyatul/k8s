'''
MIT License
Copyright (c) 2023 Atul Thosar (atulthosar@gmail.com)
'''
import execute

configs = ['current-context', 'get-contexts', 'get-users', 'view']

def config_snap(dirName):
    for c in configs:
        cmd = 'kubectl config ' + c
        file = dirName + '/' + 'config-' + c + '.txt'
        # print(cmd, file)
        execute.log_cmd_output(cmd, file)
