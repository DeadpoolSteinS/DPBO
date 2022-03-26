#include <string>
#include "Hardware.cpp"
using namespace std;

class Product : public Hardware{
    private:
        string price;
        int idProduct;

    public:
        Product(){}

        Product(string price, int idProduct){
            this->price = price;
            this->idProduct = idProduct;
        }

        void setPrice(string price)
        {
            this->price = price;
        }

        string getPrice()
        {
            return this->price;
        }

        void setIdProduct(int idProduct)
        {
            this->idProduct = idProduct;
        }

        int getIdProduct()
        {
            return this->idProduct;
        }

        ~Product(){}
};