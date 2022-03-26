public class Product extends Hardware{
    private String price;
    private Integer idProduct;

    public Product(){}

    public Product(String price, Integer idProduct){
        this.price = price;
        this.idProduct = idProduct;
    }

    public void setPrice(String price)
    {
        this.price = price;
    }

    public String getPrice()
    {
        return this.price;
    }

    public void setIdProduct(Integer idProduct)
    {
        this.idProduct = idProduct;
    }

    public Integer getIdProduct()
    {
        return this.idProduct;
    }
}