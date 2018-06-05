#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>

using namespace std;

const unsigned int DIGITOS = 4;
const unsigned int MAX_INTENTOS = 10;

// Obtiene el i-esimo digito de N, donde el digito
// 0 es el menos significativo
int digito(int N, int i) {
    int d = N % 10;
    while (i > 0) {
        N = N / 10;
        d = N % 10;
        i = i-1;
    }
    return d;
}

// Chequea si N tiene 4 digitos distintos
bool sin_digitos_repetidos(int N) {
    int i = 0, j = 0;
    while (i < DIGITOS) {
        j = i + 1;
        while (j < DIGITOS) {
            if (digito(N,i) == digito(N,j))
                return false;
            j = j + 1;
        }
        i = i + 1;
    }
    return true;
}

// Chequea cuantos digitos bien ubicados tiene M con respecto a M
int digitos_correctos(int N, int M) {
    int count = 0, i = 0;
    while (i < DIGITOS) {
        if (digito(N,i) == digito(M,i))
            count = count + 1;
        i = i + 1;
    }
    return count;
}

// Chequea cuantos digitos mal ubicados tiene M con respecto a M
int digitos_regulares(int N, int M) {
    int count = 0, i=0, j=0;
    while(i < DIGITOS) {
        j = 0;
        while (j < DIGITOS) {
            if (j != i && digito(N,i) == digito(M,j) )
                count++;
            j = j + 1;
        }
        i = i + 1;
    }
    return count;
}

// Genera un número al azar entre 0 y 9999, sin digitos repetidos
int generar_numero()
{
    int seed = time(0);
    srand(seed);
    int MAXIMO = pow(10,DIGITOS);
    int N = rand() % MAXIMO;
    while (!sin_digitos_repetidos(N))
        N = rand() % MAXIMO;

    return N;
}

// Juega una ronda. Devuelve "true" si el jugador acertó y "false" en caso contrario
bool jugar_ronda(int N) {
    int M;
    cout << "Ingrese un numero de 4 cifras: ";
    cin >> M;
    if (N==M) {
        cout << " CORRECTO!!!" << endl;
        return true;
    }
    cout << " ok: " << digitos_correctos(N,M)
         << " regulares: " << digitos_regulares(N,M) << endl;
    return false;
}

void test_numero_valido() {
    assert(  sin_digitos_repetidos(1234) );
    assert( !sin_digitos_repetidos(1231) );
    assert( !sin_digitos_repetidos(1221) );
    assert( !sin_digitos_repetidos(1111) );

    // este assert está chequeando una condicion incorrecta y va a fallar.
    // (lo que está mal escrito es el test, no la función que testea)
    //assert( sin_digitos_repetidos(1111) );

    cout << "test_numero_valido OK" << endl;
}

void test_digito() {
    int N = 1234;
    assert (digito(N,0) == 4);
    assert (digito(N,1) == 3);
    assert (digito(N,2) == 2);
    assert (digito(N,3) == 1);
    cout << "test_digito OK" << endl;
}


void test_generar_numero() {
    // Debe ser valido
    assert( sin_digitos_repetidos(generar_numero()) );
    // Debe tener menos de DIGITOS digitos
    assert( generar_numero() < pow(10,DIGITOS) );

    cout << "test_generar_numero OK" << endl;
}

void test_digitos_correctos() {
    assert(digitos_correctos(1234,1234) == 4);
    assert(digitos_correctos(1234,1235) == 3);
    assert(digitos_correctos(1234,5234) == 3);
    assert(digitos_correctos(1234,1243) == 2);
    assert(digitos_correctos(1234,1432) == 2);
    assert(digitos_correctos(1234,1423) == 1);
    assert(digitos_correctos(1234,4321) == 0);

    cout << "test_digitos_correctos OK" << endl;
}

void test_digitos_regulares() {
    assert(digitos_regulares(1234,1234) == 0);
    assert(digitos_regulares(1234,1235) == 0);
    assert(digitos_regulares(1234,5234) == 0);
    assert(digitos_regulares(1234,5178) == 1);
    assert(digitos_regulares(1234,1243) == 2);
    assert(digitos_regulares(1234,1432) == 2);
    assert(digitos_regulares(1234,1423) == 3);
    assert(digitos_regulares(1234,4321) == 4);

    cout << "test_digitos_regulares OK" << endl;
}

void ejecutar_tests() {
    test_digito();
    test_numero_valido();
    test_generar_numero();
    test_digitos_correctos();
    test_digitos_regulares();
    cout << "Todos los tests OK" << endl;
}

int main() {
    // esta línea se puede comentar una vez se está seguro
    // de la implementación conseguida
    ejecutar_tests();

    int N = generar_numero();

    int intentos = 0;
    while (intentos < MAX_INTENTOS) {
        if (!jugar_ronda(N)) {
            // No acertó: se suma un intento
            intentos += 1;
        }
        else
        {
            // acertó: finaliza el programa
            return 0;
        }
    }

    // Si llegamos aquí, el jugador gastó sus intentos, y perdió
    cout << "PERDISTE!!! El numero era: " << N << endl;

    return 1;
}
