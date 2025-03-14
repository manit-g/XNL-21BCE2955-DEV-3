terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
  
  backend "s3" {
    bucket = "xnl-terraform-state"
    key    = "multi-cloud/terraform.tfstate"
    region = "us-west-2"
  }
}

# AWS Configuration
provider "aws" {
  region = var.aws_region
}

# GCP Configuration
provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

# Azure Configuration
provider "azurerm" {
  features {}
  subscription_id = var.azure_subscription_id
}

# Create VPC/VNet networking for each cloud
module "aws_network" {
  source = "./aws/network"
  # ... network configuration
}

module "gcp_network" {
  source = "./gcp/network"
  # ... network configuration
}

module "azure_network" {
  source = "./azure/network"
  # ... network configuration
} 