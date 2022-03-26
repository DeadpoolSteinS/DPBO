public class Disk
{
    private String type = "";
    private String capacity = "";
    private int price = 0;

    Disk(){}

    Disk(String type, String capacity, int price)
    {
        this.type = type;
        this.capacity = capacity;
        this.price = price;
    }

    public void setType(String type)
    {
        this.type = type;
    }

    public String getType()
    {
        return this.type;
    }

    public void setCapacity(String capacity)
    {
        this.capacity = capacity;
    }

    public String getCapacity()
    {
        return this.capacity;
    }

    public void setPrice(int price)
    {
        this.price = price;
    }

    public int getPrice()
    {
        return this.price;
    }

    public void showDisk()
    {
        System.out.println("Disk Type       : " + this.getType());
        System.out.println("Disk Capacity   : " + this.getCapacity());
        System.out.println("Disk Price      : " + this.getPrice());
    }
}