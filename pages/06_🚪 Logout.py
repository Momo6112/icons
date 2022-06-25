import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
from PIL import Image
import streamlit as st
import streamlit_multipage
from streamlit_multipage.multipage import MultiPage
import streamlit as st
from streamlit_option_menu import option_menu

col1,col2=st.columns(2)

with col1: 
  def app():
      st.write(st.session_state.name,
              "Möchten Sie sich wirklich ausloggen?")
      with st.form("button"):
          ja=st.form_submit_button(label="Ja")
          nein=st.form_submit_button(label="Nein")
        
      if ja:
          del st.session_state.name
          st.success("Sie haben sich erfolgreich ausgeloggt")
         
        
      if nein:
          st.info("Nicht abgemeldet")
app()
with col2:
   def load_lottieurl2(url: str):
      r = requests.get(url)
      if r.status_code != 200:
      return None
      return r.json()
      lottie_url_hello2 = "https://assets9.lottiefiles.com/packages/lf20_alpjfedu.json"
 #"https://assets3.lottiefiles.com/packages/lf20_E3exCx.json"
      lottie_hello2 = load_lottieurl2(lottie_url_hello2)
      st_lottie(lottie_hello2, key="hello")
    
 load_lottieurl2("https://assets9.lottiefiles.com/packages/lf20_alpjfedu.json")
        
#https://assets9.lottiefiles.com/packages/lf20_alpjfedu.json
