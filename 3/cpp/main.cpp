#include <iostream>
#include "Pc.cpp"
using namespace std;

int main()
{
    Processor processor("Ryzen 3 5300U", 3000000);
    Disk disk("SSD", "512GB", 1000000);
    Ram ram("8GB", 500000);

    Pc pc(processor, disk, ram);
    pc.showPc();

    cout << endl;

    pc.getProcessor().setName("Intel I3 Gen11");
    pc.getProcessor().setPrice(1000000);
    pc.showPc();
    return 0;
}