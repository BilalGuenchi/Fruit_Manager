import streamlit as st
from fruit_manager import *

st.title("Dashboard de la Plantation")

inventaire = ouvrir_inventaire()
tresorerie = ouvrir_tresorerie()

with st.sidebar:
    st.header("Vendre des fruits")
    fruit_vendre = st.selectbox("Choisir un fruit", list(inventaire.keys()))
    quantite_vendre = st.number_input("Quantite à vendre", min_value=1, step=1)

    if st.button("Vendre"):
        inventaire, tresorerie = vendre(inventaire, fruit_vendre, quantite_vendre, tresorerie)

    st.header("Recolter des fruits")
    fruit_recolter = st.selectbox("Choisir un fruit à récolter", list(inventaire.keys()), key="recolter")
    quantite_recolter = st.number_input("Quantite à récolter", min_value=1, step=1, key="quantite")

    if st.button("Récolter"):
        inventaire = recolter(inventaire, fruit_recolter, quantite_recolter)

ecrire_inventaire(inventaire)
ecrire_tresorerie(tresorerie)

st.header("Tresorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f} $")

st.header("Inventaire")
st.table(inventaire)