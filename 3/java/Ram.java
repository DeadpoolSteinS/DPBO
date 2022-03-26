public class Ram
{
    private String capacity = "";
    private int price = 0;

    Ram(){}

    Ram(String capacity, int price)
    {
        this.capacity = capacity;
        this.price = price;
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

    public void showRam()
    {
        System.out.println("RAM Capacity    : " + this.getCapacity());
        System.out.println("RAM Price       : " + this.getPrice());
    }
}