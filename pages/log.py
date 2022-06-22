import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
from PIL import Image
import streamlit as st
import streamlit_multipage
from streamlit_multipage.multipage import MultiPage
import pages.home
import pages.diagramm
import pages.registrieren
import pages.mail_nachricht
import pages.kontakt
import pages.websiteaufruf
import streamlit as st
from streamlit_option_menu import option_menu

def app():
    conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                            database="dbticket", 
                            user="dbticket_user", 
                            password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

    engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
    cursor = conn.cursor()


    with st.form("log"):
        loginn=st.text_input("Benutzername: ")
        loginp=st.text_input("Passwort: ")
        
        best=st.form_submit_button("Bestätigen")

    def Login(loginn,loginp):
                    abfrage = cursor.execute("SELECT login.username FROM login WHERE username=%s", [loginn])
                    if not cursor.fetchone():  # An empty result evaluates to False.
                        st.info("Kein Benutzer mit diesem Benutzernamen")
                    else:
                        abfragep = cursor.execute("""SELECT login.passwort FROM login WHERE passwort=%s""", [loginp])
                        if not cursor.fetchone():  # An empty result evaluates to False.
                            st.warning("Falsches Passwort")
                        else:
                            st.success("Sie haben sich erfolgreich eingeloggt")#

    if best:
        Login(loginn,loginp)