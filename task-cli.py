import sys
import json
import datetime

# Function that create a new task
def create_task(description):
    # Get the next available task ID
    id = max(all_tasks.keys(), default=0) + 1

    # Add the new task to the all_tasks dictionary
    all_tasks.update(
        {
            id: {
                'description': description,
                'status': "todo",
                'createdAt': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'updateAt': None
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
        all_tasks[id]['updateAt'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
        all_tasks[id]['updateAt'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Call the function to write the updated tasks to the JSON file
        write_tasks_to_file()  
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
    # Store the arguments passed to the script
    if len(sys.argv) == 1:
        print(
            'No action provided. Please use: \n - add \n - update \n - delete \n ' \
            '- make-in-progress \n - make-done \n - list to modify tasks.'
            )
        return
    else:
        command_action = sys.argv[1]

    # Call the function to load tasks from the JSON file
    load_tasks()

    if len(sys.argv) < 3 and 'list' not in command_action:
        print('Insufficient arguments provided. Please provide the necessary arguments.')
    elif len(sys.argv) > 3 and 'update' not in command_action:
        print('Too many arguments provided. Please provide the necessary arguments.')
    else:
        if command_action == 'add':
            description = sys.argv[2]
            create_task(description)
        elif command_action == 'update':
            if len(sys.argv) < 4:
                print(
                    'Insufficient arguments provided for update. Please provide the ' \
                    'task ID and new description.'
                )
                return
            elif sys.argv[2].isdigit() is False:
                print('Invalid task ID. Please provide a valid integer ID.')
                return
            
            id = int(sys.argv[2])
            description = sys.argv[3]
            update_task(id, description)
        elif command_action == 'delete':
            if sys.argv[2].isdigit() is False:
                print('Invalid task ID. Please provide a valid integer ID.')
                return
            id = int(sys.argv[2])
            delete_task(id)
        elif command_action == 'make-in-progress' or command_action == 'make-done':
            if sys.argv[2].isdigit() is False:
                print('Invalid task ID. Please provide a valid integer ID.')
                return
            id = int(sys.argv[2])

            # Determine the new status based on the command action
            if command_action == 'make-in-progress':
                status = 'in-progress'
            else:
                status = 'done'
            
            change_task_status(id, status)
        elif command_action == 'list':
            # Check if a filter argument is provided
            if len(sys.argv) > 2:
                # Filter the tasks based on the provided argument
                if sys.argv[2] == 'done':
                    # Print the list of done tasks
                    print("List of done tasks:")
                    for id, value in all_tasks.items():
                        if value['status'] == 'done':
                            print(f"Task: {id} - {value['description']}")
                elif sys.argv[2] == 'todo':
                    # Print the list of to-do tasks
                    print("List of to-do tasks:")
                    for id, value in all_tasks.items():
                        if value['status'] == 'todo':
                            print(f"Task: {id} - {value['description']}")
                elif sys.argv[2] == 'in-progress':
                    # Print the list of in-progress tasks
                    print("List of in-progress tasks:")
                    for id, value in all_tasks.items():
                        if value['status'] == 'in-progress':
                            print(f"Task: {id} - {value['description']}")
                else:
                    print('Invalid argument. Please use "done", "todo", or ' \
                    '"in-progress" to filter tasks.'
                    )
            elif len(sys.argv) == 2:
                # Print the list of tasks
                print("List of all tasks:")
                for id, value in all_tasks.items():
                    print(f"Task: {id} - {value['description']}")
            else:
                print('Invalid action. Please use "list" to view tasks.')
        else:
            print(
                'Invalid action. Please use "add", "update", "delete", ' \
                '"make-in-progress", or "make-done" to modify tasks.'
                )

main()
