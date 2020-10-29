`docker-compose up`

`curl localhost:8000`

## Requirements

- minikube
- kubeclt
- helm charts
- terraform

## SimpleStep

`minikube start`

`cd $HOME_REPO/ops/terraform`

`terraform init`

`terraform apply -auto-approve`

`cd $HOME_REPO/opt/k8s`

`helm create charts`

`helm install values.yml charts`

`kubectl apply -k ./`


