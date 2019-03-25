"""
                 /
    |      /  |////:  o////  ./////    s`      y////-
    |         |       /      s-    s.  h`      h
    |         |////.  /      s-    s-  h`      d////`
    |         |       /      s-    s.  h`      h
    |////     |////:  o/::/  -o/::/o   y////.  d////-

        -mmmmm.   ymmmmmmmmmy-   ymmmm-       -ymmmmmm
        -mmmmm.   ymmmm+ohmmmm-  ymmmm-     :mmmmdo/+s
        -mmmmm.   ymmm     hmmmo ymmmm-    hmmmm:
        -mmmmm:   hmmm     mmmm/ ymmmm/    ymmmmy:
        -mmmmmmmmmmmmmmmmmmmms   ymmmmmmmm  dommmmmmmm
        -hhhhhhhhhhhhhhhhys+/    shhhhhhhhy  ./shddhh/
        
        
     file :main.py
     By: romain.odet <romain.odet@lecole-ldlc.com>           
     Created: 25/03/2019 14:35 by Romain ODET  
"""
import random

signes = ["Bélier", "Taureau", "Gémeaux", "Cancer", "Lion", "Vierge", "Balance", "Scorpion", "Sagittaire",
              "Capricorne", "Verseau", "Poissons"]

debut = ["Aujourd'hui", "En ce moment", "Dans cette journée", "Ce matin", "Cet après-midi"]

milieu = ["les miracles arrivent", "la vie est plutôt agréable", "tu peux tout entreprendre",
          "tu ferais mieux de rester au lit", "tu n'es pas au top", "le changement arrive", "Olivier te fera un compliment", "Guillaume te sermoneras"]

milieu2 = [". En effet, le karma te rattrape", ". De ce fait, tu devrais changer d'estheticienne", ". Sois heureux",
           ". Arrête de tirer la gueule", ". Fais attention à ton garagiste", ". Ne reste pas tout seul", ". La vie est belle", ". Prend une douche", ". Lave toi les dents"]

fin = ["car tu es génial", "car l'amour arrive progressivement", "car tes projets vont se réaliser",
       "car ton conjoint commet sûrement un adultère", "car la vie est une chienne", "car ton pull-over est moche", "car tu es mon soleil <3", "car tu es beau"]

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

    if prenom  == 1:
        phrase = debut_phrase + " " + signe_act + ", " + milieu_phrase + "" + milieu_phrase_2 + " " + fin_phrase
    elif prenom  == 2:
        phrase = debut_phrase +  ", " + milieu_phrase + " " + signe_act + "" + milieu_phrase_2 + " "  + fin_phrase
    elif prenom  == 3:
        phrase = debut_phrase + ", " + milieu_phrase + ""  + milieu_phrase_2 + " " + signe_act + " " + fin_phrase

    print(signe_act + " : " + phrase + ".")

    parcours_liste += 1
    prenom += 1

    if prenom  > 3:
        prenom  = 1


    #print(parcours_liste, " ", prenom )