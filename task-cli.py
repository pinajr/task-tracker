import sys

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

    print(f"Task added successfully (ID: {id}) {description}")

def main():
    global all_tasks
    all_tasks = {}

    if command_action == 'add':
        description = argument_1
        create_task(description)
    else:
        print('Invalid action. Please use "add" to create a new task.')

main()       
