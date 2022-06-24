from http.client import CONFLICT
from re import X
from telnetlib import DO
from typing import Collection
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
from bs4 import BeautifulSoup
import requests
import time 
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px 
import plotly
from matplotlib import dates as mpl_dates
from cProfile import label
from distutils.cmd import Command
import datetime 
from streamlit.cli import main  
from streamlit.proto.RootContainer_pb2 import RootContainer
import pandas as pd 
import plotly.figure_factory as ff
import numpy as np
from streamlit_option_menu import option_menu 
import yagmail
from dbTable import *
from http.client import CONFLICT
from re import X
from telnetlib import DO
from typing import Collection
import smtplib, ssl
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import streamlit as st

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_p4kr3lub.json"
#"https://assets3.lottiefiles.com/packages/lf20_E3exCx.json"
#lottie_hello = load_lottieurl(lottie_url_hello)
#st_lottie(lottie_hello, key="hello")
def app():
   st.subheader("Hallo!")
   strings= ("Wir sind Artur, Katja, Anna-Maria, Muhammet, Sven und Lina."
               "\n"
               "\n"
               "Wir sind Studierende der FH Aachen und haben im Zuge des Vertiefungsmoduls Digital Lab diese Website ins Leben gerufen.""\n" "\n"
               "\n"
               "Uns ist aufgefallen, dass Zugverbindungen der Deutschen Bahn stark im Preis schwanken."
               "\n" 
               "Je nachdem, wann man eine Anfrage startet - ob Morgens oder Nachmittags, am Wochenende oder unter der Woche - schwankt der Preis für die exakt gleiche Verbindung. "
               "\n"
               "\n"
               "Als Studierende - die tendenziell immer zu wenig Geld in der Tasche haben - hat uns das natürlich stutzig gemacht! "
               "\n"
               "\n"
               "Die Idee zu dieser Website wurde geboren."
               "\n"
               "\n"
               "Mit DB-Price-APP wollen wir es euch als Nutzern ermöglichen eure Wunsch-Verbindung zu tracken und euch ihren Preisverlauf anschaulich anzeigen zu lassen, damit ihr ein Gefühl für die Preisentwicklung bekommt."
               "\n"
               "\n"
               "Außerdem könnt ihr eine Email-Benachrichtigung aktivieren, sodass ihr eine Mail bekommt, sobald der Preis eurer Wunschverbindung unter eure zuvor angegebene Preisgrenze gefallen ist.""\n"
               "\n"
               "\n"
               "Damit soll vermieden werden, dass ihr selbst ständig eure Verbindung aktualisieren müsst." "\n"
               "So spart ihr mit DB-Price-APP  im Idealfall nicht nur Geld sondern auch noch Zeit und Nerven ;-)"  
               "\n" 
               "\n"
               "Kontakt:" 
               "\n"
               "\n"
               "Artur Sichwardt:	artur.sichwardt@alumni.fh-aachen.de"
               "\n"
               "\n"
               "Katja Gröning: 	katja.groening@alumni.fh-aachen.de"
               "\n"
               "\n"
               "Anna-Maria Kremer: 	anna-maria.kremer@alumni.fh-aachen.de"
               "\n"
               "\n"
               "Muhammet Aydogan:	muhammet.aydogan@alumni.fh-aachen.de"
               "\n"
               "\n"
               "Sven Piotrowski:	sven.piotrowski@alumni.fh-aachen.de"
               "\n"
               "\n"
               "Lina Koppany: 	lina.koppany@alumni.fh-Aachen.de""\n"
            )
   st.write(strings)
   
   
app()
lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_p4kr3lub.json"
#"https://assets3.lottiefiles.com/packages/lf20_E3exCx.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")
load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_E3exCx.json")
