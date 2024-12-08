from logic import DB_Manager
from config import *
from telebot import TeleBot

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот-менеджер проектов
Помогу тебе сохранить твои проекты и информацию о них!) 
""")

@bot.message_handler(commands=['find_recipe'])
def find_recipe_command(message):
    msg = bot.send_message(message.chat.id, "Введите название блюда:")
    bot.register_next_step_handler(msg, get_recipe_url)

def get_recipe_url(message):
    dish_name = message.text.strip()
    urls = manager.get_recipe_url(dish_name)

    if urls:
        response = "\n".join([f"🔗 {url[0]}" for url in urls])  # List all URLs if there are multiple
        bot.send_message(message.chat.id, f"Вот рецепт(ы) для {dish_name}:\n{response}")
    else:
        bot.send_message(message.chat.id, f"Рецепт для {dish_name} не найден.")

@bot.message_handler(commands=['get_ingredients'])
def get_ingredients_command(message):
    """Handle the /get_ingredients command."""
    msg = bot.send_message(message.chat.id, "Введите название блюда:")
    bot.register_next_step_handler(msg, fetch_ingredients)


def fetch_ingredients(message):
    """Fetch ingredients for the provided dish name."""
    dish_name = message.text.strip()
    ingredients = manager.get_ingredients(dish_name)
    bot.send_message(message.chat.id, ingredients)


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()