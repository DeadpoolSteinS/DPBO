#include <iostream>
#include "Processor.cpp"
#include "Disk.cpp"
#include "Ram.cpp"
using namespace std;

class Pc
{
    private:
        Processor processor;
        Disk disk;
        Ram ram;
        int totalPrice = 0;

    public:
        Pc(){}

        Pc(Processor processor, Disk disk, Ram ram)
        {
            this->processor = processor;
            this->disk = disk;
            this->ram = ram;
            this->totalPrice = processor.getPrice() + disk.getPrice() + ram.getPrice();
        }

        void setProcessor(Processor processor)
        {
            this->processor = processor;
        }

        Processor& getProcessor()
        {
            return this->processor;
        }

        void setDisk(Disk disk)
        {
            this->disk = disk;
        }

        Disk& getDisk()
        {
            return this->disk;
        }

        void setRam(Ram ram)
        {
            this->ram = ram;
        }

        Ram& getRam()
        {
            return this->ram;
        }

        void setTotalPrice()
        {
            this->totalPrice = this->processor.getPrice() + this->disk.getPrice() + this->ram.getPrice();
        }

        int getTotalPrice()
        {
            return this->totalPrice;
        }

        void showPc()
        {
            this->processor.showProcessor();
            this->disk.showDisk();
            this->ram.showRam();

            this->setTotalPrice();
            cout << "Total Price     : " << this->getTotalPrice() << endl;
        }

        ~Pc(){}
};