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
import bcrypt
import hashlib
import pages.home

def app():
    conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                            database="dbticket", 
                            user="dbticket_user", 
                            password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

    engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
    cursor = conn.cursor()
    with st.form(key='form201'):
        eingabe=st.text_input("Username:")
        passw1=st.text_input("Passwort:",type="password")
        

        register = st.form_submit_button(label="Registrieren")
        

    
    def add_userdata(eingabe,passw1):
            anf=cursor.execute("Select login.username From login where username=%s",[eingabe])
            if not cursor.fetchone():
                passw1 = bcrypt.hashpw(passw1.encode("utf-8"), bcrypt.gensalt(5)).decode("utf-8")
                result=pandas.DataFrame(columns=["username","passwort"])
                result.loc[len(result)]=[eingabe,passw1]
                result.to_sql(name="login", con=engine, if_exists="append")
                result=result[0:0]
                st.info("Erfolgreich registriert")
            else:
                st.warning("Der Benutzername existiert bereits")
        
                
    if register:   
        add_userdata(eingabe,passw1)
            