#include <string>
#include "Product.cpp"
using namespace std;

class Memory : public Product{
    private:
        string frequency;
        int memorySize;
        bool supportCuda;

    public:
        Memory(){}

        Memory(string frequency, int memorySize, bool supportCuda){
            this->frequency = frequency;
            this->memorySize = memorySize;
            this->supportCuda = supportCuda;
        }

        void setFrequency(string frequency)
        {
            this->frequency = frequency;
        }

        string getFrequency()
        {
            return this->frequency;
        }

        void setMemorySize(int memorySize)
        {
            this->memorySize = memorySize;
        }

        int getMemorySize()
        {
            return this->memorySize;
        }

        void setSupportCuda(bool supportCuda)
        {
            this->supportCuda = supportCuda;
        }

        bool getSupportCuda()
        {
            return this->supportCuda;
        }

        ~Memory(){}
};