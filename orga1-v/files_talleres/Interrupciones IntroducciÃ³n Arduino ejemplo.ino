
/* Constantes que no cambian y son usadas para setear el numero de los pines */
#define motorPinA  5       // el numero del pin de uno de los cables de motor
#define motorPinB  6       // el numero del pin del otro cable del motor
#define sensorInt  3       // el numero del pin del sensor que interrumpe
#define sensorPoll 2       // el numero del pin del sensor sobre el cual se hace polling


/* variables que cambian su valor: */
bool andando = true;
bool nitro   = false;

/* setup inicial*/
void setup() {
  pinMode(sensorPoll, INPUT_PULLUP);// inicializo el pin como una entrada (recordar usar INPUT_PULLUP)
  pinMode(motorPinA, OUTPUT);       // inicializo el pin A del motor como una salida
  analogWrite(motorPinA,0);  	    // pongo en 0 el pin A del motor
  pinMode(motorPinB, OUTPUT);       // inicializo el pin B del motor como una salida
  Serial.begin(9600);               // configuro e inicializo la comunicacion serial a 9600 baudios
  // configuro la interrupcion del pin sensorInt para que llame a la funcion meInterrumpieron
  // cuando se produce un cambio 
  attachInterrupt(digitalPinToInterrupt(sensorInt), meInterrumpieron, CHANGE);    
}

/* loop del programa */
void loop(){
  if(andando){                      // Pregunto si estoy en estado andando
    if (digitalRead(sensorPoll)){   // Pregunto si el sensorPoll esta apretado
      nitro = true;                 // Si estoy en estos estados seteo el estado nitro
    }
    else{                           // Si el sensorPoll no esta apretado
      nitro = false;                // pongo nitro como false
    }
  }
  actualizarEstado();               // llamo a la funcion que manda potencia a los motores dependiendo del estado definido
}

/* funcion que actualiza la velocidad de los motores dependiendo del estado*/
void actualizarEstado(){
  if(andando){                                     // Si el estado es andando
    if(nitro){                                     // y nitro es verdadero
      analogWrite(motorPinB,250);                  // Seteo la velocidad de el motor a 250      
      Serial.println("estado: andando nitro");     // mando por serial el estado 
    }
    else{
      analogWrite(motorPinB,30);                   // Si nitro == 0 entonces pongo velocidad de 30 a los motores
      Serial.println("estado: andando sin nitro"); // mando por serial el estado 
    }
  }                                
  else{                                    // Si andando no es verdadero
      analogWrite(motorPinB,0);            // freno el motor poniendo velocidad 0
      Serial.println("estado: detenido");  // mando por serial el estado 
  }
}

/* funcion que se llama cuando se produce una interrupcion */
void meInterrumpieron(){
  if(andando){                       // si estoy andando
    andando=false;                   // entonces freno
  }
  else{                              // Si estoy frenado
    andando = true;                  // comienzo a andar
  }
}
