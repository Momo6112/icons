from json import load
import streamlit as st
import PIL
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
from PIL import Image
import streamlit as st
import streamlit_multipage 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import bcrypt

conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                        database="dbticket", 
                        user="dbticket_user", 
                        password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
cursor = conn.cursor() 

def app():
    st.set_page_config("DB","house",layout="wide")
    st.title("DB Price App")
    st.header("Anleitung")
    image=Image.open("website.png")
        
    st.image(image,caption="DB Ticker-App")

    st.subheader("Beschreibung")
    #load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_E3exCx.json")
    col1,col2,col3=st.columns(3)
    if "einlogg" not in st.session_state:
        st.session_state.einlogg=False
    if "reg" not in st.session_state:
        st.session_state.reg=False
    def callback1():
        st.session_state.einlogg=True
    def callback2():
        st.session_state.reg=True
    with col1:
        einlogg=st.button("Einloggen",on_click=callback1)
                
    with col2:
        reg=st.button("Registrieren",on_click=callback2)
        
   
            
    
    if einlogg:
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
                    st.success("Sie haben sich erfolgreich eingeloggt")
                    with st.form("log3"):
                      weiter=st.form_submit_button("Fortfahren zur Anfrage")
                      weiter2=st.form_submit_button("Fortfahren zum Diagramm/Preisvorhersage")
                      
            
                    if 'name' not in st.session_state:
                        st.session_state.name =loginn
                    if 'passw' not in st.session_state:
                        st.session_state.passw=loginp
        if best:
            Login(loginn,loginp)
    if reg :
        conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                            database="dbticket", 
                            user="dbticket_user", 
                            password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

        engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
        cursor = conn.cursor()
        with st.form(key='form201'):
            eingabe=st.text_input("Username:")
            passw1=st.text_input("Passwort:",type="password")
            

            register = st.form_submit_button(label="Registrieren",on_click=callback2)
            

        
        def add_userdata(eingabe,passw1):
                anf=cursor.execute("Select login.username From login where username=%s",[eingabe])
                if not cursor.fetchone():
                    passw1 = bcrypt.hashpw(passw1.encode("utf-8"), bcrypt.gensalt(5)).decode("utf-8")
                    result=pandas.DataFrame(columns=["username","passwort"])
                    result.loc[len(result)]=[eingabe,passw1]
                    result.to_sql(name="login", con=engine, if_exists="append")
                    result=result[0:0]
                    st.info("Erfolgreich registriert")
                    st.success("Sie können nun zum Login")
                
                else:
                    st.warning("Der Benutzername existiert bereits")
            
                    
        if register:   
            add_userdata(eingabe,passw1)
app()
                         
            
            
            
        

