ZPX back-end code test

docker build -t zpx_image .

Local Kubernetes cluster:
Virtual machine running Ubuntu:
snap install kubectl --classic

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
   && sudo install minikube-linux-amd64 /usr/local/bin/minikube
sudo minikube start --vm-driver=none

Windows:
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.17.0/bin/windows/amd64/kubectl.exe
Add the binary in to your PATH.

Run the installer:
https://storage.googleapis.com/minikube/releases/latest/minikube-installer.exe
Install virtualbox 5.2 or higher:
minikube start --vm-driver=virtualbox


kubectl apply -f zpx-deployment.yml

Open browser at localhost:30000/zpx/ui to access Swagger

