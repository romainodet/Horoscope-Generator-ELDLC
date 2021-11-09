import random

signes = ["Bélier",
          "Taureau",
          "Gémeaux",
          "Cancer",
          "Lion",
          "Vierge",
          "Balance",
          "Scorpion",
          "Sagittaire",
          "Capricorne",
          "Verseau",
          "Poissons"
          ]

debut = ["Aujourd'hui",
         "En ce moment",
         "Dans cette journée",
         "Ce matin",
         "Cet après-midi"
         ]

milieu = [
    "les miracles arrivent",
    "la vie est plutôt agréable",
    "tu peux tout entreprendre",
    "tu ferais mieux de rester au lit",
    "tu n'es pas au top",
    "le changement arrive",
    "on te fera un compliment",
    "on te sermoneras",
    "remet toi en question",
    "change de vie",
    "tu n'as plus de pognon",
    "un carton rose tu prendras",
    "achète toi une vie",
    "il faut songer à revoir ses priorités",
    "change de voiture",
    "trouve toi des amis",
    "c'est ton jour de chance",
    "reste chez toi",
    "sors couvert",
    "c'est un grand jour",
    "ne dis pas bonjour",
    "sois poli avec tes collègues",
    "reste calme",
    "répond merde à tout",
    "tu es dans le mal",
    "personne ne t'aime",
    "tu es toujours en vie et c'est déjà ça",
    "prends garde à toi",
    "surveille tes affaires",
    "regarde BFM TV",
    "fais des pranks à tes camarades",
    "tu es pauvre",
    "tu as oublié de te laver",
    "tu vas enfin avoir l'air intelligent",
    "ta copine va te larguer",
    "tu es fatigué",
    "tu te prends pour Batman",
    "ton égo en prend un coup",
    "tu es moche",
    "tu répondras à un bonjour qui n'était pas pour toi",
    "tu finiras à l'hopital pour avoir commandé une chocolatine"
]
milieu2 = [". En effet, le karma te rattrape",
           ". De ce fait, tu devrais changer d'estheticienne",
           ". Sois heureux",
           ". Arrête de tirer la gueule",
           ". Fais attention à ton garagiste",
           ". Ne reste pas tout seul",
           ". La vie est belle",
           ". Prend une douche",
           ". Lave toi les dents",
           ". Tu as perdu à smash",
           ". Aime ton prochain",
           ". Va à l'église",
           ". Change de chirugien",
           ". N'oublie pas le pain",
           ". Donne toi à dieu",
           ". C'est votre journée, il faut PRO-FI-TER",
           ". Pends-toi par les pieds",
           ". Ouvre un paquet de cracotte",
           ". Déclare ta flamme à ta secrétaire",
           ". Avoue ta double vie à ta femme (oui mais laquelle ?)",
           ". Ton mariage bat de l'aile",
           ". Tu te mets à parler comme un marseillais",
           ". Tu prends l'accent québécois",
           ". Tu es victime d'une malédiction vaudou",
           ". Adopte un bébé oppossum",
           ". Un chat roux te griffera le nez",
           ". Une fiente de pigeon s'écrasera sur ton crâne",
           ". Un bébé pleurera dans ton oreille pendant tout le trajet du bus",
           ". Tu redouble de deux classes",
           ". Tu te sens nauséeux",
           ". Tu t'identifie comme un plat de spaghetti bolognaise",
           ". Ta soeur sort avec ton frère",
           ". Ton poisson aura la diarrhée pendant 8 jours",
           ". Tu vas retrouver 20€ dans une de tes poches avant de te rendre compte qu'il s'agit d'un billet de monopoly",
           ". Un groupe d'enfants te volera ton téléphone",
           ". Tu te shoote à l'homéopathie",
           ". Tu décides de changer de look",
           ". Tu lis Closer en cachette dans les toilettes",
           ". Tu as pris du poids pendant les vacances",
           ". Ta femme est enceinte de triplés",
           ". Ton rendez-vous Tinder ressemble à Igor Bogdanov",
           ". Ta mère t'avoue qu'elle sort avec Macron",
           ". Tu te découvre un cheveux blanc",
           ". Ton père devient le gourou d'une secte",
           ". Tu décides de te faire un tatouage tribal sur le biceps",
           ". Une vieille te donnera des coups de canne",
           ". Ta grand-mère participe à des tournois de roulette russe",
           ". Tu vas liquider ton héritage pour t'acheter un pistolet laser qui fait piou-piou",
           ". Tu te baladera chez toi en slip à la vue de tous tes voisins",
           ". Tu vas te prendre une patate de forain en pleine poire",
           ". Tu vas avaler un cure-dent",
           ". Tu marcheras pieds nus sur un lego",
           ". Tu seras le dernier choisi pour les équipes de foot",
           ". Ta soeur tourne dans un film X",
           ". Ton voisin se met au saxophone",
           ". Tes seules lettres au scrabble seront X, J, K et Y"
           ]
fin = ["car tu es génial", "car l'amour se fait attendre",
       "car tes projets vont se réaliser",
       "car ton conjoint commet sûrement un adultère",
       "car la vie est une chienne",
       "car ton pull-over est moche",
       "car tu es mon soleil ❤",
       "car tu es beau",
       "car le changement c'est maintenant",
       "car c'est notre projet !!!",
       "c'est un des effets de l'amour.",
       "car la consanguinité c'est sous-coté",
       "car le gras c'est la vie",
       "ce qui est plus pratique avec des baguettes",
       "c'est probablement un signe divin",
       "dommage pour toi",
       "tu feras mieux la prochaine fois",
       "heureusement qu'il te reste des bières au frigo",
       "ça semblait une bonne idée sur le coup",
       "c'est toujours mieux que ta mère",
       "au moins tu n'est plus le seul maintenant",
       "c'est surement un coup des réptiliens"
       ]

parcours_liste = 0
prenom = 1

while len(signes) > parcours_liste:
    print()
debut_phrase = ""
milieu_phrase = ""
fin_phrase = ""
phrase = ""
signe_act = signes[parcours_liste]
debut_phrase = random.choice(debut)
milieu_phrase = random.choice(milieu)
milieu_phrase_2 = random.choice(milieu2)
fin_phrase = random.choice(fin)

if prenom == 1:
    phrase = debut_phrase + " " + signe_act + ", " + milieu_phrase + "" +  milieu_phrase_2 + " " + fin_phrase
elif prenom == 2:
    phrase = debut_phrase + ", " + milieu_phrase + " " + signe_act + "" + milieu_phrase_2 + " " + fin_phrase
elif prenom == 3:
    phrase = debut_phrase + ", " + milieu_phrase + "" + milieu_phrase_2 + " " + signe_act + " " + fin_phrase
print(signe_act + " : " + phrase + ".")

parcours_liste += 1
prenom += 1
if prenom > 3:
    prenom = 1
