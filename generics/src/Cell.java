public class Cell<T>
{
    private T test;

    public Cell(T test) {
        this.setTest(test);
    }
    
    public T getTest() {
        return test;
    }
    
    public void setTest(T test) {
        this.test = test;
    }
}
