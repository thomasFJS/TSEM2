# Documentation technique

## Rappel du cahier des charges

### Introduction
Dans le cadre du 2ème travail de semestre, j'ai décidé d'effectuer un projet qui me sera très utile pour le travail de diplôme. L'idée serait de faire une application en python qui récupère des données d'entrainement avec l'API Polar en fonction de la carte RFID qui est détécté.

#### But du projet

#### Contraintes techniques


### Analyse

#### Technologies 
* Python
* Markdown
* Github (versionning, task manager)
* Ordinateur de type PC, 2 écrans
* Visual Studio Code
* Mkdocs (Documentation)
* CrowPi
* NFC Reader ACR122U

##### NFC Reader ACR122U
![NFC Reader](./images/acr122u.png)
Le lecteur NFC ACR122U est un appareil permettant de lire et d'écrire sur des cartes sans contact. Il est basé sur la technologie Mifare 13,56 MHz (RFID) et suit les standard de la norme ISO 18092. L'ACR122U est développé et vendu par ACS ltd .

Pour pouvoir utiliser ce lecteur, j'ai utilisé la librairie *pyscard* 


#### Environnement de développement
Afin de développer mon application, j'ai choisi d'utiliser [VNC Viewer](https://www.realvnc.com/fr/connect/download/viewer/) en premier lieu pour me permettre d'avoir accès au CrowPi depuis Windows. Ensuite, j'ai choisi d'utiliser l'extension [VsCode Remote-SSH](https://code.visualstudio.com/docs/remote/ssh) pour me connecter en SSH au CrowPi et ainsi manipuler les fichier directement depuis VSCode
#### Modèle de données

## Analyse fonctionnelle

### Interface

### Fonctionnalités

## Analyse organique
### Architecture
#### Arborescence de fichier
```
+-- docs
|	+-- documentation.md
|	+-- logbook.md
+-- mkdocs.yml
```

## Tests

## Conclusion