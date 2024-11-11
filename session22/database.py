import sqlite3

class Database():
    def __init__(self):
        
        self.con = sqlite3.connect("C:/Users/Dr.Laptop/Desktop/python_class/My_HW/session22/todo_list.db")
        self.cursor = self.con.cursor()


    def get_task(self):

        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks
    
    def add_new_task(self, new_title, new_description, new_date):
        try:
            query = f"INSERT INTO tasks(title, description, date) VALUES ('{new_title}', '{new_description}', '{new_date}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def remove_task(self,title):
        try:
            query = f"DELETE FROM tasks WHERE title ='{title}'"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
         

    def update_task(self, title):
        try:
            query = f"UPDATE tasks SET status = 1 WHERE title ='{title}'"
            self.cursor.execute(query)
            self.con.commit()
            return True

        except:
            return False