#include <iostream>
#include "Memory.cpp"
using namespace std;

int main(){
    Memory A = Memory("2000", 2, true);
    A.setBrand("Acer");
    A.setModel("2A");
    A.setPrice("5.000.000");
    A.setIdProduct(27);
    cout << "Brand        : " << A.getBrand() << endl;
    cout << "Model        : " << A.getModel() << endl;
    cout << "Price        : " << A.getPrice() << endl;
    cout << "Id Product   : " << A.getIdProduct() << endl;
    cout << "Frequency    : " << A.getFrequency() << endl;
    cout << "Size Memory  : " << A.getMemorySize() << endl;
    cout << "Support Cuda : " << A.getSupportCuda() << endl;
    return 0;
}