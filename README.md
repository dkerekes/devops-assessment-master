# Dokumentation

## Changes

### Helm Chart "deployment.yaml" template

- Created a helper file to make `nameOverride` easier to use.
- Included labels for all components.
- `spec.replicas`: Made it configurable from **values.yaml**.
- `spec.template.spec.imagePullSecrets`: Included an option to support private image registries.
- `spec.template.spec.containers[0].ports[0].name`: Missing port name. Including one makes it easier to reference this port in a Service, for example.
- `spec.template.spec.containers[0].ports[0].protocol`: Missing protocol type. The default is TCP, so explicitly defining it is only a best practice for better readability.

### Helm Chart "service.yaml" template

- Wrapped the entire **service.yaml** template in an **if** statement so its deployment can be controlled from the **values.yaml** file.
- Included a label.
- `spec.type`: Missing type. The default is **ClusterIP**, so this is not necessarily an error.
- `spec.selector.app`: The pods have the label "myapp", but the Service selector points to "myapps". The Service would not match the pods and would not record their IP addresses in the generated EndpointSlice.
- `spec.ports[0].targetPort`: Misconfigured port number. The container is listening on port **5000**, but the Service's `targetPort` is set to **8080**. Using a port name instead of a port number would also be preferable, as it makes such misconfigurations less likely.
- `spec.ports[0].name`: Missing port name. The same logic applies as with naming Pod ports, but from the perspective of Ingresses.
- `spec.ports[0].protocol`: Missing protocol type. The same argument applies as with the Deployment's port protocol.

### Helm Chart "ingress.yaml" template

- As with the Service, the Ingress also received an **if** statement to enable or disable it. Extracted some values into **_helpers.tpl** and **values.yaml**.
- Included a label.
- `spec.ingressClassName`: Missing, but not necessarily an error. The default IngressClass should still recognize and handle the Ingress.
- `spec.rules[0].http.paths[0].backend.service.name`: Points to the wrong Service.
- `spec.rules[0].http.paths[0].backend.service.port.number`: The number is correct, but as in previous cases, a port name is preferable.

### Terraform

- `resource.kubernetes_namespace.homework.metadata.name`: Replaced the static value with a variable.
- `resource.helm_release.homework.chart`: Fixed the chart path.
- `resource.helm_release.homework.set`: Fixed the Helm values override syntax.
- Created a Terraform output containing some metadata.
- `provider.helm.kubernetes`: Fixed a syntax error.

## Assumptions

I'm assuming that this application should be built whenever someone updates the application code and pushes a commit to GitLab.  
The pipeline should not automatically deploy the new application version after the build is complete. This could be changed if the target environment is not production.

## Limitations

- The application has no real storage backend. It only stores information in memory using a Python dictionary.
- The Dockerfile, Helm chart, and Terraform configuration work in local testing using Podman and a Kind cluster, but the GitLab pipeline has not been tested.
- In its current form, the pipeline does not provide a kubeconfig to the Terraform configuration.

## Improvements

- Make Deployment, Pod, Service, and Ingress labels and selectors configurable through **values.yaml**.
- The Helm chart could include many more features regarding security and reliability.
- GitLab pipeline versioning needs to be reworked if one wants to use a "major.minor.patch" image tagging scheme.
- There should be a couple of additional testing stages, such as unit testing and image vulnerability scanning.
- I would argue that using Terraform to deploy resources to Kubernetes is not wrong by any means, but speaking from personal experience, an ArgoCD Application approach could provide some flexibility that Terraform cannot offer for this specific task.
