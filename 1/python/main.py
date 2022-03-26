from FootballTeam import FootballTeam

team1 = FootballTeam()
team1.setName("FC Barcelona")
team1.setOrigin("Spain")
team1.setYear("1899")
team1.setPlayers(["Ter Stegen", "Gerard Pique", "Sergio Busquets"])
team1.addPlayer("Dani Alves")

team2 = FootballTeam("Liverpool FC", "United Kingdom", "1892", ["Alisson", "Virgil van Dijk", "Sadio Mane"])
team2.addPlayer("Mohamed Salah")

team1.showTeam()
print("\n")
team2.showTeam()