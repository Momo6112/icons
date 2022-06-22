from streamlit_option_menu import option_menu
import pages.home
import pages.diagramm
import pages.registrieren
import pages.mail_nachricht
import pages.kontakt
import pages.websiteaufruf
import pages.log
import pages.auslog
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
import streamlit


st.set_page_config("DB","house",layout="wide")

PAGES = {
    "Willkommen":pages.websiteaufruf,
    "Registrierung": pages.registrieren,
    "Anfragen": pages.home,
    "Diagramm": pages.diagramm,
    "Email-Benachrichtigung":pages.mail_nachricht,
    "Kontakt":pages.kontakt,
    "Login":pages.log,
    "Abmelden":pages.auslog
    
}
conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                        database="dbticket", 
                        user="dbticket_user", 
                        password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
cursor = conn.cursor() 
selected3 = option_menu("DB Price App",options=list(PAGES.keys()), 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "red", "font-size": "12px"}, 
            "nav-link": {"font-size": "12px", "text-align": "left", "margin":"10px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "red"}

        }
    )
if selected3=="Willkommen":
    pages.websiteaufruf.app()
    
       

        # Create a button which will increment the counter
        #increment = st.button('Increment')
        #if increment:
            #st.write(st.session_state.name)

        # A button to decrement the counter
if selected3=="Registrierung":
        pages.registrieren.app()
if selected3=="Anfragen":
        pages.home.app()
if selected3=="Diagramm":
        pages.diagramm.app()
if selected3=="Email-Benachrichtigung":
        pages.mail_nachricht.app()
if selected3=="Kontakt":
        pages.kontakt.app()
if selected3=="Login":
        pages.log.app()
if selected3=="Abmelden":
        pages.auslog.app()
 

