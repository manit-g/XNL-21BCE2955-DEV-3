#!/bin/bash

# Set variables
export PROJECT_NAME="XNL-21BCE2955-DEV-3"
export OWNER="Manit Gera"

# Initialize Terraform
cd terraform
terraform init
terraform apply -auto-approve

# Deploy Kubernetes resources
kubectl apply -f kubernetes/base/monitoring/
kubectl apply -f kubernetes/base/blockchain/
kubectl apply -f kubernetes/base/ml-system/
kubectl apply -f kubernetes/base/networking/
kubectl apply -f kubernetes/base/testing/

# Deploy smart contracts
cd ../blockchain
truffle migrate --network testnet

# Start monitoring
kubectl port-forward svc/grafana 3000:3000 -n monitoring &
kubectl port-forward svc/prometheus 9090:9090 -n monitoring &

echo "Deployment complete! System is ready for testing." 