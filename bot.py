import telebot, random
bot = telebot.TeleBot('808136847:AAHLq-11VcMuPKWZvStE60_-0MgRg_Lqabs')
isRunning = False

@bot.message_handler(commands=['start', 'go'])

def start(message):
    global isRunning
    if not isRunning:
        isRunning = True
        bot.send_message(message.from_user.id, 'Now your are going to play KRESTIKI NOLIKI with the most powerfull AI in the UNIRVERSE. Be prepared and try not to shit your pants')
        bot.send_message(message.from_user.id, "Please choose a marker 'X' or 'O'")
        bot.register_next_step_handler(message, game)

@bot.message_handler(content_types=['text', 'document', 'audio', 'photo'])
     
def game(message):
    global player1, player2, numbers
    if message.text.upper() == "X" or message.text.upper() == "O":
        player1 = message.text.upper()
        
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        bot.send_message(message.from_user.id, f'Great choice, looser! Now the GAME begins! Choose from 1 to 9 to place your {player1} sign')
        numbers = [1,2,3,4,5,6,7,8,9]
        n = 0
        while n <= 6:
            pole = {1: '|          |          |          |',
                2: '-------------------', 3: 
                '|{:^9}|{:^9}|{:^9}|'.format(numbers[n], numbers[n + 1], numbers[n + 2])}
            if n == 6:
                bot.send_message(message.from_user.id, pole[3])
            else:
                bot.send_message(message.from_user.id, pole[3])
                #bot.send_message(message.from_user.id, pole[2])
            n += 3
        numbers =[' ']*9
        bot.send_message(message.from_user.id,'If you are ready to start, Player1, please, enter the number where you want to put your {}\n'.format(player1))
        bot.register_next_step_handler(message, game1)
    
    elif message.text == '/Start':
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.from_user.id, 'Wrong input, please try again')
        bot.register_next_step_handler(message, game)
    
def game1(message):
    global numbers, player1, player2
    n = 0
    
    if message.text == '/Start':
        bot.register_next_step_handler(message, start)
        
    position = int(message.text)
        
    if int(message.text) > 9 or int(message.text) < 1:
        bot.send_message(message.from_user.id, 'Wrong input, please try again')
        bot.register_next_step_handler(message, game1)
    
    elif numbers[position - 1] == player1 or numbers[position - 1] == player2:
        bot.send_message(message.from_user.id, 'The CELL is already BUSY, you IDIOT! Again!')
        bot.register_next_step_handler(message, game1)
    
    else:
        numbers.pop(position - 1)
        numbers.insert(position - 1, player1)

        while n <= 6:
            pole = {1: '|          |          |          |',
            2: '-------------------', 3: 
            '|{:^9}|{:^9}|{:^9}|'.format(numbers[n], numbers[n + 1], numbers[n + 2])}
            if n == 6:
                bot.send_message(message.from_user.id, pole[3])
            else:
                bot.send_message(message.from_user.id, pole[3])
                #bot.send_message(message.from_user.id, pole[2])
            n += 3
        if (numbers[0] + numbers[1] + numbers[2] == player1 * 3) or\
            (numbers[3] + numbers[4] + numbers[5] == player1 * 3) or\
            (numbers[6] + numbers[7] + numbers[8] == player1 * 3) or\
            (numbers[0] + numbers[3] + numbers[6] == player1 * 3) or\
            (numbers[1] + numbers[4] + numbers[7] == player1 * 3) or\
            (numbers[2] + numbers[5] + numbers[8] == player1 * 3) or\
            (numbers[0] + numbers[4] + numbers[8] == player1 * 3) or\
            (numbers[2] + numbers[4] + numbers[6] == player1 * 3):
            bot.send_message(message.from_user.id,'Congratulations! You are GENIUS! Want to play again?')
            bot.register_next_step_handler(message, start)
        elif numbers.count(' ') == 0:
            bot.send_message(message.from_user.id,'Parity! Want to play again? Yes / No')
            bot.register_next_step_handler(message, other)
            
        else:
            bot.send_message(message.from_user.id,"Now, AI will make it's turn. Wait and shake, human!")

            n = 0
    
            if numbers[4] == ' ':
                position2 = 5

            elif numbers[0] == player2 and numbers[2] == player2 and numbers[1] == ' ':
                position2 = 2
            elif numbers[0] == player2 and numbers[6] == player2 and numbers[3] == ' ':
                position2 = 4
            elif numbers[2] == player2 and numbers[8] == player2 and numbers[5] == ' ':
                position2 = 6
            elif numbers[6] == player2 and numbers[8] == player2 and numbers[7] == ' ':
                position2 = 8
            elif numbers[0] == player2 and numbers[4] == player2 and numbers[8] == ' ':
                position2 = 9
            elif numbers[8] == player2 and numbers[4] == player2 and numbers[0] == ' ':
                position2 = 1
            elif numbers[2] == player2 and numbers[4] == player2 and numbers[6] == ' ':
                position2 = 7
            elif numbers[6] == player2 and numbers[4] == player2 and numbers[2] == ' ':
                position2 = 3
            elif numbers[3] == player2 and numbers[4] == player2 and numbers[5] == ' ':
                position2 = 6
            elif numbers[5] == player2 and numbers[4] == player2 and numbers[3] == ' ':
                position2 = 4
            elif numbers[1] == player2 and numbers[4] == player2 and numbers[7] == ' ':
                position2 = 8
            elif numbers[7] == player2 and numbers[4] == player2 and numbers[1] == ' ':
                position2 = 2
            elif numbers[0] == player2 and numbers[1] == player2 and numbers[2] == ' ':
                position2 = 3
            elif numbers[1] == player2 and numbers[2] == player2 and numbers[0] == ' ':
                position2 = 1
            elif numbers[0] == player2 and numbers[3] == player2 and numbers[6] == ' ':
                position2 = 7
            elif numbers[6] == player2 and numbers[3] == player2 and numbers[0] == ' ':
                position2 = 1
            elif numbers[2] == player2 and numbers[5] == player2 and numbers[8] == ' ':
                position2 = 9
            elif numbers[8] == player2 and numbers[5] == player2 and numbers[2] == ' ':
                position2 = 3
            elif numbers[6] == player2 and numbers[7] == player2 and numbers[8] == ' ':
                position2 = 9
            elif numbers[7] == player2 and numbers[8] == player2 and numbers[6] == ' ':
                position2 = 7

            elif numbers[0] == player1 and numbers[8] == player1 and numbers[4] == player2 and numbers[1] == ' ':
                position2 = 2
            elif numbers[0] == player1 and numbers[8] == player1 and numbers[4] == player2 and numbers[3] == ' ':
                position2 = 4
            elif numbers[0] == player1 and numbers[8] == player1 and numbers[4] == player2 and numbers[5] == ' ':
                position2 = 6
            elif numbers[0] == player1 and numbers[8] == player1 and numbers[4] == player2 and numbers[7] == ' ':
                position2 = 8
            elif numbers[2] == player1 and numbers[6] == player1 and numbers[4] == player2 and numbers[1] == ' ':
                position2 = 2
            elif numbers[2] == player1 and numbers[6] == player1 and numbers[4] == player2 and numbers[3] == ' ':
                position2 = 4
            elif numbers[2] == player1 and numbers[6] == player1 and numbers[4] == player2 and numbers[5] == ' ':
                position2 = 6
            elif numbers[2] == player1 and numbers[6] == player1 and numbers[4] == player2 and numbers[7] == ' ':
                position2 = 8
            elif numbers[0] == player1 and numbers[2] == player1 and numbers[1] == ' ':
                position2 = 2
            elif numbers[0] == player1 and numbers[6] == player1 and numbers[3] == ' ':
                position2 = 4
            elif numbers[2] == player1 and numbers[8] == player1 and numbers[5] == ' ':
                position2 = 6
            elif numbers[6] == player1 and numbers[8] == player1 and numbers[7] == ' ':
                position2 = 8
            elif numbers[0] == player1 and numbers[4] == player1 and numbers[8] == ' ':
                position2 = 9
            elif numbers[8] == player1 and numbers[4] == player1 and numbers[0] == ' ':
                position2 = 1
            elif numbers[2] == player1 and numbers[4] == player1 and numbers[6] == ' ':
                position2 = 7
            elif numbers[6] == player1 and numbers[4] == player1 and numbers[2] == ' ':
                position2 = 3
            elif numbers[3] == player1 and numbers[4] == player1 and numbers[5] == ' ':
                position2 = 6
            elif numbers[5] == player1 and numbers[4] == player1 and numbers[3] == ' ':
                position2 = 4
            elif numbers[1] == player1 and numbers[4] == player1 and numbers[7] == ' ':
                position2 = 8
            elif numbers[7] == player1 and numbers[4] == player1 and numbers[1] == ' ':
                position2 = 2
            elif numbers[0] == player1 and numbers[1] == player1 and numbers[2] == ' ':
                position2 = 3
            elif numbers[1] == player1 and numbers[2] == player1 and numbers[0] == ' ':
                position2 = 1
            elif numbers[0] == player1 and numbers[3] == player1 and numbers[6] == ' ':
                position2 = 7
            elif numbers[6] == player1 and numbers[3] == player1 and numbers[0] == ' ':
                position2 = 1
            elif numbers[2] == player1 and numbers[5] == player1 and numbers[8] == ' ':
                position2 = 9
            elif numbers[8] == player1 and numbers[5] == player1 and numbers[2] == ' ':
                position2 = 3
            elif numbers[6] == player1 and numbers[7] == player1 and numbers[8] == ' ':
                position2 = 9
            elif numbers[7] == player1 and numbers[8] == player1 and numbers[6] == ' ':
                position2 = 7
            elif numbers[1] == ' ':
                position2 = 2
            elif numbers[3] == ' ':
                position2 = 4
            elif numbers[5] == ' ':
                position2 = 6
            elif numbers[7] == ' ':
                position2 = 8
            elif numbers[0] == ' ':
                position2 = 1
            elif numbers[2] == ' ':
                position2 = 3
            elif numbers[6] == ' ':
                position2 = 7
            elif numbers[8] == ' ':
                position2 = 9
                
            numbers.pop(position2 - 1)
            numbers.insert(position2 - 1, player2)

            while n <= 6:
                pole = {1: '|          |          |          |',
                2: '-------------------', 3: 
                '|{:^9}|{:^9}|{:^9}|'.format(numbers[n], numbers[n + 1], numbers[n + 2])}
                if n == 6:
                    bot.send_message(message.from_user.id, pole[3])
                else:
                    bot.send_message(message.from_user.id, pole[3])
                    #bot.send_message(message.from_user.id, pole[2])
                n += 3

            if (numbers[0] + numbers[1] + numbers[2] == player2 * 3) or\
                (numbers[3] + numbers[4] + numbers[5] == player2 * 3) or\
                (numbers[6] + numbers[7] + numbers[8] == player2 * 3) or\
                (numbers[0] + numbers[3] + numbers[6] == player2 * 3) or\
                (numbers[1] + numbers[4] + numbers[7] == player2 * 3) or\
                (numbers[2] + numbers[5] + numbers[8] == player2 * 3) or\
                (numbers[0] + numbers[4] + numbers[8] == player2 * 3) or\
                (numbers[2] + numbers[4] + numbers[6] == player2 * 3):
                bot.send_message(message.from_user.id,'Congratulations! You are an IDIOT! Want to play again?')
                bot.register_next_step_handler(message, start)
            elif numbers.count(' ') == 0:
                bot.send_message(message.from_user.id,'Parity! Want to play again? Yes / No')
                bot.register_next_step_handler(message, other)
            else:
                bot.send_message(message.from_user.id,"Please input the number where you want to put {}".format(player1))
                bot.register_next_step_handler(message, game1)
                
def other(message):
    isRunning = False
    if message.text.lower() == 'no':
        bot.send_photo(message.from_user.id, '**SUICIDE**')
    else:
        bot.register_next_step_handler(message, start)

bot.polling(none_stop=True)