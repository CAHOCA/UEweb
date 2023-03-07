from database.models import *
from datetime import datetime


def db_updateStudent(id, first_name, name, nationality, taf1, taf2, birth_date):
    print("db_updateStudent")
    student = User.query.get(id)
    student.first_name = first_name
    student.name = name
    student.nationality = nationality
    if birth_date != "":
        birth_date2 = datetime.strptime(birth_date,
                                        '%Y-%m-%d')
        student.birth_date = birth_date2
    student.taf1 = taf1
    student.taf2 = taf2

    db.session.commit()


def db_updateTaf(id, name, director):
    print("db_updateTaf")
    taf = Taf.query.get(id)
    taf.name = name
    taf.director = director
    db.session.commit()


def db_updateEnterprise(id, name):
    print("db_updateEnterprise")
    enterprise = Organisation.query.get(id)
    enterprise.name = name
    db.session.commit()


def db_updateOccupation(id, title, description, start_date, organisation):
    occupation = Occupation.query.get(id)
    occupation.title = title
    occupation.description = description
    if start_date != "":
        start_date2 = datetime.strptime(start_date, '%Y-%m-%d')
        occupation.start_date = start_date2
    occupation.organisation = organisation
    db.session.commit()
