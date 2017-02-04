from random import shuffle
from pprint import pprint

NUMBER_OF_PLAYERS = 3
NUMBER_OF_CARDS = 5
poz ={'c':1,'n':0}

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
                deck.append(number[0]+color)

    return deck

def removeNegativeData(clue):
    p, n = clue.split("_") # posetive & negavit parts of the clue
    if len(p) == 2:
        n = ""

    elif len(p) == 1:
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
    p, n = clue.split("_")  # posetive & negavit parts of the clue
    return "".join(sorted(p)) + "_" + "".join(sorted(n))

def rearrangeClue(clue):
    clue = removeNegativeData(clue)
    clue = sortClue(clue)
    return clue

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
    player_num = int(player_num)
    card_num = int(card_num)
    player = players[player_num]
    data = player['Cards'][card_num][poz[type_data]]

    for card in player['Cards']:
        index = player['Cards'].index(card)
        clue = player['Clues'][index]
        if data not in clue:
            if data in card:
                print card
                player['Clues'][index] = rearrangeClue(data + clue)

            else:
                player['Clues'][index] = rearrangeClue(clue + data)
            

