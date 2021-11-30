from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    im_bin = image.binarisation(S)
    im_loc = im_bin.localisation()
    c = 0.
    k = int(0)
    for i in range (10) :
        im_rez = im_loc.resize(liste_modeles[i].H, liste_modeles[i].W)
        if im_rez.similitude(liste_modeles[i]) > c :
            c = im_rez.similitude(liste_modeles[i])
            k = int(i)
    return k

