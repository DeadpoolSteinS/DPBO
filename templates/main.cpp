#include "OperasiAritmetika.cpp"
using namespace std;

int main(){
    OperasiAritmetika <int> test;
    cout << test.tambah(6, 2) << endl;
    cout << test.bagi(6, 2) << endl;
    cout << test.kali(6, 2) << endl;
    cout << test.kurang(6, 2) << endl;
    return 0;
}