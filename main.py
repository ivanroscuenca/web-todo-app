import streamlit as st
import bonarea
import caprabo
import fruteria

# Título al principio
st.title("Seleccionar Supermercado")

# Mostrar botones para seleccionar supermercado
supermercado = st.button("BonArea")
if supermercado:
    bonarea.get_list_bonarea()

supermercado = st.button("Caprabo")
if supermercado:
    caprabo.get_list_caprabo()

supermercado = st.button("Fruteria")
if supermercado:
    fruteria.get_list_fruteria()