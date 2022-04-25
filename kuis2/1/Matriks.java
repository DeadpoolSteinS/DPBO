public class Matriks {
    private Integer[][] oldMatrik, newMatrik;
    private Integer x, y;

    public Matriks(Integer x, Integer y) {
        this.oldMatrik = new Integer[x][y];
        this.newMatrik = new Integer[x][y];
        this.x = x;
        this.y = y;
        this.setNewMatrik();
    }

    public Integer[][] getOldMatrik() {
        return oldMatrik;
    }

    public Integer[][] getNewMatrik() {
        return newMatrik;
    }

    public void setOldMatrik(Integer[][] oldMatrik) {
        this.oldMatrik = oldMatrik;
    }

    public void setNewMatrik(Integer[][] newMatrik) {
        this.newMatrik = newMatrik;
    }

    public void setMember(Integer x, Integer y, Integer a) {
        this.oldMatrik[x][y] = a;
    }

    public void generateNewMatrik() {
        for (Integer i = 0; i < this.x; i++) {
            for (Integer j = 0; j < this.y; j++) {
                this.generateNewMember(i, j);
            }
        }
    }

    public void generateNewMember(Integer x, Integer y) {
        for (Integer i = -1; i <= 1; i++) {
            for (Integer j = -1; j <= 1; j++) {
                this.checkErrorSum(x + i, y + j, x, y);
            }
        }
    }

    public void checkErrorSum(Integer i, Integer j, Integer x, Integer y) {
        try {
            this.newMatrik[x][y] += this.oldMatrik[i][j];
        } catch (ArrayIndexOutOfBoundsException e) {
            // TODO: handle exception
        }
    }

    public void showNewMatrik() {
        for (Integer i = 0; i < this.x; i++) {
            for (Integer j = 0; j < this.y; j++) {
                System.out.print(this.newMatrik[i][j] + " ");
            }
            System.out.print("\n");
        }
    }

    public void setNewMatrik() {
        for (Integer i = 0; i < this.x; i++) {
            for (Integer j = 0; j < this.y; j++) {
                this.newMatrik[i][j] = 0;
            }
        }
    }

}
