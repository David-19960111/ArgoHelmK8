# Desafio Nº9

- En este desafío nos encontraremos una mezcla de otros desafíos (CICD y Kubernetes), en este caso utilizaremos herramientas de Gitops para automatizar cambios en nuestro deployments y en cualquier otro archivo yaml que configuremos, de esta forma será solo cuestión de hacer los cambios en el código .yaml y dejar que la herramienta que hayamos elegido se encargue de aplicar nuestros cambios (ya sea de forma manual o automática).

## Primer paso

## 1 - Creacion de archivo Dockerfile

## 2 - Construir la imagen de Docker
  
  - Proporciona el comando para construir la imagen Docker. Asegúrate de incluir detalles como el nombre de la imagen y la ubicación del archivo Dockerfile.

```bash
docker build -t nombre-de-la-imagen -f ruta/al/Dockerfile .
```

## 3 - Publicacion en Docker Hub

  - Iniciar Sesión en Docker Hub: Si no has iniciado sesión en Docker Hub, proporciona el comando para hacerlo.

```bash
docker login
```

- Etiquetar la Imagen para Docker Hub: Etiqueta la imagen con el nombre de usuario de Docker Hub y el repositorio.

```bash
docker tag nombre-de-la-imagen nombre-de-usuario/nombre-del-repositorio:etiqueta
```

- Subir la Imagen a Docker Hub: Sube la imagen etiquetada a Docker Hub.

```bash
docker push nombre-de-usuario/nombre-del-repositorio:etiqueta
```
## 4 - Minikube

Asegúrate de que Minikube esté en funcionamiento. Si aún no has iniciado Minikube, puedes hacerlo con el comando:

```bash
minikube start
```

## 5 - Helm

- Crear repositorio de proyecto

```bash
helm create project-helm-argocd
```

- Creacion de namespace de Kubernetes

```bash
kubectl create namespace python-app
```

- Instalar repositorio de proyecto

```bash
helm install k8s github/project-helm-argocd -n python-app  
```

- Revision de instalacion

```bash
helm repo list -n python-app
```

## 6 - ArgoCD

- Crear repositorio de argocd

```bash
helm repo add argo https://argoproj.github.io/argo-helm
```

- Instalamos el repositorio

```bash
helm install argocd argo/argo-cd -n argocd
```

- Revision de Instalacion

```bash
helm repo list -n agrocd
```

- Port-forward

```bash
kubectl port-forward svc/argocd-server -n argo-cd 8080:443
```
Aplica el archivo de manifiesto YAML que describe la configuración de tu aplicación en Kubernetes. Supongamos que el archivo se llama mi-aplicacion.yaml y se encuentra en el directorio actual. Utiliza el siguiente comando:

```bash
kubectl apply -f mi-aplicacion.yaml
```
- Esto creará los recursos (pods, servicios, etc.) especificados en el archivo YAML en el clúster de Minikube.

Verifica el estado del despliegue. Puedes comprobar que los recursos se hayan desplegado correctamente utilizando comandos como kubectl get pods, kubectl get services, y otros comandos de kubectl según corresponda.

## Acceso al Panel de Control de Minikube

1 - Inicia el Dashboard: Ejecuta el siguiente comando para iniciar el panel de control de Minikube:

```bash
minikube dashboard
```

Esto abrirá una ventana del navegador web con la interfaz gráfica del panel de control.

2 - Accede al Panel de Control en tu Navegador: La URL del panel de control se mostrará en la terminal. Puedes abrirla en tu navegador web para acceder a la interfaz gráfica. Por lo general, la URL es algo como http://127.0.0.1:XXXXX.

3 - Explora y Administra el Clúster: A través del panel de control, puedes explorar los pods, servicios, despliegues y otros recursos en tu clúster de Minikube. También puedes realizar tareas de administración, como la escalabilidad de aplicaciones, la visualización de registros y más.





