from flask import render_template,request,redirect,url_for
from ..requests import getSources
from ..models import Source
from . import main

@main.route('/')
def index():

    business = getSources('business')
    entertainment = getSources('entertainment')
    general = getSources('general')
    health  = getSources('health')
    science = getSources('science')
    sports = getSources('sports')
    technology = getSources('technology')
    

    title = 'Home, Welcome to the best News Center'

    return render_template('index.html',title = title, business = business,entertainment = entertainment, general = general, health = health,science = science, sports = sports,technology = technology)