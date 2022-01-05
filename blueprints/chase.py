from flask import Blueprint, render_template
import requests
from algorithms.ChaseAPI import game
from algorithms.Table import habitat

bchase = Blueprint("bchase", __name__, static_folder="static", template_folder="templates")


@bchase.route('/Chase/')
def chase():
    return render_template('Chase.html', fgame=game())


@bchase.route('/cats/')
def cats():
    return render_template('cat.html')


@bchase.route('/Habitats/')
def habitats():
    return render_template('Habitats.html', habitat=habitat())

