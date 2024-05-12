import streamlit as st
import functionsbonarea
import functionsfruteria


def get_list_fruteria():
    global todos
    todos = functionsfruteria.get_todos()

    def add_todo():
        todo = st.session_state['new_todo'] + '\n'
        if todo.strip():  # Check if the input is not empty or whitespace only
            todos.append(todo)
            functionsbonarea.write_todos(todos)
            st.session_state['new_todo'] = ''  # Clear the text input

    st.title('Lista de la compra BonArea')
    st.subheader('Lista de productos para próximo día')
    st.write('Añadir productos en la lista')
    for i, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(i)
            functionsbonarea.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()
    st.text_input(label='escribir productos debajo:', placeholder='Añadir nuevo producto...',
                  on_change=add_todo, key='new_todo')


# Comprobación para que la función se ejecute solo cuando se llame directamente a este script
if __name__ == "__main__":
    get_list_fruteria()
