import re
#change "input.ttrm" to "blahblah.ttrm" to change the input file's name to blahblah.ttrm
file = open("input.ttrm", "r")
text = file.read()

p1_attacks = []
p2_attacks = []

p1_pieces = []
p2_pieces = []

number = re.findall("\"stats\":\{.*?attack\":.*?,.*?,\"kills\":.*?,", text)


#search for attack and append it to the player's corresponding array
for i in range(1, len(number), 4):
    p1_attacks.append(re.search("\"attack\":.*?,", number[i]).group())
    p1_pieces.append(re.search("\"piecesplaced\":.*?,", number[i]).group())

for i in range(3, len(number), 4):
    p2_attacks.append(re.search("\"attack\":.*?,", number[i]).group())
    p2_pieces.append(re.search("\"piecesplaced\":.*?,", number[i]).group())


#take raw number values (without the attack thingey attached)
p1_attacks_raw = []
p1_pieces_raw = []

p2_attacks_raw = []
p2_pieces_raw = []

#append the raw number, because they are all in same format can take form 9nth (after "attack":), to before the comma. access as 2d array 
#the element then the string needed --> send to _raw array 
for i in range(0, len(p1_attacks)):
    p1_attacks_raw.append(
        p1_attacks[i][9:len(p1_attacks[i])-1]
        )
    
    p1_pieces_raw.append(
        p1_pieces[i][15:len(p1_pieces[i])-1]
        )

for i in range(0, len(p2_attacks)):
    p2_attacks_raw.append(
        p2_attacks[i][9:len(p2_attacks[i])-1]
        )
    
    p2_pieces_raw.append(
        p2_pieces[i][15:len(p2_pieces[i])-1]
        )


#find who players 1 and 2 are :skull:
usertext = re.finditer("\"username\":\".*?\"", text)
user1 = usertext.__next__()
player1 = user1.group()[12:len(user1.group())-1]

user2 = usertext.__next__()
player2 = user2.group()[12:len(user2.group())-1]


#total everything
p1_attacks_total = 0
p1_pieces_total = 0

p2_attacks_total = 0
p2_pieces_total = 0

for i in p1_attacks_raw:
    p1_attacks_total += int(i)
for i in p1_pieces_raw:
    p1_pieces_total += int(i)

for i in p2_attacks_raw:
    p2_attacks_total += int(i)
for i in p2_pieces_raw:
    p2_pieces_total += int(i)

print(player1, "\nattacks:", p1_attacks_total, "\npieces placed:", p1_pieces_total)
print("Attacks per piece:", p1_attacks_total/p1_pieces_total)

print(player2, "\nattacks:", p2_attacks_total, "\npieces placed:", p2_pieces_total)
print("Attacks per piece:", p2_attacks_total/p2_pieces_total)

input("\n\nType anything to exit")