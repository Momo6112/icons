import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import plotly.express as px
from tensorflow import keras 
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

st.title("Preisvorhersage/Diagramm")

conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                      database="dbticket", 
                      user="dbticket_user", 
                      password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
cursor = conn.cursor()

def app():
  coll1,coll2,coll3,coll4=st.columns(4)
  
  with coll1:
    loginname=st.text_input("Benutzer: ")

  with coll2:
    loginpassw=st.text_input("Passwort:")
    anfragenlistebenutzer=[]
    abfrage = cursor.execute("SELECT login.username FROM login WHERE username=%s", [loginname])
    if not cursor.fetchone():  # An empty result evaluates to False.
        st.write("Kein Benutzer mit diesem Benutzernamen")
    else:
        abfragep = cursor.execute("""SELECT login.passwort FROM login WHERE passwort=%s""", [loginpassw])
        if not cursor.fetchone():  # An empty result evaluates to False.
            st.write("Falsches Passwort")
        else:
            st.write("Sie haben sich erfolgreich eingeloggt")
            richtigentabellen=cursor.execute("Select anfragen.tabelle from anfragen where username=%s", [loginname])
            alleanfragen=cursor.fetchall()
            if alleanfragen==None:
                st.info("Zu diesem Benutzernamen gibt es noch keine Tabelle") 
            else:
                listes=[]
                for b in alleanfragen:
                  liste=b[0]
                  listes.append(liste)

                  with coll3:

                    boxen=st.selectbox("Tabelle: ", listes)
                  with coll1:

                    data_tabelle = pd.read_sql(f"SELECT * FROM {boxen}", conn)

                    df_diagramm= pd.DataFrame(data_tabelle)
                    date_list = df_diagramm['anfrage_tag'].unique()


                    date = st.selectbox("Wähle ein Datum:",date_list)


                    fig = px.line(df_diagramm[df_diagramm['anfrage_tag'] == date], 
                    x = "anfrage_uhrzeit", y = "preis", title = date)
                    st.plotly_chart(fig)

                    cursor.execute(f"SELECT DISTINCT anfrage_tag FROM {boxen}")

                    inhalt = cursor.fetchall()
                    mins=[]
                    maxs=[]
                    dates=[]



                    for d in inhalt:
                     date=str(d[0])
                     cursor.execute(f"SELECT MIN(preis), MAX(preis) FROM {boxen} WHERE anfrage_tag = '{date}' ") 
                     res=cursor.fetchone()
                     mini=res[0]
                     maxi=res[1]
                     mins.append(mini)
                     maxs.append(maxi)
                     dates.append(date)

                    df=pd.DataFrame({'Datum':dates, 'Maximum': maxs, 'Minimum':mins})
                    st.table(df)
                    train_size = int(len(df) * 0.8)
                    df_train, df_test = df[:train_size], df[train_size:len(df)]
                    train_data = df_train.iloc[:, 1:2].values

                    from sklearn.preprocessing import MinMaxScaler
                    scaler = MinMaxScaler(feature_range=(0, 1))
                    train_data_scaled = scaler.fit_transform(train_data)


                    x_train = []
                    y_train = []

                    time_window = 3

                    for i in range(time_window, len(train_data_scaled)):
                        x_train.append(train_data_scaled[i-time_window:i, 0])
                        y_train.append(train_data_scaled[i, 0])

                    x_train, y_train = np.array(x_train), np.array(y_train)

                    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))





                    with st.spinner('Bitte warten, der prognostizierte Preis wird berechnet'):
                            time.sleep(45)
                    st.success('Ergebnis folgt')
                    model = Sequential()
                    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
                    model.add(Dropout(0.2))
                    model.add(LSTM(units=50, return_sequences=True))
                    model.add(Dropout(0.2))
                    model.add(LSTM(units=50))
                    model.add(Dropout(0.2))
                    model.add(Dense(units=1))

                    model.compile(optimizer='adam', loss='mean_squared_error')

                    model.fit(x_train, y_train, epochs=25, batch_size=32)



                    actual_stock_price = df_test.iloc[:, 1:2].values

                    total_data = pd.concat((df_train['Minimum'], df_test['Minimum']), axis=0)
                    test_data = total_data[len(total_data)-len(df_test)-time_window:].values
                    test_data = test_data.reshape(-1, 1)
                    test_data = scaler.transform(test_data)



                    total_dates = pd.concat((df_train['Datum'], df_test['Datum']), axis=0)
                    test_dates = total_dates[len(total_dates)-len(df_test)-time_window:].values
                    test_dates = test_dates.reshape(-1, 1)


                    x_test = []
                    for i in range(time_window, len(test_data)):
                        x_test.append(test_data[i-time_window:i, 0])

                    x_test = np.array(x_test)
                    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))



                    predicted_stock_price = model.predict(x_test)
                    predicted_stock_price = scaler.inverse_transform(predicted_stock_price)




                    real_data = [test_data[len(test_data)+1-time_window:len(test_data+1), 0]]
                    real_data = np.array(real_data)
                    real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

                    prediction = model.predict(real_data)
                    prediction = scaler.inverse_transform(prediction)



                    preis=float(prediction[0][0])
                    preis2=str(round(preis, 2))+ ' EUR'
                    st.subheader('Der prognostizierte Preis beträgt morgen:  ')
                    st.subheader(preis2)

app()
