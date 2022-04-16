#include <iostream>
using namespace std;

template <class T> class OperasiAritmetika
{
    public:
        T tambah(T a, T b)
        {
            return (a+b);
        }
        T bagi(T a, T b)
        {
            return (a/b);
        }
        T kali(T a, T b)
        {
            return (a*b);
        }
        T kurang(T a, T b)
        {
            return (a-b);
        }
};
