import streamlit as st
from pymongo import MongoClient

# Conexión a MongoDB Atlas (reemplaza con tu URI)
uri = "mongodb+srv://airflow_user:admin123@cluster0.r16adub.mongodb.net/registroDB?retryWrites=true&w=majority&appName=Cluster0"

cliente = MongoClient(uri)
db = cliente['registroDB']
coleccion = db['usuarios']

st.title("Registro de Usuarios")

nombre = st.text_input("Nombre")
correo = st.text_input("Correo electrónico")
edad = st.number_input("Edad", min_value=0, max_value=120, step=1)

if st.button("Registrar"):
    if not nombre or not correo or edad == 0:
        st.warning("Por favor completa todos los campos")
    else:
        usuario = {
            "nombre": nombre,
            "correo": correo,
            "edad": int(edad)
        }
        coleccion.insert_one(usuario)
        st.success(f"Usuario {nombre} registrado correctamente")

# Mostrar usuarios registrados
st.subheader("Usuarios registrados")
usuarios = list(coleccion.find())

for u in usuarios:
    st.write(f"- {u['nombre']} - {u['correo']} - {u['edad']} años")
