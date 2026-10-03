import streamlit as st
import csv
import os
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

def save_tasks():
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for task in st.session_state["tasks"]:
            writer.writerow([task])

st.title("Todo List")
st.header("Welcme to your todo task tracker:")

#havnet loaded history
if "loaded" not in st.session_state:
    st.session_state["loaded"] = False


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
            st.rerun()
 
#remove page when remove button is pressed
if st.session_state["mode"] == "remove":
    with st.container(border = True):
        taskR = st.text_input("Task to be removed")
        if st.button("Remove"): 
            if taskR in st.session_state["tasks"]:
                st.session_state["tasks"].remove(taskR)
            st.session_state["mode"] = None
            st.rerun()

if st.session_state["mode"] == "load":
    #check if csv exist before opening to avoid program crash
    if os.path.exists("tasks.csv"):
        st.session_state["tasks"] = []
        with open("tasks.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                st.session_state["tasks"].append(row[0])
        st.success("Previous tasks loaded!")
    else:
            st.warning("No saved task file found.")
    st.session_state["mode"] = None
    st.session_state["loaded"] = True
    st.rerun()

if st.session_state["mode"] == "exit":
    save_tasks()
    st.write("See you next time")

col1, col2, col3, col4 = st.columns(4)
if st.session_state["mode"] == None:
    with col1:
        if st.button("Add task"):
            st.session_state["mode"] = "add"
            st.rerun()
    with col2: 
        if st.button("Remove task"):
            st.session_state["mode"] = "remove"
            st.rerun()
    with col3: 
        if not st.session_state["loaded"]:
            if st.button("Load previous Data"):
                st.session_state["mode"] = "load"     
                st.rerun() 
    with col4:       
        if st.button("Save and exit"):
            st.session_state["mode"] = "exit"
            st.rerun()
            




