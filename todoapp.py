#TO DO app; create task, mark the task as complete, edit task

from asyncio import tasks
import psycopg2
import os
from psycopg2 import OperationalError, sql
from dotenv import load_dotenv

load_dotenv()

def connect():
    try:
        #print("Connected to the database")
        return psycopg2.connect(
        host=os.getenv('HOSTNAME'),
        database=os.getenv('DATABASE'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        port=os.getenv('PORT')
        )
       
    except OperationalError as e:
        print(f"Unable to connect to the database: {e}")
conn = connect()
#print(conn)


#create table 
def create_table():
    conn = psycopg2.connect(database="tododb")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE tasks (id SERIAL PRIMARY KEY, task VARCHAR(255), status boolean default false)',)
    conn.commit()
    cursor.close()

# #add task
def add_task(tasks):
    conn = connect()
    if not conn:
        return "missing credentials",401
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks VALUES (default, %s)', (tasks,))
    conn.commit()
    cursor.close()
    conn.close()
# add_task('learn python')

def update_task(task_id):
    conn = connect()
    if not conn:
        return "missing credentials",401
    
    cursor = conn.cursor()
    try:
      # Update the status of the task
        update_query = 'UPDATE tasks SET status = %s WHERE id = %s'
        cursor.execute(update_query, (True, task_id))
        
        # Commit the transaction
        conn.commit()
        
        # Check if the update was successful
        check_query = 'SELECT status FROM tasks WHERE id = %s'
        cursor.execute(check_query, (task_id,))
        
        # Fetch the updated status
        result = cursor.fetchone()
        
        if result:
            updated_status = result[0]
            if updated_status == True:
                print(f"Task {task_id} successfully marked as completed.")
            else:
                print(f"Failed to mark task as completed. Current status: {updated_status}")
        else:
            print("Task not found")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()
#done = update_task(1)

def display_tasks():
    conn = connect()
    if not conn:
        return "missing credentials",401
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    for row in rows:
        print(f'Task ID: {row[0]}, Task: {row[1]}, Status: {row[2]}')
    cursor.close()
#dis = (display_tasks)

def main():
    conn = connect()
    while True:
        try:
            print("\nChoose an option:")
            print("1. Add task")
            print("2. Mark task as complete")
            print("3. Display tasks")
            print("4. Exit")

            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                task = input("Enter the task: ")
                add_task(task)
            elif choice == 2:
                taskid = input("Enter the task ID: ")
                update_task(taskid)
            elif choice == 3:
                display_tasks()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

