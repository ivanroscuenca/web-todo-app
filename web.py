import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    if todo.strip():  # Check if the input is not empty or whitespace only
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state['new_todo'] = ''  # Clear the text input
        st.experimental_rerun()

st.title('Lista de la compra de Ivan & Jessica')
st.subheader('Lista de productos para próximo día')
st.write('Añadir productos en la lista')

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='escribir productos debajo:', placeholder='Añadir nuevo producto...',
              on_change=add_todo, key='new_todo')
