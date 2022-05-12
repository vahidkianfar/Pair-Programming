import numpy as np


def AssignPlayersToTeams(players):

    np.random.shuffle(players)
    np.random.shuffle(players)
    np.random.shuffle(players)
    pairing = []

    for _ in players:
        pairing.append(players.pop(np.random.randint(0, len(players))))

    [print(f'Pairing Team {i + 1} : ', players[i] + " and " + pairing[i]) for i in range(len(pairing))]


members = ["Adrian", "Aja", "Apshan", "Carl", "Eman", "Franco", "Hayley", "Ia", "Namita", "Nolan", "Sam",
           "Shannon", "Sherry", "Vahid", "Vijay", "Vinu"]

AssignPlayersToTeams(members)
