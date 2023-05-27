#!/usr/bin/python3
'''
MIT License
Copyright (c) 2023 Atul Thosar (atulthosar@gmail.com)
'''

'''
Assumptions:
- kubectl is installed
- k8s cluster exists

Script Usage:
- Fetch namespaced and non-namespaced k8s api-resources
- execute kubectl apply on each resource
- log the output of kubectl apply
- File Format:
    - If resource is namespaced:
        <resource name>.<namespace name>.txt
    - If resource is not namespaced:
        <resource name>.txt

ToDo:
- add pre-checks
    - kubectl exists and working
- arg to log output to stdout. Default is in file 
- arg to pass resource list. Log only those resources. Default is all resources

'''

import os, sys, time
import shlex, subprocess
from configsnap import *
from execute import log_cmd_output

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

def list_namespaces():
    get_ns_cmd = 'kubectl get namespaces -o=jsonpath=\'{range.items[*]}{.metadata.name}{"\\n"}{end}\''
    o = subprocess.run(shlex.split(get_ns_cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # print(o.stdout) # Returning extra empty line at the end
    global all_nss
    all_nss = o.stdout.split("\n");
    # print(all_nss)

def save_resource_snap_per_ns(res_name):
    for ns in all_nss:
        if ns == '': return
        cmd = 'kubectl get ' + res_name + ' -n ' + ns + kubectl_global_options
        file = dirName + '/' + res_name + '.' + ns + '.txt'
        # print(cmd, file)
        log_cmd_output(cmd, file)

def save_resource_snap(res_name, ns='False'):
    cmd = 'kubectl get ' + res_name + kubectl_global_options
    file = dirName + '/' + res_name + '.txt'
    log_cmd_output(cmd, file)

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
    # print(apires_wo_ns)

def log_api_resources_wo_namespace_scope():
    for r in apires_wo_ns:
        if r != '': save_resource_snap(r)

def log_api_resources_w_namespace_scope():
    for r in apires_w_ns:
        if r != '': save_resource_snap_per_ns(r)

print('Starting snapshot')
create_dir();
list_namespaces()
print('Taking snap of configs'); config_snap(dirName)

print('Taking snap of non namespaced resources')
api_resources_wo_namespace_scope(); log_api_resources_wo_namespace_scope()

print('Taking snap of namespaced resources')
api_resources_w_namespace_scope(); log_api_resources_w_namespace_scope()

print('Snapshot stored in ' + dirName)

