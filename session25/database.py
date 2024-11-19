import sqlite3

class DatabaseManager:
    def __init__(self):
      
      self.con = sqlite3.connect("C:/Users/Dr.Laptop/Desktop/python_class/My_HW/session25/alarms.db")
      self.cursor = self.con.cursor()

    def add_alarm(self, hour, minute, text):
        try:

            self.cursor.execute("INSERT INTO alarms (hour, minute, text) VALUES (?, ?, ?)", (hour, minute, text))
            self.con.commit()
            return True

        except:
            return False
        

    def get_alarms(self):
        
        result =self.cursor.execute("SELECT * FROM alarms")
        alarms = result.fetchall()
        
        return alarms

    def update_alarm(self, alarm_id, new_hour, new_minute, new_text):

        self.cursor.execute("UPDATE alarms SET hour = ?, minute= ?, text = ? WHERE id = ?", (new_hour, new_minute,new_text, alarm_id))
        self.con.commit()
        

    def delete_alarm(self, alarm_id):
        self.cursor.execute("DELETE FROM alarms WHERE id = ?", (alarm_id,))
        self.con.commit()
        
