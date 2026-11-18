output "deployment_info" {
  description = "Application deployment information"
  value = {
    environment = var.environment
    image_tag   = var.image_tag
    namespace   = kubernetes_namespace.homework.metadata[0].name
    release     = helm_release.homework.name
  }
}