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

J'ai repris le projet "CrowMagic" auquel j'ai participé l'année passée dans le cadre des ateliers décloisonnés. Le projet utilisait les cartes RFID et je voulais reprendre un peu l'utilisation des cartes pour mon projet. 

J'ai installé [VNC Viewer](https://www.realvnc.com/fr/connect/download/viewer/) pour utiliser le CrowPi directement sur mon PC. 

Chaque carte RFID possède un id, dans un json je définis les valeurs dont j'ai besoin qui sont associées à l'id de la carte.