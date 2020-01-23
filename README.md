ZPX back-end code test
========================================
The following instructions are to be used in a Linux machine.

Docker
----------------------
In the terminal go to zpx project folder.    
Create a **docker image** named zpx with tag:local:     
`docker build -t zpx:local .`

kubectl
----------------------
Install kubectl to work with **Kubernetes**.     
For Ubuntu: `snap install kubectl --classic`    
For other dist: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux

Minikube
----------------------
If you don't own a **Kubernetes cluster**, install Minikube:    
`curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
   && sudo install minikube-linux-amd64 /usr/local/bin/minikube`

Install **VirtualBox** 5.2 or higher: https://www.virtualbox.org/wiki/Downloads   
Start the Cluster:        
`sudo minikube start --vm-driver=virtualbox`     
Or if already running Minikube from inside a Virtual Machine, skip the creation of an additional VM layer by using the none driver:     
`sudo minikube start --vm-driver=none`

Deployment
----------------------
Apply a predefined configuration in the cluster:      
`sudo kubectl apply -f zpx-deployment.yml`

Open browser at `localhost:30000/zpx/ui` to access **Swagger**.
