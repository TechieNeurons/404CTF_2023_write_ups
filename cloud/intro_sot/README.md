> # Introduction - Le Sot
>
> Dans un coin reculé du café est assis Panurge, la mine sombre. Prenant pitié, vous vous donnez pour mission de lui remonter le moral.
>
> « Que diable vous prend-il aujourd'hui ? Il me semblerait rencontrer le désepoir en personne.
>
> — Mes moutons se sont échappés. L'un deux a pris la fuite, et les autres l'ont suivi.
> 
> — Comment ? Mais où donc sont-ils allés ?
>
> — Ils sont partis dans les nuages... »
>
> Allons, vous avez bon coeur n'est-ce pas ? Allez donc lui retrouver ses moutons.
>
> Endpoint S3 : https://s3.gra.io.cloud.ovh.net/
>
> Bucket : cloud-intro-challenge
> Attention, il s'agit d'une vrai infrastructure cloud, le brute-force est particulièrement proscrit

1. I'm discovering how to cloud works, so I make some research about accessing the endpoint, I find : https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteEndpoints.html

2. Let's try to access the endpoint to see what he got :

```
$ curl https://cloud-intro-challenge.s3.gra.io.cloud.ovh.net

<?xml version='1.0' encoding='UTF-8'?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Name>cloud-intro-challenge</Name><Prefix/><Marker/><MaxKeys>1000</MaxKeys><IsTruncated>false</IsTruncated><Contents><Key>les-moutons.json</Key><LastModified>2023-05-12T13:56:48.000Z</LastModified><ETag>"d642390a5d6f695d958015801e585cb1"</ETag><Size>1767</Size><Owner><ID/><DisplayName/></Owner><StorageClass>STANDARD</StorageClass></Contents></ListBucketResult>
```                                     

2. We notice one ressource **les-moutons.json**, let's access it :

```
$ curl https://cloud-intro-challenge.s3.gra.io.cloud.ovh.net/les-moutons.json
{
    "sheeps": [...],
    "flag": "404CTF{D35_m0utOns_D4n5_13s_NU@g3s}"
}
```