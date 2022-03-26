public class Processor
{
    private String name = "";
    private int price = 0;

    Processor(){}

    Processor(String name, int price)
    {
        this.name = name;
        this.price = price;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public String getName()
    {
        return this.name;
    }

    public void setPrice(int price)
    {
        this.price = price;
    }

    public int getPrice()
    {
        return this.price;
    }

    public void showProcessor()
    {
        System.out.println("Processor name  : " + this.getName());
        System.out.println("Processor Price : " + this.getPrice());
    }
}