variable "project_name" {
  description = "Project name for resource tagging"
  default     = "XNL-21BCE2955-DEV-3"
}

variable "aws_region" {
  description = "AWS region"
  default     = "us-west-2"
}

variable "gcp_project_id" {
  description = "GCP project ID"
  default     = "xnl-21bce2955-dev3"
}

variable "gcp_region" {
  description = "GCP region"
  default     = "us-central1"
}

variable "azure_subscription_id" {
  description = "Azure subscription ID"
  type        = string
}

variable "environment" {
  description = "Environment (dev/staging/prod)"
  default     = "dev"
} 