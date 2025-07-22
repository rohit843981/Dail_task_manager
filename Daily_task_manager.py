
tasks =[]
num_tasks = int(input("How many tasks today? "))

for i in range(num_tasks):
    task = input(f"Enter task {i+1}: ")
    tasks.append(task)

completed_tasks = []
incomplete_tasks = []

for task in tasks:
    while True: 
        status = input(f"Did you complete '{task}'? (yes/no): ").lower()
        if status in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")
    if status == 'yes':
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("\n--- Task Summary ---")
print("Completed Tasks:")
if completed_tasks:
    for task in completed_tasks:
        print(f"- {task}")
else:
    print("None")

print("\nIncomplete Tasks:")
if incomplete_tasks:
    for task in incomplete_tasks:
        print(f"- {task}")
else:
    print("None")

with open("task_summary.txt", "w") as f:
    f.write("--- Task Summary ---\n")
    f.write("Completed Tasks:\n")
    if completed_tasks:
        for task in completed_tasks:
            f.write(f"- {task}\n")
    else:
        f.write("None\n")

    f.write("\nIncomplete Tasks:\n")
    if incomplete_tasks:
        for task in incomplete_tasks:
            f.write(f"- {task}\n")
    else:
        f.write("None\n")

print("\nTask summary saved to task_summary.txt")
