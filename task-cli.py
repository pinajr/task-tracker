import sys
import json
import datetime

# Store the arguments passed to the script
command_action = sys.argv[1]
argument_1 = sys.argv[2]
argument_2 = sys.argv[3] if len(sys.argv) > 3 else None

# Function that create a new task
def create_task(description):
    # Get the next available task ID
    id = max(all_tasks.keys(), default=0) + 1

    # Add the new task to the all_tasks dictionary
    all_tasks.update(
        {
            id: {
                'description': description,
                'status': "to-do",
                'createdAt': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'updateAT': None
            }
        }
    )

    # Call the function to write the updated tasks to the JSON file
    write_tasks_to_file()

    print(f"Task added successfully (ID: {id})")

# Function that update a task
def update_task(id, description):
    load_tasks()  # Load the tasks from the JSON file
    if id in all_tasks.keys():
        all_tasks[id]['description'] = description
        all_tasks[id]['updateAT'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        write_tasks_to_file()  # Call the function to write the updated tasks to the JSON file
    else:
        print(f"Task with ID {id} not found.")

# Function that delete a task
def delete_task(id):
    load_tasks() # Load the tasks from the JSON file

    if id in all_tasks.keys():
        del all_tasks[id]  # Delete the task from the all_tasks dictionary
        write_tasks_to_file()  # Call the function to write the updated tasks to the JSON file
    else:
        print(f"Task with ID {id} not found.")

# Function to change the status of a task
def change_task_status(id, status):
    load_tasks()  # Load the tasks from the JSON file

    if id in all_tasks.keys():
        all_tasks[id]['status'] = status
        all_tasks[id]['updateAT'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        write_tasks_to_file()  # Call the function to write the updated tasks to the JSON file
    else:
        print(f"Task with ID {id} not found.")

# Save the updated tasks to the JSON file
def write_tasks_to_file():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(all_tasks, file, indent=4)

# Load the tasks from the JSON file
def load_tasks():
    global all_tasks

    with open("tasks.json", "r", encoding="utf-8") as file:
        all_tasks = json.load(file)

    # Convert the keys of the all_tasks dictionary to integers
    all_tasks = {int(key): value for key, value in all_tasks.items()}

def main():
    # Call the function to load tasks from the JSON file
    load_tasks()

    if command_action == 'add':
        description = argument_1
        create_task(description)

    elif command_action == 'update':
        id = int(argument_1)
        description = argument_2 
        update_task(id, description)

    elif command_action == 'delete':
        id = int(argument_1)
        delete_task(id)
    elif command_action == 'make-in-progress' or command_action == 'make-done':
        id = int(argument_1)

        # Determine the new status based on the command action
        if command_action == 'make-in-progress':
            status = 'in-progress'
        else:
            status = 'done'
        
        change_task_status(id, status)
    else:
        print('Invalid action. Please use "add" to create a new task.')

main()       
