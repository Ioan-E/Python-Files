from time import time
import datetime
import random
import logging

logging.basicConfig(level = logging.DEBUG, filename = 'logging.log')
logger = logging.getLogger(__name__)

logger.debug('Game Started')

class PrittyPrinterMixin:

    def __str__(self):

        print_view = f'\n***********************************'
        print_view += f'\n*** Player\'s name: {self.get_name()} ***\n'
        for info,detail in self.player_info.items():
            print_view += f'\n{info}: {detail}' + '\n'    
        print_view += f'\n***********************************\n'
        return (print_view)



class Players(PrittyPrinterMixin):
    def __init__(self,gamer_name, player_info):
        self.gamer_name = gamer_name
        self.player_info = player_info
        
    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f'{self.gamer_name},{self.player_info}, id:{id(self)}'

    def get_name(self):
        return self.gamer_name

    def __len__(self):
        return len(self.player_info)

    def __getitem__(self,index):
        return self.player_info[index]

    def __contains__(self,info):
        return info in self.player_info

    def __iter__(self):
        return iter(self.player_info)

    def keys(self):
        return self.player_info.keys()

    def items(self):
        return self.player_info.items()

    def values(self):
        return self.player_info.values()

    def __eq__(self,other):
        return self.player_info["credit"] == other.player_info["credit"]

    def __lt__(self,other):
        return self.player_info["credit"] < other.player_info["credit"]

    def __le__(self,other):
        return self.player_info["credit"] <= other.player_info["credit"]

    def __ge__(self,other):
        return self.player_info["credit"] >= other.player_info["credit"]

    def __gt__(self,other):
        return self.player_info["credit"] > other.player_info["credit"]


class TableOfPlayers():
    def __init__(self):
        self.players_list = {}

    def __str__(self):
        return (f'Table contains the following players: {list(self.players_list.keys())}')

    def __repr__(self):
        return (f'{list(self.players_list.keys())}')

    def __len__(self):
        return len(self.players_list)

    def __contains__(self,player):
        return player in self.players_list

    def __iter__(self):
        return iter(self.players_list)

    def __setitem__(self,index, newplayer):
       self.players_list[index] = newplayer

    def __delitem__(self,player):
        del self.players_list[player]

    def __getitem__(self,index):
        return self.players_list[index]

    def keys(self):
        return self.players_list.keys()

    def values(self):
        return self.players_list.values()

    def items(self):
        return self.players_list.items()

    def add_player(self,player):
        logging.debug(f'Adding player {player.gamer_name}')
        self.players_list[player.gamer_name] = player.player_info
        print(f'Adding player {player.gamer_name} to the Table.')

    def remove_player(self,player):
        logging.debug(f'Removing player {player.gamer_name}')
        del self.players_list[player.gamer_name]
        print(f'Removing player {player.gamer_name} from the Table.')

        
    
rules='''Welcome to Roulette!  
        In this game, you have a wheel that features red and black slots
        that have the numbers from 1 to 36 on them. 
        Except for the wheel, you have a table which also features the numbers and several 
        additional sectors on which you can place bets. After you place your bet, the table 
        will generate a random winning number (and color), and we will compare it with your bet. '''

betting_options='''Betting options:
            1: on any number between 1-36 
            2: by color (red/black) 
            3: even / odd number
            4: low / high bet'''

winning_rules='''Winning rules:
            Case 1: 100% bonus of the amount he was betting.
            Case 2 and 3: 50% bonus of the amount he was betting. 
            Case 4: 30% bonus of the amount he was betting. 
            If the table wins, the player will loose the amount he was betting.'''



def betting_params(type,value):
    options = [
        {'question':'What number? (1-36) ---> ', 'error_msg':'Invalid number'},
        {'question':'What color? (red/black) ---> ', 'error_msg':'Invalid color'},
        {'question': 'Even or odd? ---> ', 'error_msg': 'Invalid option'},
        {'question': 'Low (1-18) or high (19-36) bet? (low/high) ---> ', 'error_msg': 'Invalid option'}
    ]
    return options[type-1][value]    

def betting_params_validation(type):
    logging.debug('Validating players option')
    try:
        if 0 < int(type) < 5:
            return True
        else:
            return 'Option not between 1-4'    
    except ValueError:    
        return 'Option is not an integer'

def validate_number(number,type):
    logging.debug('Validating players choice')
    try:
        if type == 1 and 0 < int(number) < 37:
            return True
        elif number.upper() in ('RED','BLACK','EVEN','ODD','LOW','HIGH'):
            return True
        else:
            return False
    except ValueError:
        return 'Option invalid'
        
def validate_bet_amount(amount, player, credit):
    logging.debug(f'Validating {player.gamer_name}\'s betting amount')
    try:
        if 0 < int(amount) <= credit:
            return True
        else:
            return 'Not enogh credit'
    except ValueError:
        return 'This is not a number.'

def generate_random():
    logging.info('Generating the random number and color')
    random_nr = random.randint(1,36)
    random_color = random.choice(['RED','BLACK'])
    return (random_nr, random_color)

def compare_numbers(player_nr, cpu_nr, type):
    logging.info('Comparing players and tables numbers')
    if type == 1:
        return int(player_nr) == cpu_nr[0]
    elif type == 2:
        return player_nr == cpu_nr[1]
    elif type == 3:
        return True if (cpu_nr[0]%2 == 0 and player_nr=='EVEN') or (cpu_nr[0]%2!=0 and player_nr=='ODD') else False
    elif type == 4:
        return True if (1<=cpu_nr[0]<19 and player_nr=='LOW') or (19<=cpu_nr[0]<37 and player_nr=='HIGH') else False

def no_more_credit(credit):
    exit = False
    if credit == 0:
        print('You lost your credits. Have a good day')
        exit = True
    return exit

def winning(type,amount):
    if type == 1:
        sum = amount 
    elif type == 2:
        sum = amount*0.5
    elif type == 3:
        sum = amount*0.5 
    elif type == 4:
        sum = round(amount*0.3)
    return sum

def exit_betting():
    logging.info('Checking if the player wants to leave')
    answer = ''
    while answer not in ['Y', 'N']:    
        answer = input('Do you want to continue? (Y/N) --->').upper()
        if  answer == 'N':
            return True
        elif answer == 'Y':
            return False


all_time_scores = []

def roulette(players):

    print(rules)        
    print(betting_options)
    print(winning_rules)
    
    play_game = True

    while play_game:

        for index, player in enumerate(players):
              
            credit = player["credit"]
            player_option = None
            player_choice = None
            bet_amount = None

            logging.info(f'Playing with player {player.gamer_name}')
            print(f'Playing with player {player.gamer_name}...')
            
            while True:
                logging.debug(f'Asking player {player.gamer_name} for a betting option')
                player_option = input('Which option you choose to bet? (1-4) ---> ')
                validation = betting_params_validation(player_option)
                if validation != True:
                    print(validation)
                else:
                    break

            player_option = int(player_option)
            
            while True:
                logging.debug(f'Asking player {player.gamer_name} for a playing choice')
                player_choice = (input(betting_params(player_option,'question'))).upper()
                if validate_number(player_choice, player_option) != True:
                    print(betting_params(player_option,'error_msg'))
                else:
                    break
            
            while True:
                logging.debug(f'Asking player {player.gamer_name} for a betting amount')
                bet_amount = input(f'How much credit you want to bet on this number? You have: {credit} left. ---> ')
                validate_bet = validate_bet_amount(bet_amount, player, credit)
                if validate_bet != True:
                    print(validate_bet)
                else:
                    break
            
            bet_amount = int(bet_amount)

            players[index].player_info['credit'] = credit
            players[index].player_info['player_option'] = player_option
            players[index].player_info['player_choice'] = player_choice
            players[index].player_info['bet_amount'] = bet_amount        
        
        tables_number = generate_random()

        remained_players = []
        for index, player in enumerate(players):       
            player_choice = player['player_choice']
            player_option = player['player_option']
            credit = player['credit']
            bet_amount = player['bet_amount']
            if compare_numbers(player_choice, tables_number, player_option):
                print(f'{player.gamer_name} you WON!!! The number was {tables_number}, your bet was {player_choice} ')
                credit += winning(player_option,bet_amount)
                players[index].player_info['credit'] = credit      
            else:
                print(f'{player.gamer_name} you LOST!!! The number was {tables_number}, your bet was {player_choice}')
                credit -= bet_amount
                players[index].player_info['credit'] = credit
            
            if player not in all_time_scores:
                all_time_scores.append(player)
            else:
                player.player_info["credit"] = credit

            if no_more_credit(credit):
                remove_player = True
            else:
                logging.info(f'Asking player {player.gamer_name} if they want to leave the table')
                remove_player = exit_betting()
                
            if not remove_player:
                remained_players.append(players[index]) 

        players = remained_players
        if not players:
            logging.info('No more players')
            print('All the players have left the table')
            play_game = False

class TimeIt:
    def __init__(self,players):
        self.players = players
    
    def __enter__(self):
        logging.info('Starting the cronometer')
        print('Start game timing')
        self.start = time()
        self.log_file = open('scores.txt','w')
        self.log_file.write(f'Players credits BEFORE playing roulette: '+'\n')
        logging.debug('Writing out the players and credits before playing the game')
        for player in self.players:
            self.log_file.write(f'\nPlayer: {player.gamer_name} CREDIT: {player.player_info["credit"]}\n')  
        self.log_file.write('*'*30)
    
    def __exit__(self,type,value,traceback):
        self.stop = time()
        logging.info('Stopping the cronometer')
        print(f'Game duration is: {round((self.stop-self.start),2)} seconds')
        self.log_file.write('\nPlayers credits AFTER playing roulette:'+'\n')
        logging.debug('Writing out the players and credits after playing the game')
        for player in self.players:
            self.log_file.write(f'\nPlayer: {player.gamer_name} NEW-CREDIT: {player.player_info["credit"]}\n')

