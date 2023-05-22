 - Facile -
Les OSINTables [1/3]
693

En pleine discussion au Procope, Cosette vous raconte autour d'une part de fraisier la première fois qu'elle a essayé d'envoyer une lettre à son bienfaiteur : Jean Valjean.

 
Débutante dans la démarche postale, elle s'est trompée sur les informations nécessaires, elle en a même oublié l'adresse du destinataire, n'écrivant que la sienne. Elle vous montre la photo ci-jointe et vous met au défi de trouver d'où elle l'a écrite.

 

 

Trouvez l'adresse d'envoi de la lettre (celle de Cosette).

 

    Format : 404CTF{numero_adresse_rue_ville}

exemple : 404CTF{36_quai_des_orfevres_paris}

 

Contact en cas de problème : Racoon#8487
Neptales

1. The LXXXIII seems to be roman number after a quick convertion it give us 83
2. The stree is written in full : rue victor hugo
3. The line after the stree must be the city, so the city begin with VE
4. On google maps search for the "83 rue victor hugo ve", two city appear Vergèze and Versailles

the flag is : 404CTF{83_rue_victor_hugo_vergeze}
