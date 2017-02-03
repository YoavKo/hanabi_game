from random import shuffle
from pprint import pprint

NUMBER_OF_PLAYERS = 3
NUMBER_OF_CARDS = 5
poz ={'c':0,'n':1}
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

def removeNegativeData(clue):
    p, n = clue.split("_")
    switch p.len():
        case 2:
            n = ""

        case 1:
            if p.isdigit():
                for part in n:
                    if part.isdigit():
                        n = n.replace(part, "")

            else: # p is color
                for part in n:
                    if not part.isdigit():
                        n = n.replace(part, "")

    return p + "_" + n

def sortClue(clue):
    pass

def rearrangeClue(clue):
    '''
    clue = removeNegativeData(clue,)
    clue = sortClue(clue)
    return clue
    '''
    pass

deck = deck_generate()
shuffle(deck)

players = []
for player in xrange(NUMBER_OF_PLAYERS):
    players.append({'Cards' : [], 'Clues' : [],})
    for card in xrange(NUMBER_OF_CARDS):
        players[player]['Cards'].append(deck.pop())
        players[player]['Clues'].append("_")

#pprint(deck)
def print_bord():
    pprint(players[1:])

while True:
    print_bord()

    cmd = raw_input("Enter clue:[player,card,n/c]")
    cmd = cmd.split(",")
    pprint(cmd)
    player_num, card_num,type_data = cmd
    data = players[int(player_num)]['Cards'][int(card_num)][poz[type_data]]

    for card in players[int(cmd[0])]['Cards']:
        index = players[int(cmd[0])]['Cards'].index(card)
        clue = players[int(cmd[0])]['Clues'][index]
        if data not in clue:
            if data in card:
                print card
                players[int(cmd[0])]['Clues'][index] = data + clue
            else:
                players[int(cmd[0])]['Clues'][index] = clue + data

