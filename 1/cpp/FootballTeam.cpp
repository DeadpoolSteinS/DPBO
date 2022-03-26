#include <iostream>
#include <string>
#include <vector>
using namespace std;

class FootballTeam
{
    private:
        string name;
        string origin;
        string year;
        vector <string> players;

    // set default data
    public:
        FootballTeam(){}

        FootballTeam(string name, string origin, string year, vector <string> players)
        {
            this->name = name;
            this->origin = origin;
            this->year = year;
            this->players.insert(this->players.end(), players.begin(), players.end());
        }

        void setName(string name)
        {
            this->name = name;
        }

        string getName()
        {
            return this->name;
        }

        void setOrigin(string origin)
        {
            this->origin = origin;
        }

        string getOrigin()
        {
            return this->origin;
        }

        void setYear(string year)
        {
            this->year = year;
        }

        string getYear()
        {
            return this->year;
        }

        void setPlayers(vector <string> players)
        {
            this->players.insert(this->players.end(), players.begin(), players.end());
        }

        vector <string> getPlayers()
        {
            return this->players;
        }

        void addPlayer(string player)
        {
            this->players.push_back(player);
        }

        void showTeam()
        {
            cout << "Team Name      : " << this->getName() << endl;
            cout << "Origin Country : " << this->getOrigin() << endl;
            cout << "Year of Build  : " << this->getYear() << endl;

            for(int i = 0; i < this->getPlayers().size(); i++)
            {
                cout << "    - " << this->getPlayers()[i] << endl;
            }
        }
        ~FootballTeam(){}
};