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

#display the todo list

with st.container(border = True):
    st.subheader("Tasks for today:")
    for i in range(len(st.session_state["tasks"])):
        st.write(str(i + 1) + ". " + st.session_state["tasks"][i])

#default mode
if "mode" not in st.session_state:
    st.session_state["mode"] = None

#add page when add button is pressed
if st.session_state["mode"] == "add":
    with st.container(border =True):
        task = st.text_input("New task")
        if st.button("Confirm adding"):
            if task != "":
                st.session_state["tasks"].append(task)
            st.session_state["mode"] = None
 
#remove page when remove button is pressed
if st.session_state["mode"] == "remove":
    with st.container(border = True):
        taskR = st.text_input("Task to be removed")
        if st.button("Remove"): 
            if taskR in st.session_state["tasks"]:
                st.session_state["tasks"].remove(taskR)
            st.session_state["mode"] = None


col1, col2, col3 = st.columns(3)
if st.session_state["mode"] == None:
    with col1:
        if st.button("Add task"):
            st.session_state["mode"] = "add"
    with col2: 
        if st.button("Remove task"):
            st.session_state["mode"] = "remove"
    with col3: 
        if st.button("Save and exit"):
            st.write("See you next time")


