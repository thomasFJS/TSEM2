# Logbook

## Jeudi 09 Décembre 2021
Je décide de tester un exemple d'utilisation de l'API Accesslink de Polar en python, le script n'arrive pas a se lancer avec une erreur dans le loader du fichier de config yaml.
Il y avait juste un problème avec la version de Pyyaml, certaine installation change sa version et elle n'était plus bonne pour le script, j'ai réinstallé pyyaml avec la version 5.4
``` python hl_lines="2 3"
pip install pyyaml==5.4.1
```
Après une discussion avec M.Aigroz sur mon sujet, nous avons parler de l'import des fichiers excel (Les programmes que les coachs pourront upload), les données seront converties en json pour être plus facilement traitable ensuite. 

[Excel to json](https://docs.microsoft.com/en-us/office/dev/scripts/resources/samples/get-table-data)


## Jeudi 16 Décembre 2021
L'API Polar étant un des éléments les plus importants pour mon application, j'aimerai essayer de faire en sorte d'avoir une application en python capable d'afficher les infos de l'utilisateur Polar lorsque le lecteur RFID scan la carte de l'utilisateur.

J'ai amené une montre Polar M400 de chez moi pour pouvoir avoir plusieurs montre pour tester l'API. Je vais prendre les 2 montres et enregistrer des données d'entrainement pendant les vacances.

L'idée pour mon travail de diplôme est d'avoir 1 seul compte Polar (Le compte de l'admin de la salle de sport) qui serait connecté à plusieurs montres dans la salle. Lorsqu'un client arrive et badge sa carte de membre (carte RFID), une montre lui est assigné pour la session d'entrainement (elle prend fin lorsque le client badge sa sortie).

## Jeudi 23 Décembre 2021

J'ai repris le projet ["CrowMagic"](https://github.com/DavidPlnmr/crowmagic) auquel j'ai participé l'année passée dans le cadre des ateliers décloisonnés. Le projet utilisait les cartes RFID et je voulais reprendre un peu l'utilisation des cartes pour mon projet. 

J'ai installé [VNC Viewer](https://www.realvnc.com/fr/connect/download/viewer/) pour utiliser le CrowPi directement sur mon PC. 

Chaque carte RFID possède un id, dans un json je définis les valeurs dont j'ai besoin qui sont associées à l'id de la carte. Problème avec l'import de RPi.GPIO, je vais regarder l'install ou si c'est un problème de version.

## Jeudi 13 Janvier 2021

La malette CrowPi ne fonctionne plus, je pense que jeudi dernier avant les vacances quelqu'un a du debranché la malette. J'ai prit la deuxième malette et j'ai reconfiguré VNC pour pouvoir avoir accès. Je créer un [Trello](https://trello.com/b/13LfbmBE/polardata) pour gérer la roadmap du projet. J'ai commencé à remplir les backlogs et j'ai défini un niveau d'importance pour les tâches. Bug avec vscode sur le CrowPi, vscode n'arrive pas à se lancer comme il faut (Affichage). J'ai commencé à créer un fichier json contenant les données des cartes RFID et le programme pour lire les infos des cartes. Lorsque le problème avec vscode sera réglé je pourrai tester le programme. L'après-midi M.Garcia m'a prêté un [lecteur NFC](https://www.acs.com.hk/en/products/3/acr122u-usb-nfc-reader/), je vais essayer de le tester d'ici jeudi prochain pour essayer de remplacer la malette CrowPi.


## Jeudi 20 Janvier 2022

Je me suis documenté sur le lecteur NFC ACR122U afin de l'utiliser avec les cartes RFID, j'ai découvert la librairie python [*pyscard*](https://pyscard.sourceforge.io/user-guide.html#the-answer-to-reset-atr) qui permet d'utiliser les lecteurs NFC. A l'aide de la documentation j'ai pu faire un petit programme qui lit la carte scannée et affiche son UID. Malheureusement, pour l'utilisation de cette libraire fonctionne sur le fait qu'une connexion doit  être établie avec une carte donc si aucune carte n'est placée à l'avance sur le lecteur le programme crashera car il n'aura aucune carte pour créer la connexion. Une fonctionnalité permet de mettre un timeout et d'attendre qu'une carte soit scannée mais un nombre de seconde doit être défini avant que le programme ne se ferme. 

Sachant qu'un nombre de seconde d'attente doit être défini, je ne pense pas que cette approche conviendrait pour mon projet. Je décide donc de repartir sur la malette CrowPi et de réinstaller une version plus récente de raspberryOS.

## Jeudi 27 Janvier 2022

J'ai discuter un peu avec M.Aigroz par rapport à mon problème avec le lecteur NFC et la connexion avec la carte. Je revois donc toute la documentation et je finis par trouver un moyen de faire fonctionner le lecteur. J'ai réussi à avoir un fichier json contenant les ids des cartes RFID et j'utilise le lecteur pour comparé les ids des cartes scannées avec les ids stockées dans le json. Il faudrait maintenant que j'arrive à intégrer un appel à l'API Polar lorsque je scanne la carte. Depuis les vacances, j'ai eu le temps d'ajouter des données d'entrainements sur les montres Polar que j'avais à disposition. Maintenant le problème avec le lecteur NFC réglé je vais commencer la partie sur l'API Polar et la récupération des données.

## Jeudi 03 Février 2022

J'ai avancé sur la documentation, j'ai ajouter la description du lecteur, la librairie pyscard ainsi que l'API Polar. J'ai commencé à regarder le fonctionnement de l'API pour essayer de récupérer les données d'entrainements quand la carte RFID est scannée. Il me semble que lorsqu'on récupère les données d'entrainements avec l'API on récupère toutes les données du compte, il faut que je regarde si il est pas possible de récupérer seulement les dernières données. 

**Rappel** : L'authentification pour l'API Polar n'est pas pareil que l'authentification avec les cartes RFID. Il y a 1 compte Polar (celui du coach) qui est relié à plusieurs montres et l'authentification des cartes RFID (client) en est une totalement séparée.

## Jeudi 10 Février 2022 
Nous avons réalisé une présentation intermédiaire pour montrer l'avancement de nos projets. Suite à cette présentation, je réalise que jusque là je n'ai fait que de la recherche ou quelques essais mais je n'ai pas encore de POC concrèt.

## Jeudi 24 Février 2022

En m'aidant de la doc Polar, je vais créer un objet qui me permettra de récupérer les datas. J'ajouterai ensuite l'objet au programme qui me permet de vérifier les cartes RFID pour récupérer les données lorsqu'on s'identifie avec la carte RFID. Je vais également créer une base de données pour enregistrer quelques données. 

## Jeudi 3 Mars 2022 
Malade (Covid-19)

## Jeudi 10 Mars 2022
Le rendu du projet est fixé à la semaine prochaine. J'ai fait l'update du firmware de la montre Polar. 