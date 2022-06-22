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

def app(): 
    st.subheader("Benachrichtigung anfordern")
    emailteil1=st.text_input("Emailnamen eingeben")
    emaildomains=["@gmail.com","@gmx.de","@web.de"]

    option = st.selectbox('Email Domain auswählen', emaildomains)
    ganzeemail=emailteil1+option

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    yag = yagmail.SMTP("dbaaahn@gmail.com","wmgtfktvxmjsipox")
    contents = [
            "Ein neuer Preis ihrer Verbindung ist verfuegbar."
            "\n"
            "Kaufen Sie sich ein Ticket."
            "\n"

            "Freundlicher Gruss"
            "\n"
            "\n"
            "DBTickeralert"
            ]
    liste=[1,2,3,4,5,6,7,8,9,10]

                    
    preisangabe = st.slider("Ihr gewünschter Höchstpreis:")
    with st.form(key='form1'):
            submit_buttonpreis = st.form_submit_button(label='Benachrichtige mich')    
            if submit_buttonpreis:
                st.write("Sie erhalten eine Email Benachrichitung wenn sich der Preis unter",preisangabe ,"€ befindet") 
                for i in range(len(liste)):
                    if liste[i]<=preisangabe:
                        yag.send(to=ganzeemail,
                        subject='Neuer Preis',
                        contents=contents)
                    else:
                        if preisangabe>liste[i]:
                            st.write("Ihre Kaufbereitschaft ist sehr hoch") 