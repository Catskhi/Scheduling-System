import telebot
from dotenv import load_dotenv
import os

load_dotenv()
api_token = os.getenv('TELEGRAM_TOKEN')
events_channel_id = os.getenv('TELEGRAM_EVENTS_CHANNEL_ID')
admin_channel_id = os.getenv('TELEGRAM_ADMIN_CHANNEL_ID')

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 
        """
            Olá, eu sou o SmithSegTron, estou pronto para te vigiar. 👁️
        """
    )

class SmithSegBot():
    bot = telebot.TeleBot(api_token)
    
    def __init__(self) -> None:
        pass

    @classmethod
    def send_message(self, message) -> None:
        self.bot.send_message(events_channel_id, message, parse_mode='Markdown')

    @classmethod
    def send_admin_message(self, message) -> None:
        self.bot.send_message(admin_channel_id, message, parse_mode='Markdown')


class ReadyMessages():
    def created_event_message(self, owner, title, address, technical, description, date, start_time, end_time):
        message = f"""
        *Novo Evento Criado* 💾 \n                
        """

        message = message + self.event_default_message(owner, title, address, technical, description, date, start_time, end_time)

        return message
    
    def edited_event_message(self, owner, title, address, technical, description, date, start_time, end_time):
        message = f"""
        *Evento Editado* ✏️
        """

        message = message + self.event_default_message(owner, title, address, technical, description, date, start_time, end_time)

        return message

    def edited_event_admin_message(self, owner, edited_by, old_title, old_address, old_technical, old_description, old_date, old_start_time, old_end_time,
                                new_title, new_address, new_technical, new_description, new_date, new_start_time, new_end_time):
        message = f"""
        *Evento Editado* ✏️

Editado por: *{edited_by}*

======================= Antes =======================
"""

        message = message + self.event_default_message(owner, old_title, old_address, old_technical, old_description, old_date, old_start_time, old_end_time)

        message = message + """
======================= Depois =======================      
"""

        message = message + self.event_default_message(owner, new_title, new_address, new_technical, new_description, new_date, new_start_time, new_end_time)

        return message
    
    

    def event_default_message(self, owner, title, address, technical, description, date, start_time, end_time):
        message = f"""
Título: *{title}*
Descrição: \n *{description}*

©️ Autor: *{owner}*
🌎 Endereço: *{address}*
👨‍🔧 Técnico: *{technical}*
📅 Data: *{date}*
🕒 Inicio: *{start_time}*
🕤 Fim: *{end_time}*
"""
        return message