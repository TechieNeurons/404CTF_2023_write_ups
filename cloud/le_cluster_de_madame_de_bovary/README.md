 - Facile -
Le Cluster de Madame Bovary
980

Un individu dans un coin vous interpelle et vous invite à sa table. Une fois assis, il vous explique qu'il veut que vous infiltriez le cluster Kubernetes de Madame Bovary. Madame Bovary est une femme riche et influente qui a investi dans la technologie Kubernetes pour gérer les applications de son entreprise de production de médicaments. Vous vous doutez qu'il s'agit sans doute d'un concurrent industriel mais il vous offre une belle récompense si vous réalisez sa demande.

 

Votre mission consiste à prendre le contrôle du cluster Kubernetes de Madame Bovary et à accéder à ses applications critiques. Vous devrez exploiter toutes les vulnérabilités possibles pour atteindre votre objectif.

 

 

Le fichier fourni est une machine virtuelle à charger dans Virtualbox. Cette machine virtuelle contient le cluster Kubernetes du challenge.

    Utilisateur : ctf

    Mot de passe : 404ctf2023

Typhlos#9037

1. kubectl get pods --> just one pod named agent
kubectl logs agent --> Say we need to deploy the pod 404ctf/the-container
kubectl create deployment <premiercontainer> --image=404ctf/the-container
kubectl logs <PremierContainer> --> We need to be in the correct namespace
kubectl create namespace 404ctf
Redeploy with the option --namespace=404ctf
Enter the pod : kubectl exec -it <deuxiemecontainer> -- bash
strings /opt/the-container | grep -C 20 404CTF{
	404CTF{A_la_decouv le reste du flag est dans le container 404ctf/web-server

kubectl create deployment <premierweb> --image=404ctf/web-server
Lets visit the web site, to find the ip of the pod : kubectl describe pod --namespace=404ctf and in the log a message say the port 8080 is open
Go ont the port 8080 of the IP of the pod we get the message 'the flag is in /flag' go to /flag (the web)
we get : erte_de_k8s}

404CTF{A_la_decouverte_de_k8s}
