import sqlite3
from config import DATABASE
import json

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE (
                          
                        )''') 

            conn.commit()


    def get_recipe_url(self, dish_name):
        sql = "SELECT field1 FROM povarenok_recipes_2021_06_16 WHERE field2 = ?"
        return self.__select_data(sql, (dish_name,))

    def get_ingredients(self, dish_name):
        """Fetch ingredients as a formatted string."""
        sql = "SELECT field3 FROM povarenok_recipes_2021_06_16 WHERE field2 = ?"
        result = self.__select_data(sql, (dish_name,))
        
        if not result:
            return "Ингредиенты не найдены для указанного блюда."

        ingredients_str = result[0][0]  # Assuming the result is a string like "Картофель: 3 шт, Морковь: 1 шт"
        
        # Split the string into individual ingredient items (split by commas)
        ingredients_list = ingredients_str.split(', ')
        
        # Use a for loop to create the formatted output
        formatted_ingredients = ""
        for item in ingredients_list:
            ingredient, quantity = item.split(':')  # Split each item into ingredient and quantity
            formatted_ingredients += f"{ingredient.strip()} : {quantity.strip()}\n"
        
        return formatted_ingredients.strip()  # Remove the trailing newline


    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
            
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
