from database.models import *
from datetime import datetime
from database.add_db import *
def create_test_db():
    db.drop_all()
    db.create_all()
    taf1 = Taf(name="DCL", director="Théo CALVAR")
    db.session.add(taf1)
    taf2 = Taf(name="Login", director="Hélène COULON")
    db.session.add(taf2)
    enterprise = Organisation(name="CGI")
    db.session.add(enterprise)
    enterprise2 = Organisation(name="Cap Gemini")
    db.session.add(enterprise2)
    enterprise3 = Organisation(name="EDF")
    db.session.add(enterprise3)
    promo = Promo(annee=2020)
    promo2 = Promo(annee=2021)
    db.session.add(promo)
    db.session.add(promo2)
    tutor = Tutor(name="Tolosa", first_name="Jean", number="0123456789", mail="j.t@cgi.fr", enterprise=1)
    db.session.add(tutor)
    stage = Stage(title="Code un truc", date_start=datetime.now(), date_end=datetime.now(), resume="resume",
                  rapport="rapport", tutor=1, enterprise=1)
    db.session.add(stage)
    stage2 = Stage(title="Code 2 truc", date_start=datetime.now(), date_end=datetime.now(), resume="resume",
                  rapport="rapport", tutor=1, enterprise=1)
    db.session.add(stage2)
    stage3 = Stage(title="Code 3 truc", date_start=datetime.now(), date_end=datetime.now(), resume="resume",
                   rapport="rapport", tutor=1, enterprise=1)
    db.session.add(stage3)
    etudiant = User(name="Riegel", first_name="Sam", nationality="French", birth_date=datetime.now(), taf1=2,
                    taf2=1, stage=1, promo=1, occupation="Chef de projet")
    db.session.add(etudiant)
    etudiant2 = User(name="Bailey", first_name="Laura", nationality="French", birth_date=datetime.now(), taf1=1,
                     taf2=2, stage=1, promo=1, occupation="Developpeur")
    db.session.add(etudiant2)
    etudiant3 = User(name="Mercer", first_name="Matthew", nationality="Américain", birth_date=datetime.now(), taf1=1,
                     taf2=2, stage=1, promo=2, occupation="Developpeur")
    db.session.add(etudiant3)
    db_addOccupation("Chef d'équipe","Je suis trop fort","2020-10-10",1,1)
    db_addOccupation("Codeur","moins fort","2020-05-05",1,1)
    db_addOccupation("Poète", "Je suis trop fort", "2020-10-10", 2, 1)
    db_addOccupation("Codeur", "moins fort", "2020-05-05", 2, 1)
    db_addOccupation("Pilote d'avion de chasse", "Je suis trop fort", "2020-10-10", 3, 1)
    db_addOccupation("Codeur", "moins fort", "2020-05-05", 3, 1)
    db.session.commit()