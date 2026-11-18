resource "kubernetes_namespace" "homework" {
    metadata {
        name = var.namespace
    }
}

resource "helm_release" "homework" {
    name       = "homework"
    chart      = "${path.module}/../helm"
    namespace  = kubernetes_namespace.homework.metadata[0].name
    
    set = [
        {
            name  = "image.repository"
             # Move this static value to a variable
            value = var.image_name
        },
        {
            name  = "image.tag"
            value = var.image_tag
        },
        {
            name  = "environment"
            value = var.environment
        }
    ]
}
