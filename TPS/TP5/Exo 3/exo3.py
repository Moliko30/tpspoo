from tkinter import *

def afficher_donnees():
    """Affiche les données saisies dans le label."""
    prenom = entr1.get()
    nom = entr2.get()
    ville = entr3.get()
    label_resultat.config(text=f"{prenom}//{nom}//{ville}")

def main():
    """Crée une interface graphique avec des champs de saisie et une image."""
    fen1 = Tk()
    txt1 = Label(fen1, text ='Votre prénom :')
    txt2 = Label(fen1, text ='Votre nom :')
    txt3 = Label(fen1, text ='Votre ville :')
    global entr1, entr2, entr3, label_resultat  # Déclaration globale pour accéder dans la fonction
    entr1 = Entry(fen1)
    entr2 = Entry(fen1)
    entr3 = Entry(fen1)
    
    # Agrandissement de la dimension de l'image
    can1 = Canvas(fen1, width=230, height=230, bg='white')
    
    # Assurez-vous que le fichier image est dans le bon répertoire
    photo = PhotoImage(file='photo.png')  # Modifiez le nom de fichier si nécessaire
    item = can1.create_image(200, 200, image=photo)  # Centrer l'image dans le canvas
    
    txt1.grid(row=1, sticky=E)
    txt2.grid(row=2, sticky=E)
    txt3.grid(row=3, sticky=E)
    entr1.grid(row=1, column=2)
    entr2.grid(row=2, column=2)
    entr3.grid(row=3, column=2)
    can1.grid(row=1, column=3, rowspan=3, padx=10, pady=5)
    
    # Ajout des boutons
    btn_valider = Button(fen1, text='Valider', command=afficher_donnees)
    btn_quitter = Button(fen1, text='Quitter', command=fen1.quit)
    btn_reinitialiser = Button(fen1, text='Réinitialiser')
    
    # Alignement horizontal des boutons
    btn_valider.grid(row=4, column=3, sticky=W, padx=5)
    btn_quitter.grid(row=4, column=3, padx=5)  # Correction ici
    btn_reinitialiser.grid(row=4, column=3, sticky=E, padx=5)

    # Label pour afficher les résultats
    label_resultat = Label(fen1, text='')
    label_resultat.grid(row=4, column=0, columnspan=3)  # Modification ici pour le placer sous les champs de saisie

    fen1.mainloop()

if __name__ == "__main__":
    main()