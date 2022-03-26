#include "FootballTeam.cpp"
using namespace std;

int main(){
    FootballTeam team1;
    team1.setName("FC Barcelona");
    team1.setOrigin("Spain");
    team1.setYear("1899");
    vector <string> players1 = {"Ter Stegen", "Gerard Pique", "Sergio Busquets"};
    team1.setPlayers(players1);
    team1.addPlayer("Dani Alves");

    vector <string> players2 = {"Alisson", "Virgil van Dijk", "Sadio Mane"};
    FootballTeam team2("Liverpool FC", "United Kingdom", "1892", players2);
    team2.addPlayer("Mohamed Salah");

    team1.showTeam();
    printf("\n");
    team2.showTeam();
    return 0;
}