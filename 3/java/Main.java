public class Main
{
    public static void main(String[] args)
    {
        Processor processor = new Processor("Ryzen 3 5300U", 3000000);
        Disk disk = new Disk("SSD", "512GB", 1000000);
        Ram ram = new Ram("8GB", 500000);

        Pc pc = new Pc(processor, disk, ram);
        pc.showPc();

        System.out.print("\n");

        pc.getProcessor().setName("Intel I3 Gen11");
        pc.getProcessor().setPrice(1000000);
        pc.showPc();
    }
}