> # Moyen - Les Mystères du cluster de la Comtesse de Ségur [1/2]
>
> Vous rencontrez la Comtesse de Ségur au Procope. La Comtesse de Ségur a créé une entreprise de vente de livres en ligne en s'aidant du succès de ses livres pour enfants et l'a déployé sur un cluster Kubernetes.
>
> Celle-ci vous explique avoir été victime d'une demande de rançon. En effet, quelqu'un lui a volé ses livres pas encore publiés et menace de les publier sur Internet si elle ne lui paye la rançon demandée.
>
> La Comtesse vous demande d'enquêter sur la manière dont le maître chanteur a pu voler ses livres et vous donne pour cela les informations à sa disposition.
>
> Votre mission consiste à exploiter le fichier fourni pour y retrouver les traces du maître chanteur.
> Auteur : Typhlos#9037

1. I knew nothing about kubernetes so I made some research first, I kept 3 link which was useful for this challenge :
- https://kubernetes.io/blog/2022/12/05forensic-container-checkpointing-alpha/
- https://kubernetes.io/blog/2023/03/10/forensic-container-analysis/

2. To solve the chall, I extracted the zip, then I did a strings on every checkpoint and I filtered to find 404.

```
# sudo strings checkpoint/* | grep 404
es.404ctf.fr
404ctf.fr -o agent.zi
curl agent.challenges.404ctf.fr -o agent.zip
enges.404ctf.fr -o agent.zip
```

3. We can see the user made a curl to download a zip, let's do the same ! After extraction we get the flag (the zip is in the second part in reverse)
