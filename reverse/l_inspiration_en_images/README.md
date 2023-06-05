# Facile - L'Inspiration en images
>
> Un quart d'heure plus tôt dans la soirée, vous étiez en train de parler avec Sabine de vos méthodes créatives, de vos exercices de style dans vos mediums respectifs. Elle mentionna au fil de la conversation son atelier de peinture se situant dans les combles rustiques du café littéraire, vous suggérant que vous pourriez toujours prendre de l'inspiration en observant ses peintures, son processus de création, sa manière de capturer la beauté insaisissable.
>
> Une fois la conversation et le café terminés, vous vous aventurez dans l'atelier de peinture de Sabine, votre lampe torche à la main. Au milieu de cette mer de tableaux, vous repérez une peinture étrange, criblée d'inscriptions.
>
> Et au pied du chevalet a chu une note, sur laquelle il est marqué : 'Ma clé est la couleur du fond de la toile'. Vous remarquez également d'autres inscriptions incompréhensibles au verso de la note. Sans doute un message chiffré ?
>
> Vous vous mettez en quête de la clé.
>
> Note : Le déchiffrage du message n'est pas nécessaire à la complétion du challenge.
>
> **Format :** 404CTF{vec4(r,g,b,a)} où r,g,b et a sont des flottants précis au dixième.

1. Open the binary in ghidra, The following line seems interesting :

```
(*glad_glClearColor)(0x3e4ccccd,0x3e99999a,0x3e99999a,0x3f800000);
```

2. After some research : https://registry.khronos.org/OpenGL-Refpages/gl4/html/glClearColor.xhtml

3. Transform the hex value to float : https://gregstoll.com/~gregstoll/floattohex/

4. We get :
- 0x3e4ccccd -> 0.2
- 0x3e99999a -> 0.3
- 0x3e99999a -> 0.3
- 0x3f800000 -> 1

5. So the flag is : 404CTF{vec4(0.2,0.3,0.3,1.0)}
