from application import PrittyPrinterMixin, Players, TableOfPlayers, rules, betting_options, winning_rules, betting_params, \
                        betting_params_validation, validate_number, validate_bet_amount, generate_random, compare_numbers, \
                        no_more_credit, winning, exit_betting, all_time_scores, roulette, TimeIt

player1_info = {'name':'Mick Jager', 'age': 35, 'credit':1000}
player2_info = {'name':'George Drag', 'age': 30, 'credit':800}
player3_info = {'name':'Jack Daniels', 'age': 38, 'credit':1200}
player4_info = {'name':'Julius Caesar', 'age': 60, 'credit':500}
player5_info = {'name':'John Doe', 'age': 25, 'credit':700}

player1 = Players('Lucky Mike', player1_info)
player2 = Players('Drag X', player2_info)
player3 = Players('Jacky 8', player3_info)
player4 = Players('Imperator', player4_info)
player5 = Players('Johnny D', player5_info)

print(player1)
# print(repr(player1))
# print(player2)
# print(repr(player2))
# print(player3)
# print(repr(player3))
# print(player4)
# print(repr(player4))
# print(player5)
# print(repr(player5))


# print(player1['age'])


# players_list = TableOfPlayers()
# players_list.add_player(player1)
# players_list.add_player(player2)
# players_list.add_player(player3)
# players_list.add_player(player4)
# players_list.add_player(player5)

# print(players_list)
# players_list.remove_player(player5)
# print(players_list)
# print(len(players_list))


# players = [player1, player2, player3, player4, player5]
players = [player1, player2]


with TimeIt(players):
    roulette(players)


