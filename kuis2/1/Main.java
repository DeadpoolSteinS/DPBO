import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner user = new Scanner(System.in);
        Integer x = user.nextInt();
        Integer y = user.nextInt();

        Matriks matrik = new Matriks(x, y);

        for (Integer i = 0; i < x; i++) {
            for (Integer j = 0; j < y; j++) {
                Integer z = user.nextInt();
                matrik.setMember(i, j, z);
            }
        }

        matrik.generateNewMatrik();
        matrik.showNewMatrik();
    }
}