import streamlit as st
 #1. Create an empty list called todo_list to store tasks.
# 2. Display a menu with three choices:
#       1. Add a task
#       2. Remove a task
#       3. Exit
# 3. Ask the user which option they want.
# 4. If they choose 1:
#       - Ask for a task.
#       - Add the task to the todo_list.
# 5. If they choose 2:
#       - Dsiplay the tasks.
#       - Ask which task they want to remove.
#       - Remove that task from the list.
# 6. If they choose 3 end the program.
# 7. Keep showing the menu until the user chooses Exit.


st.title("Todo List")
st.header("Welcme to your todo task tracker:")


#initialize it only if it doesn't already exist. because 
#clicking anything reruns the entire script from top to bottom. 
#So without the if every click does reinitixalizes the list
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

with st.container(border = True):
    st.subheader("Tasks for today:")
    for i in range(len(st.session_state["tasks"])):
        st.write(str(i + 1) + ". " + st.session_state["tasks"][i])




col1, col2 = st.columns(2)

with col1:
    with st.container(border = True):
        st.subheader("Add Task")
        task = st.text_input("New task")
        if st.button("Add"):
            st.session_state["tasks"].append(task)
        
with col2:
    with st.container(border = True):
        st.subheader("Remove Task")
        taskR = st.text_input("Task to be removed")
        
        if st.button("Remove"): 
            if taskR in st.session_state["tasks"]:
                st.session_state["tasks"].remove(taskR)

if st.button("3. Save and exit"):
    st.write("See you next time")


