import logging
import random

logging.basicConfig(filename='game.log', level=logging.DEBUG)

CELLS = [(0,0), (0,1), (0,2),
         (1,0), (1,1), (1,2),
         (2,0), (2,1), (2,2)]


def get_locations():

    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)
    if monster == door or monster == start or door == start:
        return get_locations()
    return monster, door, start


def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    if move == 'UP':
        x -= 1
    if move == 'DOWN':
        x += 1
    player = x, y
    return player


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', "DOWN"]
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')
    return moves


def draw_map(player):
    print(' _ _ _')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))


monster, door, player = get_locations()
logging.info("monster: {}, door: {}, player: {}".format(monster, door, player))

print('Welcome to the dungeon!\n')


while True:
    moves = get_moves(player)
    print("You're currently in room {}.\n You can move {}\n".format(player, moves),
          "Enter QUIT to quit")  # Fill in with player position and available moves
    draw_map(player)
    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break
    if move in moves:
        player = move_player(player, move)
    else:
        print("**Bad move!**")
        continue

    if player == door:
        print("You escaped!")
        break
    elif player == monster:
        print("You were eaten by the monster :(")
        break


#########################################################################################
# my_list = list('abcdefg')
# my_num = 6
#
# def nchoices(my_list, num):
#     random_list = []
#     for n in range(num):
#         random_thing = random.choice(my_list)
#         random_list.append(random_thing)
#     print(random_list)
#
# nchoices(my_list, my_num)
