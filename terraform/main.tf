provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_artifact_registry_repository" "llm_repo" {
  name     = "llm-backend"
  format   = "DOCKER"
  location = var.region
}

resource "google_vertex_ai_endpoint" "llm_endpoint" {
  display_name = "llm-faq-endpoint"
  region       = var.region
}

# terraform/variables.tf
variable "project_id" {}
variable "region" {
  default = "us-central1"
}