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
    st.write(st.session_state.user,
            "Möchten Sie sich wirklich ausloggen?")
    with st.form("button"):
        ja=st.form_submit_button(label="Ja")
        nein=st.form_submit_button(label="Nein")
        
    if ja:
        del st.session_state.name
        st.success("Sie haben sich erfolgreich ausgeloggt")
        
    if nein:
        st.info("Nicht abgemeldet")
        
