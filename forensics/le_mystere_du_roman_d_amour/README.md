> # Facile - Le Mystère du roman d'amour
>
> En train de faire les cent pas dans un couloir du café se trouve Joseph Rouletabille. Il est préoccupé par un mystère des plus intrigants : une de ses amies, qui écrit régulièrement des livres passionnants, a perdu le contenu de son dernier roman !! Elle a voulu ouvrir son oeuvre et son éditeur a crashé... Il semblerait qu'un petit malin a voulu lui faire une blague et a modifié ses fichiers. Elle n'a pu retrouver qu'un seul fichier étrange, que Joseph vous demande de l'aider à l'analyser afin de retrouver son précieux contenu et de comprendre ce qu'il s'est passé.
>
> Vous devez retrouver :
>
> - le PID du processus crashé
> - le chemin complet vers le fichier en question (espaces autorisés) : la forme exacte trouvée dans le challenge et la forme étendue commençant par un / permettent toutes les deux de valider le challenge
> - le nom de l'amie de Rouletabille
> - le nom de la machine
> - le contenu TEXTUEL du brouillon de son livre (si vous avez autre chose que du texte, continuez à chercher : vous devez trouver un contenu texte qui ressemble clairement au début d'un roman). Une fois ce contenu trouvé, il sera clairement indiqué quelle partie utiliser pour soumettre le flag (il s'agira d'une chaîne de caractères en leet)
>
> Le flag est la suite de ces éléments mis bout à bout, et séparés par un tiret du 6 (-), le tout enveloppé par 404CTF{...}.
>
> **Format :** 404CTF{PidDuProcessusCrashé-chemin/vers le/fichier-nomUser-nomDeLaMachine-contenuDuFichier} 
>
> **Un exemple de flag valide :** 404CTF{1234-/ceci/est/un/Chemin avec/ des espaces1337/fichier.ext-gertrude-monPcPerso-W0w_Tr0P_1337_C3_T3xt3}
>
> **Auteur :** mh4ckt3mh4ckt1c4s#0705

1. It's a vi swap file ! with the **file** command we have most of the info we need :

```
file fichier-etrange.swp
```

2. Then we can recover the file :

```
vi -r fichier-etrange.swp
```

3. It's a png ! (we see that with the magic number)

![png recovered](./toto.png)

4. We put the png in **aperisolve** and we get a QR code

![png aperisolve, qr](./image_b_1.png)

5. Use a phone to scan (I don't know why online tools wasn't able to decode it)

6. We get the final flag : 404CTF{168-/home/jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt-jaqueline-aime_ecrire-3n_V01L4_Un_Dr0l3_D3_R0m4N}
