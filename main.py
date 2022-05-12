import numpy as np

players = ["Adrian", "Aja", "Apshan", "Carl", "Eman", "Franco", "Hayley", "Ia", "Namita", "Nolan", "Sam",
           "Shannon", "Sherry", "Vahid", "Vijay", "Vinu"]

np.random.shuffle(players)
np.random.shuffle(players)
np.random.shuffle(players)

pairing = []
for player in players:
    pairing.append(players.pop(np.random.randint(0, len(players))))

for i in range(len(players)):
    print(f'Pairing Team {i+1} : ', players[i] + " and " + pairing[i])
