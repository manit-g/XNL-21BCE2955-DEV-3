resource "google_compute_network" "vpc" {
  name                    = "${var.project_name}-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "${var.project_name}-subnet"
  ip_cidr_range = "10.2.0.0/16"
  network       = google_compute_network.vpc.name
  region        = var.gcp_region

  secondary_ip_range {
    range_name    = "k8s-pods"
    ip_cidr_range = "10.3.0.0/16"
  }
} 