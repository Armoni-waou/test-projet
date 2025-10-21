import streamlit as st
import pandas as pd

st.header("L'appli de Cataclop aka Lise")

st.header("Voici une petite demonstation de mes talents")


nombres = [1, 2, 3, 4, 5]
carré = [1**2, 2**2, 3**2, 4**2, 5**2]
d = {"nombres":nombres, "carré":carré}
data = pd.DataFrame(d)

st.header("n'hesitez pas aller voir l'appli de Romain : 
https://bonjourre-tousses.streamlit.app/")


st.header("attention aux espions")
st.header("Si vous vous sentez observé, ce qui va suivre vous serra utile")

st.write(data)
