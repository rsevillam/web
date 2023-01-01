import streamlit as st 
import Funciones

listaTareas = Funciones.buscaLista()

def añadeTarea():
    tarea = st.session_state["nuevaTarea"] + "\n"
    listaTareas.append(tarea)
    Funciones.escribeLista(listaTareas)

st.title("Gestor de Tareas")
st.subheader("Añadir, Editar o completar tareas")
st.write("Sirve para incrementar la productividad")

for indice, tarea in enumerate(listaTareas):
    checkBox = st.checkbox(tarea, key=tarea)
    if checkBox:
        listaTareas.pop(indice)
        Funciones.escribeLista(listaTareas)
        del st.session_state[tarea]
        st.experimental_rerun()

st.text_input(label="", placeholder="Añadir nueva tarea", on_change=añadeTarea, key="nuevaTarea")

st.session_state


