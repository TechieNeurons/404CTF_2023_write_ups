> # Moyen - Les Mystères du cluster de la Comtesse de Ségur [2/2]
> Ce challenge est la suite du premier, qui se trouve dans la catégorie Analyse Forensique
>
> Après vos premières découvertes, vous faites votre rapport à Madame Bovary. Vous lui expliquez que quelqu'un a réussi à lui voler ses derniers livres grâce à une faille dans son application. Madame Bovary vous demande alors de trouver où ont été exfiltrées ses livres et de vous infiltrer sur ce serveur.
>
> Toutes les informations nécessaires sont présentes dans le fichier initial.
> Auteur : Typhlos#9037

1. Open with IDA we can see (in the **main_main**) 
 - the program must be run in **kubernetes** 
 - after that he open the **flag.txt**
 - After the binary send something to a C2 server (**c2.challenges.404ctf.fr**)
2. Install **minikube** (and **kubectl**)
3. Create a yaml file for creating a new Ubuntu pods :

```
# Launch minikube :
minikube start

# In the yaml file :
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu
  labels:
    app: ubuntu
spec:
  containers:
  - name: ubuntu
    image: ubuntu:latest
    command: ["/bin/sleep", "3650d"]
    imagePullPolicy: IfNotPresent
  restartPolicy: Always

# Create the pod :
kubectl -f ubuntu.yml
```

4. Enter the pod :

```
kubectl exec --stdin --tty ubuntu -- /bin/bash
```

5. I put the binary file in a public github repo and **wget** it after doing a **apt update && apt install wget** (one way to get the file in the pod, probably not the best one)

6. Execute the script and get the flag :

```
root@ubuntu:~# ./agent  
404CTF{K8S_checkpoints_utile_pour_le_forensic}
404CTF{command_&_~~conquer~~_control}
```