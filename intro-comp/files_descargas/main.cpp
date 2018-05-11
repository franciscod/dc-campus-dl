#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include<array>
#include<ctime>

using namespace std;
//Función que determina sino hay dígitos repetidos en un vector de tamaño 4.
bool sin_digitos_repetidos(array<int,4> a){
    bool SI = true;
    int i=0;
    int j=1;
    while(SI && i<4){
        while(j<4){
            if (a[i]==a[j]) {SI=false;}
            j=j+1;
        }
        i=i+1;
        j=i+1;
    }
    return SI;
}

// Genera un arreglo de 4 dígitos al azar entre 0 y 9
array<int,4> generar()
{array<int,4> azar ={0,0,0,0};
    int i=0;
    int seed = time(NULL);
    srand(seed);
    while(i<4) {
        azar[i] = rand() % 10;
        i=i+1;
    }
    return azar;
}


array<int,4> generar_sin_repetir(){
    array<int,4> Sin_repe ={0,0,0,0};
    bool Sin=false;
    while (!(Sin && Sin_repe[0]!=0)){
        Sin_repe=generar();
        Sin=sin_digitos_repetidos(Sin_repe);
    }
    return Sin_repe;
}


array<int,2> comparar(array<int,4> secreto,array<int,4> propuesto){
    int i=0;
    int j=0;
    array<int,2> aux = {0,0};
    while(i<4){
        if (propuesto[i]==secreto[i]) {aux[0]=aux[0]+1;}
        else{
            while(j<4){
                if (i != j) {
                    if (propuesto[i]==secreto[j]) {aux[1]=aux[1]+1;
                    }
                }
                j=j+1;
            }
        }
        i=i+1;
        j=0;
    }
    return aux;
}

array<int,4> pedir(){
    array<int,4> propuesto={0,0,0,0};
    int i =0;
    bool Sin_repe=false;
    while(!Sin_repe){
        while(i<4){
            cout << "Ingrese el " << i << " -esimo dígito" << endl;
            cin >> propuesto[i];
        i=i+1;
        }
        if(sin_digitos_repetidos(propuesto)){Sin_repe=true;}
        else {
            cout << "La secuencia de dígitos tiene repetidos. Tendrá que ingresarlos de nuevo" << endl;
        }
        i=0;
    }
    return propuesto;
}

void jugar(){
    int jugada=0;
    bool gano=false;
    array<int,4> secreto=generar_sin_repetir();
    array<int,4> propuesto={0,0,0,0};
    array<int,2> Buenos_Regulares = {0,0};
    while(jugada < 10 && !gano){
        propuesto=pedir();
        Buenos_Regulares=comparar(secreto,propuesto);
        if(Buenos_Regulares[0]==4){gano=true;}
        else{
            cout << "Su número propuesto: " << propuesto[0] << propuesto[1] << propuesto[2] << propuesto[3]<< endl;
            cout << "Tiene buenos " << Buenos_Regulares[0] << endl;
            cout << "Tiene regulares " << Buenos_Regulares[1] << endl;
            cout << "Intentelo nuevamente." << endl;
        };
        jugada=jugada+1;
    }
    if(gano){
        cout << "GANOOOOOOO!!!!" << endl;
    } else{
        cout << "PERDIO :-(" << endl;
    };

}


int main(){
    jugar();
    return 0;
}

/*
int main(){
array<int,4> s={1,2,3,4};
array<int,4> p={1,3,2,4};
array<int,2> a = {0,0};
a= comparar(s,p);
cout << "Tiene buenos " << a[0] << endl;
cout << "Tiene regulares " << a[1] << endl;
return 0;
}





/*
int main() {
int i =0;
array<int,4> a =generar();
while(i<4) {
    cout <<a[i]  << endl;
    i=i+1;
}
*/
