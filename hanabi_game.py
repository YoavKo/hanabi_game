from random import shuffle
from pprint import pprint

NUMBER_OF_PLAYERS = 3
NUMBER_OF_CARDS = 5
def deck_generate():
    deck = []
    colors = ["B", "R", "G", "Y", "W"] 
                            # "B"=blue, "R"=red, "G"=green, "Y"=yeloow, "W"=white
    numbers =  [["1", 3],   #[label, quantity]
                ["2", 2],
                ["3", 2],
                ["4", 2], 
                ["5", 1]]

    for color in colors:
        for number in numbers:
            for i in xrange(number[1]):
                deck.append(color+number[0])

    return deck

deck = deck_generate()
shuffle(deck)

players = []
for player in xrange(NUMBER_OF_PLAYERS):
    players.append({'Cards' : [], 'Clues' : [],})
    for card in xrange(NUMBER_OF_CARDS):
        players[player]['Cards'].append(deck.pop())
        players[player]['Clues'].append("")

#pprint(players[1:])
#pprint(deck)

def print_bord():
    pprint(players[1:])

poz ={'c':0,'n':1}

while True:
    print_bord()
    cmd = raw_input("Enter clue:[player,card,n/c]")
    cmd = cmd.split(",")
    pprint(cmd)
    data = players[int(cmd[0])]['Cards'][int(cmd[1])][poz[cmd[2]]]
    for card in players[int(cmd[0])]['Cards']:
        if data in card:
            print card
