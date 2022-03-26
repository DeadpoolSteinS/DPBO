class FootballTeam:
    name = ""
    origin = ""
    year = ""
    players = []

    # set default data
    def __init__(self, name = "-", origin = "", year = "", players = []):
        self.name = name
        self.origin = origin
        self.year = year
        self.players = players

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setOrigin(self, origin):
        self.origin = origin

    def getOrigin(self):
        return self.origin

    def setYear(self, year):
        self.year = year

    def getYear(self):
        return self.year

    def setPlayers(self, players):
        self.players = players

    def getPlayers(self):
        return self.players

    def addPlayer(self, player):
        self.players.append(player)

    def showTeam(self):
        print("Team Name      : " + self.getName())
        print("Origin COuntry : " + self.getOrigin())
        print("Year of Build  : " + self.getYear())

        players = self.getPlayers()
        for i in range(len(players)):
            print("    - " + players[i])