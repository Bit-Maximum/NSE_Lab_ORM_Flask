from app import app
from flask import render_template
from .crud import *


@app.route("/")
def index():
    buildings_data = get_all_buildings()
    type_data = grouped_by_type()
    country_data = grouped_by_country()
    year_data = grouped_by_year()
    year_by_range_data = get_buildings_in_year_range(2000, 2018)

    html = render_template(
        "index.html",
        buildings=buildings_data,
        type_data=type_data,
        country=country_data,
        year=year_data,
        year_by_range_data=year_by_range_data,
    )
    return html
