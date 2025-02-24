from sqlalchemy import func

from config import db
from models import Country, City, Building, TypeBuilding


def get_all_buildings():
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.name.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}


def grouped_by_type():
    query = (
        db.session.query(
            TypeBuilding.name.label("Тип"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.avg(Building.height).label("Средняя высота"),
        )
        .join(Building)
        .group_by(TypeBuilding.name)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}


def grouped_by_country():
    query = (
        db.session.query(
            Country.name.label("Страна"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.avg(Building.height).label("Средняя высота"),
        )
        .join(Country.cities)
        .join(City.buildings)
        .group_by(Country.name)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}


def grouped_by_year():
    query = db.session.query(
        Building.year.label("Год"),
        func.max(Building.height).label("Максимальная высота"),
        func.min(Building.height).label("Минимальная высота"),
        func.avg(Building.height).label("Средняя высота"),
    ).group_by(Building.year)
    return {"head": query.statement.columns.keys(), "body": query.all()}


def get_buildings_in_year_range(start_year=2000, end_year=2018):
    if start_year > end_year:
        start_year, end_year = end_year, start_year
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.name.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
        .filter(Building.year >= start_year, Building.year <= end_year)
    )
    return {"head": query.statement.columns.keys(), "body": query.all()}
