import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Carlos Carrillo")

modulos = st.selectbox("Selecione el módulo",["Listas", "Arreglos", "Funciones", "POO"])

if modulos == "Listas":
  st.write("Te encuentras en el módulo de Listas")

  valor_inicial = st.number_input("Ingresa tu valor inicial del rango",value=0)
  valor_final = int(st.number_input("Ingresa tu valor final del rango",value=10))

  Lista = list(range(valor_inicial,valor_final))

  st.write(Lista)

elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de Arreglos")
elif modulos == "Funciones":
  st.write("Te encuentras en el módulo de Funciones")
  
else:
  st.write("Te encuentras en el módulo de POO")
