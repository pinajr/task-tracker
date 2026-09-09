import sys
import json

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
            }
        }
    )

    # Call the function to write the updated tasks to the JSON file
    write_tasks_to_file()

    print(f"Task added successfully (ID: {id})")

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
    else:
        print('Invalid action. Please use "add" to create a new task.')

main()       
