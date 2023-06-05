> # Harpagon et le magot
>
> Un homme en habits de laquais fait les cents pas, seul au fond du café. Vous vous en approchez par curiosité.
>
> La Flèche
>
> Brisant le quatrième mur
>
> Hé quoi ! Ce coquin d'Harpagon ne se lassera donc jamais d’importuner les jeunes gens ! Voilà donc maintenant qu'il va jusqu'à louer des serveurs pour mettre ses écus à l’abri, alors même qu'il refuse à ses propres enfants la moindre dot. Son fils, mon maître, est désespéré de ne pouvoir prétendre à sa bien-aimée Mariane, que son père tente de lui ravir. Sa fille Élise n'est pas mieux traitée, la voilà promise à un ancêtre. Ha non vraiment, je ne puis me résoudre à les abandonner ! Sachez que j'ai donc mené mon enquête, et je pense avoir trouvé de quoi déstabiliser le coquin. Je ne crois pas qu'il ait jamais réussi à faire marcher sa machine comme il le souhaitait, mais elle dois néanmoins contenir toutes sortes de choses qui pourraient faire avancer notre affaire. Accepteriez-vous de m'apporter votre concours pour dévoiler les secrets du vieil avare afin que nos chers amis puissent plus aisément le raisonner ?
>
>Connectez vous au VPS d'Harpagon, investiguez ce qu'il y a fait et retrouvez son secret.
>
>Attention, les services peuvent mettre un peu de temps à démarrer. Harpagon n'est pas très doué et n'a jamais réussi à utiliser sa cassette
>
> Mot de passe : T8h2UKEstg
>
> Auteur : Smyler#7078

1. After connecting we can note multiple thing, first we have some kubernetes and Harpagon used **helm** to admin his kube, let's list the kube :

```
$ helm list
NAME    	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART            	APP VERSION
cassette	cassette 	2       	2023-05-13 17:59:56.996583917 +0000 UTC	deployed	vaultwarden-0.8.0	1.24.0     
```

2. We have one kube named **cassette** and he have two "revision" / two version, list the different versions :

```
$ helm history cassette
REVISION	UPDATED                 	STATUS    	CHART            	APP VERSION	DESCRIPTION     
1       	Sat May 13 17:58:09 2023	superseded	vaultwarden-0.8.0	1.24.0     	Install complete
2       	Sat May 13 17:59:56 2023	deployed  	vaultwarden-0.8.0	1.24.0     	Upgrade complete
```

3. If we open the file value.yaml in the harpagon folder we can see a mesage (on the line "admin-key") which say : "My secret is not here anymore, we'll rollback to the first version (the one not in production) to get back the first used secret :

```
$ helm rollback cassette 1
Rollback was a success! Happy Helming!

$ helm history cassette
REVISION	UPDATED                 	STATUS    	CHART            	APP VERSION	DESCRIPTION     
1       	Sat May 13 17:58:09 2023	superseded	vaultwarden-0.8.0	1.24.0     	Install complete
2       	Sat May 13 17:59:56 2023	superseded	vaultwarden-0.8.0	1.24.0     	Upgrade complete
3       	Sat May 20 12:30:52 2023	deployed  	vaultwarden-0.8.0	1.24.0     	Rollback to 1   
```

4. After the rollback we connect to the service :

```
$ kubectl exec -it cassette-vaultwarden-0 -- bash
```

5. The admin key is stored as a local variable :

```
# env
ADMIN_TOKEN=}em1tciv_7s3_l1_7n0d_u@3lf_1_7s3_3c1r4v@l{FTC404
```