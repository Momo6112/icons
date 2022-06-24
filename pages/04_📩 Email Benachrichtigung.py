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

conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                      database="dbticket", 
                      user="dbticket_user", 
                      password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
cursor = conn.cursor()

def app(): 
    st.subheader("Benachrichtigung anfordern")
    anfragenlistebenutzer=[]
    collll1,collll2,collll3,collll4=st.columns(4)
    with collll1:
      user="ich"
      st.write("Benutzername:",user)
      #st.text_input("Benutzer:",st.session_state.name)
      richtigentabellen1=cursor.execute('Select anfragen.tabelle FROM anfragen WHERE username=%s',[user])
                                        #=%s", [st.session_state.name])
      alleanfragen1=cursor.fetchall()
      if alleanfragen1==None:
        st.info("Zu diesem Benutzernamen gibt es noch keine Tabelle") 
      else:
        for tabell in alleanfragen1:
            anfragenlistebenutzer.append(tabell[0])
      boxen1=st.selectbox("Für folgende Anfrage:", anfragenlistebenutzer)
      tabell2=cursor.execute("SELECT * FROM boxen1")
      prei=cursor.fetchall()
      df_diagramm= pd.DataFrame(tabell2)
      st.table(df_diagramm)
      liste=[]
      if prei==None:
          st.info("Keine Tabelle vorhande") 
      else:
          for tabelle in prei:
              liste.append(tabelle[0])
      #liste.append(tabell2[0])
      st.info(tabell2)
      
    emailteil1=st.text_input("Emailnamen eingeben")
    emaildomains=["@gmail.com","@gmx.de","@web.de"]

    option = st.selectbox('Email Domain auswählen', emaildomains)
    ganzeemail=emailteil1+option
    

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    yag = yagmail.SMTP("dbpriceapp@gmail.com","jeedmppkysrivewz")
    contents = [
            "Hallo :)"
             "\n" 
            "Der Preis Ihrer favoritisierten Verbindung ist auf Ihren Wunschpreis gefallen."
            "\n"
            "Kaufen Sie sich also am besten direkt ein Ticket auf der Seite der DeutschenBahn."
            "\n"
            "Freundliche Grüße und eine gute Fahrt!"
            "\n"
            "\n"
            "DB-Price-App"
            ]
                        
    preisangabe = st.slider("Ihr gewünschter Höchstpreis:")
    with st.form(key='form1'):
            submit_buttonpreis = st.form_submit_button(label='Benachrichtige mich')    
            if submit_buttonpreis:
                st.write("Sie erhalten eine Email Benachrichitung wenn sich der Preis unter",preisangabe ,"€ befindet") 
                for i in range(len(liste)):
                    if [i]<=preisangabe:
                        yag.send(to=ganzeemail,
                        subject='Wunschpreis',
                        contents=contents)
                    else:
                        if preisangabe>liste[i]:
                            st.write("Ihre Kaufbereitschaft ist sehr hoch")
    
app()
