# Freyja

!! Ce Logiciel a été créé dans un but éducatif et pour mon apprentissage du python, merci de ne pas l'utiliser à des fins malhonnêtes !!
Je ne suis en aucun ras responsable des données pouvant circuler sur un réseau louche ou sur internet.

Un spyware codé en python (et dans le futur avec du batch et C++).
Ce spyware collecte pour le moment :
- Votre OS, version et type.
- Votre ip internet et locale.
- Vos frappes clavier.
- La tasklist au moment du lancement du spyware.

Et les envois à l'adresse indiquée dans la section "Fin du spyware" dans Freyja.pyw toutes les heures (adresse que vous devrez remplir pour que le spyware envois les données)

Les frappes clavier sont enregistrées dans le fichier key_log.txt qui sera créé quand le spyware sera lancé.
La tasklist est enregistrée dans le fichier output.txt qui sera également créé au moment du lancement du spyware.
L'ip et l'os ne sont stockés dans aucun fichier mais sont ajoutés en tant que subject de l'email.

Les données sont envoyées sur un serveur gmail. Assurez-vous donc d'avoir une addresse email gmail, tout autre boite mail ne marchera pas.
