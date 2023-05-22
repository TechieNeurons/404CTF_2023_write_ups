 - Difficile -
Note de bas de page
999

En tendant l'oreille dans le salon, votre attention est captée par une conversation particulière. Là où les alentours dissertent sur des sujets de procédés littéraires toujours plus avancés, celle-ci semble en effet plutôt porter sur la philosophie naturelle. Vous vous approchez par curiosité, lorsque la marquise du Châtelet, alors en pleine explication des travaux d'un certain Leibniz, s’interrompt et vous interpelle :

« Vous me voyez ravie de vous rencontrer ici ! Nous n'avons pas eu la chance de nous rencontrer, mais on m'a parlé de vous et l'on m'a assuré que vous étiez formidable lorsqu'il s’agissait de retrouver les choses perdues. Voyez, j'ai travaillé il y a peu sur un projet qui me tient à cœur, et j'ai bien peur d'avoir perdu le fruit de mon travail par un triste accident. Heureusement, j'avais échangé à ce sujet avec un ami proche, et il est bien possible que notre correspondance ait gardé la trace d'une note de bas de page que je souhaiterais tout particulièrement retrouver. Auriez vous l’amabilité de m'assister dans ma mésaventure ? »

Aidez la marquise à retrouver la note qu'elle a perdue grâce à une sauvegarde de ses correspondances.
Smyler#7078

1. Install pst-utils
2. readpst -D backup.pst
3. "Boite envoyé" contain a png (can use KMAIL too)
4. In this png we can see the beginning of the flag in the bottom right corner
5. We need to use the vuln acropalypse found recently but the script doesnt work with windows screenshot...
6. 
```
python acropalypse_matching_sha256.py 2560 1080 Capture\ d’écran\ 2023-05-07\ 210840.png reconstructed.png
```

Ressources :
https://twitter.com/David3141593/status/1638222624084951040
https://www.da.vidbuchanan.co.uk/blog/
https://www.bleepingcomputer.com/news/microsoft/windows-11-snipping-tool-privacy-bug-exposes-cropped-image-content/

404CTF{L3_f0rM1d@bl3_pO9re35_d3s_lUm13re5}
