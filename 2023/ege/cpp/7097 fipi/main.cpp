#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

int main() {
    int n;
    int o = 100000000;
    int c = 0;
    ifstream f("27_B_7097 (1).txt");
    if (f.is_open()) { // прверяю, открыт ли файл
        f >> n;
        int **a = new int *[n];
        for (int i = 0; i < n; i++) {
            a[i] = new int[2];
        }

        for (int i = 0; i < n; i++) f >> a[i][0] >> a[i][1];
        for (int i = 0; i < n; i++) {
            if (a[i][1] % 44 == 0) {
                a[i][1] = a[i][1] / 44;
            } else {
                a[i][1] = (a[i][1] / 44) + 1;
            }
        }


        for (int i = 0; i < 100; i++) {
            if ((c < o) and (c != 0)) {
                o = c;
            }
            c = 0;
            for (int j = 0; j < 100; j++) {
                if (i != j) {
                    c += (((abs(a[i][0] - a[j][0])) * a[j][1]));

                }
            }
        }
        delete[] a;
        cout << o << endl;
    } else {
        cout << "cannot open file" << endl;
    }
    return 0;


}