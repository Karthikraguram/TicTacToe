import random
def draw_board(board):
	print(board[1]+'|'+board[2]+'|'+board[3])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[7]+'|'+board[8]+'|'+board[9])

def player_choose():
	choice = 'None'
	while choice not in ['X','O']:
		choice = input("Which one do you want to play (X or O): ").capitalize()
		if choice not in ['X','O']:
			print("Wrong! Choose 'X' or 'O'")
	if choice == 'X':
		return ('X','O')
	else:
		return ('O','X')

def player_choice(bd,turn):
	pos = 0
	while not space_check(bd, pos):
		try:
			pos = int(input(turn +"'s turn choose(1-9) : "))
			print('Position already taken!')
		except:
			print('Enter the valid position')
	return pos

def placing(bd,pos,marker):
	bd[pos] = marker

def choose_first():
	if random.randint(0,1) == 0:
		return 'Player1'
	else:
		return 'Player2'

def board_check(board,marker):
	return (board[1]==board[2]==board[3]==marker or board[4]==board[5]==board[6]==marker or board[7]==board[8]==board[9]==marker or board[1]==board[4]==board[7]==marker or board[2]==board[5]==board[8]==marker or board[3]==board[6]==board[9]==marker or board[1]==board[5]==board[9]==marker or board[3]==board[5]==board[7]==marker)

def space_check(bd,pos):
	return bd[pos] == ' '

def draw_check(bd):
	for i in range(1,10):
		if space_check(bd,i):
			return False
	return True

def replay():
	return input('Want to play more (X=No or O=Yes) : ').upper()

print('Welcome to TICTACTOE')
while True:
	bd = [' ']*10
	bd[0] = 'W'
	Player1_marker,Player2_marker = player_choose()
	turn = choose_first()
	print(turn + ' goes First')
	game_on = True
	while game_on:
		if turn == 'Player1':
			pos = player_choice(bd,turn)
			placing(bd,pos,Player1_marker)
			draw_board(bd)
			if board_check(bd,Player1_marker):
				draw_board(bd)
				print(Player1_marker + ' Wins!')
				game_on = False
			else:
				if draw_check(bd):
					draw_board(bd)
					print('Match draw')
					break
				else:
					turn = 'Player2'
		if turn == 'Player2':
			pos = player_choice(bd,turn)
			placing(bd,pos,Player2_marker)
			draw_board(bd)
			if board_check(bd,Player2_marker):
				draw_board(bd)
				print(Player2_marker + ' Wins!')
				game_on = False
			else:
				if draw_check(bd):
					draw_board(bd)
					print('Match draw')
					break
				else:
					turn = 'Player1'
	if replay() == 'X':
		break