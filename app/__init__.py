"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7p85269vf5qba9bmg-a.oregon-postgres.render.com",
        database="todo_ev8w",
        user="root",
        password="fqi7PzXzysiE992MnMnEoV93LrpVTaWV")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
