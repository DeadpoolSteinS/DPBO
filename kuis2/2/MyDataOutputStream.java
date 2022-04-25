public class MyDataOutputStream implements MyDataStream {
    private String stream;

    public MyDataOutputStream(String stream) {
        this.stream = stream;
    }

    public String getDataStream() {
        return this.stream;
    }
}
