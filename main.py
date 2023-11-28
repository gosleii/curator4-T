import telebot

bot = telebot.TeleBot('6525649843:AAHzYx7SUSELE6BnXLNWTwJd1jSkiQkT28A')

START_MESSAGE = 'Привет, это бот - калькулятор. Он может производить простые математические оперции: складывать, вычетать, умножать и делить.'

@bot.message_handler(commands=['start'])
def main(message):
    numone = bot.send_message(message.chat.id, f'{START_MESSAGE} \n\nВведи первое число')
    bot.register_next_step_handler(numone, num1_fun)

def num1_fun(message):
    global num1
    num1 = message.text
    numtwo = bot.send_message(message.chat.id, 'Введи второе число')
    bot.register_next_step_handler(numtwo, num2_fun)

def num2_fun(message):
    global num2
    num2 = message.text
    operation = bot.send_message(message.chat.id, 'Введите действие: +, -, * или /')
    bot.register_next_step_handler(operation, action)

def action(message):
    global oper
    oper = message.text
    if oper == '+':
        result = int(num1) + int(num2)
        bot.send_message(message.chat.id, f'{result}. Чтобы начать сначала, напиши /start')
    elif oper == '-':
        result = int(num1) - int(num2)
        bot.send_message(message.chat.id, f'{result}. Чтобы начать сначала, напиши /start')
    elif oper == '*':
        result = int(num1) * int(num2)
        bot.send_message(message.chat.id, f'{result}. Чтобы начать сначала, напиши /start')
    elif oper == '/':
        result = int(num1) / int(num2)
        bot.send_message(message.chat.id, f'Результат: {int(result)} \n\nЧтобы начать сначала, напиши /start')
    else:
        bot.send_message(message.chat.id, 'Ошибка. Чтобы начать сначала, напиши /start')

bot.infinity_polling()
