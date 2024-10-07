# Pre-req steps

## Create the VM

```bash
vagrant up
```

Once VM is created, ssh into VM

```bash
vagrant ssh
```

Once you entered into VM, do source to pull all aliases

```bash
vagrant@ubuntu-jammy:~$ source setaliases.sh 
[Mon Oct 07 13:06:47] [vagrant@ubuntu-jammy] [~]# 
```

Create K8s cluster using Kind

```bash
[Mon Oct 07 13:13:15] [vagrant@ubuntu-jammy] [/shared-with-host]# 
kind create cluster --config kind-local-k8s-cluster-baremin.yaml --name k8s-samples
Creating cluster "k8s-samples" ...
 ✓ Ensuring node image (kindest/node:v1.31.0) 🖼 
 ✓ Preparing nodes 📦 📦 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
 ✓ Joining worker nodes 🚜 
Set kubectl context to "kind-k8s-samples"
You can now use your cluster with:

kubectl cluster-info --context kind-k8s-samples
```

```bash
[Mon Oct 07 13:16:28] [vagrant@ubuntu-jammy] [/shared-with-host]# 
kubectl cluster-info --context kind-k8s-samples
Kubernetes control plane is running at https://127.0.0.1:38919
CoreDNS is running at https://127.0.0.1:38919/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

