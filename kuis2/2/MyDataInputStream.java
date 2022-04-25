public class MyDataInputStream implements MyDataStream {
    private String stream;

    public MyDataInputStream(String stream) {
        this.stream = stream;
    }

    public String getDataStream() {
        return this.stream;
    }
}
