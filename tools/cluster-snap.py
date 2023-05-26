import os, sys, time
import shlex, subprocess

kubectl_global_options = ' -o wide'
dirPrefix = 'cluster-snapshot-'

def create_dir():
    global dirName
    dirName = dirPrefix + time.strftime("%Y-%m-%d-%H-%M-%S")
    try:
        os.makedirs(dirName)
    except FileExistsError as err:
        print('Unable to create directory: ', dirName)
        print('Exception: ', err)
        sys.exit(1)

def snap_resource(res_name):
    cmd = 'kubectl get ' + res_name + kubectl_global_options
    file = dirName + '/' + res_name + '.txt'

    with open(file, 'w') as f:
        f.write('$ ' + cmd + '\n')

    with open(file, 'a') as stdout_file:
        subprocess.run(shlex.split(cmd), stdout=stdout_file, stderr=subprocess.PIPE, text=True)

def api_resources_w_namespace_scope():
    apires_cmd_w_ns = 'kubectl api-resources -o=name --namespaced=true'
    o = subprocess.run(shlex.split(apires_cmd_w_ns), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    global apires_w_ns
    apires_w_ns = o.stdout.split("\n");

def api_resources_wo_namespace_scope():
    apires_cmd_wo_ns = 'kubectl api-resources -o=name --namespaced=false'
    o = subprocess.run(shlex.split(apires_cmd_wo_ns), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    global apires_wo_ns
    apires_wo_ns = o.stdout.split("\n");

def log_api_resources_wo_namespace_scope():
    for r in apires_wo_ns:
        snap_resource(r)

print('Starting snapshot')
create_dir(); print(dirName + ' directory created')
api_resources_wo_namespace_scope(); log_api_resources_wo_namespace_scope()
