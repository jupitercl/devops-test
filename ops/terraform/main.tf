resource "kubernetes_namespace" "minikube-namespace-talana" {
  metadata {
        name = "talana-namespace"
  }
}
