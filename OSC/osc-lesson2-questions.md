# Course Questions - Lecture 2
**Chapter 1**
* What are containers?
Containers are a way to package and isolate applications and their dependencies into a single, self-contained unit that can be easily moved from one environment to another. They allow you to run applications in a consistent and predictable manner, regardless of the environment in which they are deployed.
* Why would anyone use containers? Aka. what is the prime goal/function of containers?
Containers use lightweight, isolated environments to run applications, which makes them more efficient and portable than traditional virtualization techniques. They are built on top of the host operating system, sharing the underlying kernel and resources, but each container has its own filesystem and process space, so applications running in different containers do not interfere with each other. This makes it easy to run multiple applications on the same host without worrying about conflicts or resource contention.
* What is the difference between a container and a virtual machine?
Containers and virtual machines are both technologies that can be used to run applications in isolated environments, but they work in different ways.
Virtual machines (VMs) are a type of software that allows you to run an entire operating system within another operating system. Each VM runs on top of a host operating system, and includes its own operating system, resources, and applications. This allows you to run multiple operating systems on the same physical hardware, and to run applications that are not compatible with the host operating system.
Containers, on the other hand, are a way to package and isolate applications and their dependencies into a single, self-contained unit that can be easily moved from one environment to another. They use lightweight, isolated environments to run applications, which makes them more efficient and portable than traditional virtualization techniques. Containers share the underlying kernel and resources of the host operating system, but each container has its own filesystem and process space, so applications running in different containers do not interfere with each other.
In summary, the main difference between containers and virtual machines is that containers share the host operating system and resources, while virtual machines include their own operating system and resources. This makes containers more lightweight and efficient, but also means that they are not as isolated as virtual machines, and may be more vulnerable to security breaches.
* Why are the terms "container" and "docker" not synonyms?
Docker is one of the most widely used containerization platforms, but it is not the only one. Other popular containerization platforms include Kubernetes, Apache Mesos, and LXC (Linux Containers).
In summary, the term "container" refers to the concept of containerization, while "Docker" refers specifically to the Docker containerization platform.
* List 2 other technologies to run a "container" without using "docker".
Kubernetes: Kubernetes is an open-source container orchestration platform that allows you to deploy, scale, and manage containerized applications. It provides a set of tools and services for building, distributing, and running containerized applications, including the kubelet, which is a runtime environment for building and running containers, and the kube-apiserver, which is a central component of the Kubernetes control plane that exposes the API for interacting with the cluster.
LXC (Linux Containers): LXC is an open-source containerization platform that allows you to run multiple isolated Linux systems on a single host. It uses Linux kernel namespaces and cgroups to create lightweight, isolated environments for running applications, and provides a set of tools and libraries for building and managing containerized applications.
Both Kubernetes and LXC are popular alternatives to Docker for running containerized applications, and offer a wide range of features and capabilities for building, deploying, and managing containerized applications at scale.
* Is it possible to run the very same type of Docker container both on Linux and on Windows? Why or why not? How do Windows 10 and Windows 11 work around this?
Docker containers are designed to be portable and can be run on any platform that supports the Docker runtime, regardless of the host operating system.
But it depends on the kind of container you are running. In general it should be possible but if it is an application that relies on Linux-specific libraries or tools it may not be able to run on Windows.
* What is the difference between the Docker client (utilities) and the Docker server (~daemon)?
the Docker client is a command-line interface that allows you to interact with the Docker daemon, while the Docker daemon is a background process that runs on the host operating system and is responsible for building and running Docker containers.
* What is a Dockerfile, image and registry?
In summary, a Docker file is a text file that contains instructions for building a Docker image, a Docker image is a standalone, executable package that includes everything needed to run an application, and a Docker registry is a storage location for Docker images. These three concepts work together to build and deploy Docker containers.
## What do the following docker commands do?
* docker ps
List all running containers
* docker images
List downloaded images
* docker run -d <imagename>
Start a container based on the image (and pull it automatically if necessary) 
* docker exec -it <imagename> sh
The Answer
* docker compose up
The Answer
* docker stop <containerid>
The Answer
* docker rm <containerid>
The Answer
## What is the workflow (--> you should be able to do this yourself!) to properly deploy/ship/package an application:
1. Create an application that prints "hello world" in a programming language.
1. Create a Dockerfile for this application
1. Build a Docker image from this Dockerfile
1. Create and run a Docker container from this Docker image
1. Interact with the container by entering (and gaining access with for example a shell) to the running Docker container
1. Stop and remove the Docker container.
