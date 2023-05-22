 - Moyen -
Lettres volatiles
981

Une femme regarde avec hésitation une table à l'autre bout du café Le Procope, au milieu des conversations de fond des habitués. Sur cette table, un ordinateur allumé est laissé à l'abandon.

 

ARSINOÉ

à part

Vais-je réellement croissanter mon amie ?

Je m'en voudrais longtemps, même si c'est permis.

Cela suffit. Il est grand temps que je m'élance.

De Célimène, je vais trahir la confiance.

ARSINOÉ

prenant les commandes de la machine

Il semble que quelques intéressants fichiers

Soient protégés par quelque magie noire.

Célimène garde vraiment bien ses secrets.

Il va alors falloir capturer sa mémoire.

 

 

Arsinoé s'exécute en vitesse, et récupère le répertoire utilisateur de Célimène dans une clé. À vous d'y récupérer le secret.
MD5 C311M1N1.zip : a22df7724c02691d12ef1451fb83bf3a
OwlyDuck#4819


We get a zip with the file of a User
Nothing interesting except for the folder Documents/JumpBag it's the result of the software JumpBag which take snapshot of memory and we have a snapshot of the memory in this folder
After some search we find one interesting process, notepad, let's get the content by using VAD (dump of the heap)
With vol2 : 
```
python /opt/vol2/vol.py -f C311M1N1-PC-20230514-200525.raw --profile=Win7SP1x64 pstree | grep notepad
Volatility Foundation Volatility Framework 2.6.1
. 0xfffffa8003d3c060:notepad.exe                     4188    840      1     60 2023-05-14 20:02:09 UTC+0000
                                                                    
                                                                    
python /opt/vol2/vol.py -f C311M1N1-PC-20230514-200525.raw --profile=Win7SP1x64 vadtree -p 4188 --output=dot --output-file=../../../dump/graph.dot 
Volatility Foundation Volatility Framework 2.6.1
Outputting to: ../../../dump/graph.dot

```
We get a .dot file we can convert it with :
```
dot -Tps ../../../dump/graph.dot -o ../../../dump/outfile.ps
```

Then, with vol3 :
```
python /opt/vol3/vol.py -f C311M1N1-PC-20230514-200525.raw windows.vadinfo.VadInfo --dump --pid 4188
```

We can extract the password by using strings on the heap (red memory location on the vadtree)
```
strings -e l pid.4188.vad.0x80000-0x17ffff.dmp

Z1p p4s5wOrd : F3eMoBon8n3GD5xQ
```
In the pdf :

404CTF{V0147i1I7y_W1Ll_N3v3r_Wr8_loV3_l3ttEr5}
