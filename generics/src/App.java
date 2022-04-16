public class App {
    public static void main(String[] args) throws Exception {
        Cell<Integer> angka = new Cell<Integer>(3);
        Cell<String> kata = new Cell<String>("tiga");
        System.out.println(angka.getTest());
        System.out.println(kata.getTest());
    }
}
