public class Pc
{
    private Processor processor;
    private Disk disk;
    private Ram ram;
    private int totalPrice = 0;

    Pc(){}

    Pc(Processor processor, Disk disk, Ram ram)
    {
        this.processor = processor;
        this.disk = disk;
        this.ram = ram;
        this.totalPrice = processor.getPrice() + disk.getPrice() + ram.getPrice();
    }

    public void setProcessor(Processor processor)
    {
        this.processor = processor;
    }

    public Processor getProcessor()
    {
        return this.processor;
    }

    public void setDisk(Disk disk)
    {
        this.disk = disk;
    }

    public Disk getDisk()
    {
        return this.disk;
    }

    public void setRam(Ram ram)
    {
        this.ram = ram;
    }

    public Ram getRam()
    {
        return this.ram;
    }

    public void setTotalPrice()
    {
        this.totalPrice = this.processor.getPrice() + this.disk.getPrice() + this.ram.getPrice();
    }

    public int getTotalPrice()
    {
        return this.totalPrice;
    }

    public void showPc()
    {
        this.processor.showProcessor();
        this.disk.showDisk();
        this.ram.showRam();

        this.setTotalPrice();
        System.out.println("Total Price     : " + this.getTotalPrice());
    }
}