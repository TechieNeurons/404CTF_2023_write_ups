 - Moyen -
Les Mystères du cluster de la Comtesse de Ségur [1/2]
975

Vous rencontrez la Comtesse de Ségur au Procope. La Comtesse de Ségur a créé une entreprise de vente de livres en ligne en s'aidant du succès de ses livres pour enfants et l'a déployé sur un cluster Kubernetes.

Celle-ci vous explique avoir été victime d'une demande de rançon. En effet, quelqu'un lui a volé ses livres pas encore publiés et menace de les publier sur Internet si elle ne lui paye la rançon demandée.

La Comtesse vous demande d'enquêter sur la manière dont le maître chanteur a pu voler ses livres et vous donne pour cela les informations à sa disposition.

Votre mission consiste à exploiter le fichier fourni pour y retrouver les traces du maître chanteur.
Typhlos#9037

Useful link : https://kubernetes.io/blog/2022/12/05/forensic-container-checkpointing-alpha/
https://kubernetes.io/blog/2023/03/10/forensic-container-analysis/

Extract the zip, then :
```
sudo strings checkpoint/* | grep 404
es.404ctf.fr
404ctf.fr -o agent.zi
curl agent.challenges.404ctf.fr -o agent.zip
enges.404ctf.fr -o agent.zip
```

Go on agent.challenges.404ctf.fr, download the zip extract and flag

