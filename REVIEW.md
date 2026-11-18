# Code Review and Suggestions

For a junior-level colleague, the given code is not a bad start. The main problem is that many things have been started, but nothing has been finished. Numerous small, easily avoidable mistakes make the code difficult to fix. A step-by-step approach could help resolve these issues.

## Suggestions

1. Write the application code. Start simple and test it in a local Python virtual environment (venv).
2. Create a simple Dockerfile and, after building the image, test the entire application again by running the container locally.
3. Do not overcomplicate the Helm chart initially. Start with just the three main Kubernetes manifests. Use the example manifests from [https://kubernetes.io/docs/](https://kubernetes.io/docs/) and the `helm template` command for debugging. Only after everything works should you start moving configuration values out of the manifests and into **values.yaml**. Add useful features last.
4. Fix the errors in the Terraform configuration and use the `terraform validate` command to verify it. Most syntax errors can be avoided by copying examples directly from the [Terraform Registry](https://registry.terraform.io/).
5. As with all previous steps, develop the pipeline incrementally. Only start working on the deployment stage once the build stage is working correctly.

## Concrete Things to Fix

1. The Kubernetes Service label selector is misconfigured.
2. The Kubernetes Service target port is also incorrect.
3. The Kubernetes Ingress should point to the Service **myapp**, not **homeworks**.
4. In the Terraform `helm_release` resource, the `chart` attribute is incorrect. Given the current project structure, it should be `../helm`, or preferably `"${path.module}/../helm"`.
5. The Terraform variable **namespace** is not used.
