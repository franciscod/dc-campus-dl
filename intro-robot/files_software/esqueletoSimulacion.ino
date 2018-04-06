/****************************** algunas definiciones globales ************/

#define IR_FRONT 1
#define IR_LEFT  0
#define IR_RIGHT 2

#define MIN_DIST_SIDE 0.25
#define MIN_DIST_FRONT 0.22

#define SPEED_NORMAL 1
#define SPEED_FAST 2

/****************************** Setup *********************************/
void setup() {

  /* inicializacion de sensores */
  motors_init();
  ir_init();
  bumper_init();

  /* inicializacion del comportamiento */
  comportamiento_init();
  
  Serial.begin(9600);
}

/****************************** Loop principal ************************/
void loop() {

  /* procesamiento de sensores */
  ir_loop();
  bumper_loop();

  /* procesamiento del comportamiento */
  comportamiento_loop();
  
  
}

/***************************** Comportamientos ************************/

/***************************** SOLO COMPLETAR AQUI ************************/

enum Estado { ESTADO_INICIAL /*... */ };

Estado estado;

long t;

void comportamiento_init()
{
  /* define estado inicial y ejecuta accion de la trancision inicial, segun ejercicio */
  estado = ESTADO_INICIAL; 
  
  //... 
  
}

void comportamiento_loop()
{
	// Proceso estados, chequeo condiciones y ejecuto transiciones
	
	//...
}

/***************************** FIN COMPLETAR ***************************/


/******************** control de motores (hagamos de cuenta que hay un driver) *************/

#define motor1a  10
#define motor1b  11
#define motor2a  5
#define motor2b  6

void pid_set_speed(float left, float right)
{
  pid_set_left(left);
  pid_set_right(right);
}

void pid_set_left(float v)
{
  v = mapFloat(v, 0, 2.0, 0, 128);
  set_motor_left(v);
}

void pid_set_right(float v)
{
  v = mapFloat(v, 0, 2.0, 0, 128);
  set_motor_right(v);
}

void set_speed(float left, float right)
{
  set_motor_left(left);
  set_motor_right(right);
}

void set_motor_left(int speed)
{
  analogWrite(motor1a, speed > 0 ? speed : 0);
  analogWrite(motor1b, speed < 0 ? -speed : 0);
}

void set_motor_right(int speed)
{
  analogWrite(motor2a, speed > 0 ? speed : 0);
  analogWrite(motor2b, speed < 0 ? -speed : 0);
}

void motors_init(void)
{
  pinMode(motor1a, OUTPUT);
  pinMode(motor1b, OUTPUT);
  pinMode(motor2a, OUTPUT);
  pinMode(motor2b, OUTPUT);
}

/******************** bumper ******************/

//Bumper
#define bumRight 2
#define bumLeft 3

bool bumper_state[2] = { false, false };

void bumper_init(void)
{
  pinMode(bumLeft, INPUT_PULLUP);           // inicializo el pin pulsador como una entrada
  pinMode(bumRight, INPUT_PULLUP);           // inicializo el pin pulsador como una entrada
}


void bumper_loop(void)
{
  bumper_state[0] = !digitalRead(bumLeft);
  bumper_state[1] = !digitalRead(bumRight);
  //Serial.print("BL: "); Serial.print(bumper_state[0]); Serial.print(" BR: "); Serial.println(bumper_state[1]);
}

bool bumper_left(void)
{
  return bumper_state[0];
}

bool bumper_right(void)
{
  return bumper_state[1];
}



/************ infrarojos ********************/
#define IR_COUNT 3

#define IR_MAX_DIST 5000

#define PIN_IR0 A0
#define PIN_IR1 A1
#define PIN_IR2 A2

float ir_distances[IR_COUNT];

void ir_init(void)
{
  for (int i = 0; i < IR_COUNT; i++)
    ir_distances[i] = -1;
}

void ir_loop(void)
{
  ir_distances[0] = mapFloat(analogRead(PIN_IR0), 344.0, 1017.0, 0.06, 0.8); 
  ir_distances[1] = mapFloat(analogRead(PIN_IR1), 344.0, 1017.0, 0.06, 0.8); 
  ir_distances[2] = mapFloat(analogRead(PIN_IR2), 344.0, 1017.0, 0.06, 0.8); 

  Serial.print("IR0: "); Serial.print(ir_distances[0]);
  Serial.print(" IR1: "); Serial.print(ir_distances[1]);
  Serial.print(" IR2: "); Serial.println(ir_distances[2]);
  
}

float ir_distance(unsigned int i)
{
  if (i >= IR_COUNT) return -1;
  else
  {
    return ir_distances[i];    
  }
}


float mapFloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
