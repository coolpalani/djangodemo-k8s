# Django Kubernetes Demo

This demo was created on Minikube.  It's a basic DRF API that allows you to run CRUD functions on quotes.  

## Getting Started
Clone this repo.  I haven't pushed the Django image up to Docker Cloud yet, you'll have to build it locally before running the Kube configs.  

1) Clone: `git clone https://github.com/jayps/djangodemo-k8s.git`  
2) Build djangodemo: `docker build -t djangodemo:v2.5 .`  
3) Create deployment for djangodemo app: `kubectl create -f djangodemo-deployment.yaml`  
4) Create service for djangodemo app: `kubectl create -f djangodemo-service.yaml`  
5) Create deployment for djangodemo db: `kubectl create -f djangodemo-db-deployment.yaml`  
6) Create service for djangodemo db: `kubectl create -f djangodemo-db-service.yaml`  

If you're running Minikube, you can then run `minikube service djangodemo-service` to open the service in your browser.  No authentication is required.  

### Viewing what you've done
Run `kubectl get pods` to view pods for what is running.  Similarly, run `kubectl get services` to see what services are actively running (what's exposed).  

### Basic API
You can go to `http://serviceurl/quotes` to view quotes.  On that page, you'll find a form that lets you POST new quotes as well.  

## TODO
I still need to properly expose the djangodemo-service service so that it can be accessed via something like http://localhost/ or http://yoururl.