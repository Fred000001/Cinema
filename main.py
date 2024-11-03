from tkinter import *

fenetre = Tk()
fenetre.title("Seance de cinema !")
fenetre.geometry("400x300")

#fonction qui va s'activer lors du clique sur le bouton reserver
def click_btn(film_id, txt):
    print(f"click ok sur le film n {film_id}")
    
    
    print(f"Vous avez choisit le film {films[film_id-1]["titre"]}")

    nb_place = films[film_id-1]["places"]

    #verifier si le film n'est pas complet
    if nb_place > 0:
        print("Achat effectué !")
        #retier 1 place au nombre de place disponible
        films[film_id-1]["places"] -= 1
        txt.set(films[film_id-1]["places"])
        print(f"le film possède désormais {films[film_id-1]["places"]} places !")
    else:
        print("Film complet !")
        txt.set("Film complet !")

#afficher un message de bienvenue
print("Bienvenue au cinema, voici les films à l'affiche !")

#liste de films
#films = ["Voyage au centre du HTML", "Les 9 jsons cachés", "Algobox - le film"]

#dictionnaire de film
films = [
    { #film 1
        "titre": "Le Seigneur des Scripts", 
        "seance": "18h06",
        "places": 200
    },
    
    { #film 2
        "titre": "Matrix - Les Clés de l'Interface",
        "seance": "10h10",
        "places": 80
    },
    
    { #film 3
        "titre": "Les Aventuriers du Code Perdu",
        "seance": "22h15",
        "places": 120
    },
    
    { #film 4
        "titre": "50 Nuances de JavaScript",
        "seance": "22h15",
        "places": 50
    },
    
    { #film 5
        "titre": "React et les Hooks Magiques",
        "seance": "22h15",
        "places": 130
    }
    
]

#afficher chaque film
for numero, film in enumerate(films, start=1):
    titre: str= film["titre"]
    seance: str= film["seance"]
    places: int= film["places"]
    places_var = StringVar()
    places_var.set(places)
    
    titre_label = Label(fenetre, text=titre)
    titre_label.grid(row=numero, column=0)
    
    seance_label = Label(fenetre, text=seance)
    seance_label.grid(row=numero, column=1)
    
    places_label = Label(fenetre, textvariable=places_var)
    places_label.grid(row=numero, column=2)
    
    bouton = Button(fenetre, text="Reserver", command= lambda num = numero, txt = places_var: click_btn(num, txt))
    bouton.grid(row=numero, column=3)

    
fenetre.mainloop()