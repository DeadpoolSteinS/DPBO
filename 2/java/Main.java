public class Main{
    public static void main(String[] args){
        Memory A = new Memory("2000", 2, true);
        A.setBrand("Acer");
        A.setModel("2A");
        A.setPrice("5.000.000");
        A.setIdProduct(27);
        System.out.println("Brand        : " + A.getBrand());
        System.out.println("Model        : " + A.getModel());
        System.out.println("Price        : " + A.getPrice());
        System.out.println("Id Product   : " + A.getIdProduct());
        System.out.println("Frequency    : " + A.getFrequency());
        System.out.println("Size Memory  : " + A.getMemorySize());
        System.out.println("Support Cuda : " + A.getSupportCuda());
    }
}