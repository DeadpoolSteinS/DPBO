public class FootballTeam
{
    private String name;
    private String origin;
    private String year;
    private String[] players;

    // set default data
    public FootballTeam(){}

    public FootballTeam(String name, String origin, String year, String[] players)
    {
        this.name = name;
        this.origin = origin;
        this.year = year;
        this.players = players;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public String getName()
    {
        return this.name;
    }

    public void setOrigin(String origin)
    {
        this.origin = origin;
    }

    public String getOrigin()
    {
        return this.origin;
    }

    public void setYear(String year)
    {
        this.year = year;
    }

    public String getYear()
    {
        return this.year;
    }

    public void setPlayers(String[] players)
    {
        this.players = players;
    }

    public String[] getPlayers()
    {
        return this.players;
    }

    // public void addPlayer(String player)
    // {
    //     this.players[] = player;
    // }

    public void showTeam()
    {
        System.out.println("Team Name      : " + this.getName());
        System.out.println("Origin Country : " + this.getOrigin());
        System.out.println("Year of Build  : " + this.getYear());

        String[] players = this.getPlayers();
        for(int i = 0; i < players.length; i++)
        {
            System.out.println("    - " + players[i]);
        }
    }
}