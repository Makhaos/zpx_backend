ZPX back-end code test
========================================
The following instructions are to be used in a Linux machine.

Docker
----------------------
### Installation
For reference:    
https://docs.docker.com/install/linux/docker-ce/ubuntu/     
https://docs.docker.com/install/linux/linux-postinstall/    

`sudo apt-get update`      
`sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common`     
`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`      
`sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"`    
`sudo apt-get update`      
`sudo apt-get install docker-ce docker-ce-cli containerd.io`      
`sudo groupadd docker`     
`sudo usermod -aG docker $USER`     
Reboot the machine

### Dockerize
In the terminal go to the project folder.    
`cd ~/.../zpx_backend-master`    
Create a **docker image** named zpx with tag:local:     
`docker build -t zpx:local .`

To run as a stand-alone docker container:    
`docker run -d -p 5000:5000 zpx:local`

Open browser at `localhost:5000/zpx/ui` to access **Swagger**.

Kubernetes
----------------------
### Install kubectl
`sudo apt-get update && sudo apt-get install -y apt-transport-https`    
`curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -`      
`echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list`    
`sudo apt-get update`      
`sudo apt-get install -y kubectl`   

Minikube
----------------------
### If you don't own a **Kubernetes cluster**, install Minikube:
`curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube && sudo install minikube /usr/local/bin/`
  
### Start the Cluster
**If** already running Minikube from inside a Virtual Machine, skip the creation of an additional VM layer by using the 'none' driver:     
`sudo minikube start --vm-driver=none`

**If not**:     
Install **VirtualBox** 5.2 or higher: https://www.virtualbox.org/wiki/Downloads     
And run:    
`sudo minikube start --vm-driver=virtualbox`     

Deployment
----------------------
Apply a predefined configuration in the cluster:      
`sudo kubectl apply -f zpx-deployment.yml`

Open browser at `localhost:30000/zpx/ui` to access **Swagger**.
