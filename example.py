# import game class
from crosses_zeroes import CAZ

# create game
# s - board size
# fp - first player; 0 - zeroes, 1 - crosses
game = CAZ(s=3, fp=1)

#restart game
game.restart_game()

#check win; n - none, d - draw, c - crosses, z - zeroes
game.check_win()

#return who win; n - none, d - draw, c - crosses, z - zeroes
game.return_winner()

#return whoes turn; 0 - zeroes; 1 - crosses
game.return_player_turn()

#return game board as list
game.return_gameboard()

#print game board as watchable list
game.print_gameboard()

#add figure; x = {0 : s-1}, y = {0 : s-1}
game.add_fig(x=0, y=0)