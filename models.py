import csv

from app import app
from config import db

#
# from sqlalchemy.orm import declarative_base
#
# db.Model = declarative_base()
#
# db.metadata.clear()

class Country(db.Model):
    __tablename__ = "country"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Страна", db.String(100), nullable=False)
    cities = db.relationship("City", cascade="all, delete")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"id: {self.id}, Страна: {self.name}"


class City(db.Model):
    __tablename__ = "city"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("Город", db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"))

    country = db.relationship("Country", back_populates="cities")
    buildings = db.relationship(
        "Building", cascade="all, delete"
    )

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        return f"id: {self.id}, Город: {self.name}, country_id: {self.country_id}"


class TypeBuilding(db.Model):
    __tablename__ = "type_building"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Тип", db.String(100), nullable=False)

    buildings = db.relationship(
        "Building", cascade="all, delete"
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"id: {self.id}, Тип: {self.type}"


class Building(db.Model):
    __tablename__ = "building"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Название", db.String(200), nullable=False)
    type_building_id = db.Column(db.Integer, db.ForeignKey("type_building.id"))
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"))
    year = db.Column(db.Integer)
    height = db.Column(db.Integer)

    type_building = db.relationship("TypeBuilding", back_populates="buildings")
    city = db.relationship("City", back_populates="buildings")

    def __init__(self, title, type_building_id, city_id, year, height):
        self.title = title
        self.type_building_id = type_building_id
        self.city_id = city_id
        self.year = year
        self.height = height

    def __repr__(self):
        return (
            f"id: {self.id}, Здание: {self.title}, type_building_id: {self.type_building_id}, "
            f"city_id: {self.city_id}, Год: {self.year}, Высота: {self.height}"
        )


app.app_context().push()
with app.app_context():
    db.create_all()

#
# if __name__ == '__main__':

    # items = [
    #     'Небоскрёб', 'Антенная мачта', 'Бетонная башня', 'Радиомачта', 'Гиперболоидная башня', 'Дымовая труба',
    #     'Решётчатая мачта',
    #     'Башня', 'Мост'
    # ]
    # for item in items:
    #     db.session.add(TypeBuilding(item))
    # db.session.commit()
    #
    # # Load Country data
    # with open('data/country.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     heading = next(reader)
    #     for row in reader:
    #         country = Country(*row)
    #         db.session.add(country)
    #     db.session.commit()
    # #
    # # # Load Cities data
    # with open('data/city.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     heading = next(reader)
    #     for row in reader:
    #         country = City(*row)
    #         db.session.add(country)
    #     db.session.commit()

    # # Load Buildings data
    # with open('data/building.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     heading = next(reader)
    #     for row in reader:
    #         country = Building(*row)
    #         db.session.add(country)
    #     db.session.commit()