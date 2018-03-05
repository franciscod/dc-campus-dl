/* Interrupciones */
#define TIMER 0x1C
#define TECLADO 0x09

/* Codificacion de las direcciones */
#define LEFT 0
#define RIGHT 1
#define UP 2
#define DOWN 3

/* Definiciones para el gusanito */
#define NIB_MAX 16
#define NIB_CHAR 0xDB
#define NIB_BLANK 0x00
#define NIB_SPACE 0x20

/* Tamano de la pantalla */
#define FILAS 50
#define COLUMNAS 80

/* Scancodes de las teclas */
#define TECLA_LEFT 0x4B
#define TECLA_RIGHT 0x4D
#define TECLA_UP 0x48
#define TECLA_DOWN 0x50
#define TECLA_ESC 0x01

/* Organizacion de un caracter en pantalla */
struct mem_video_t {
	unsigned char ch;
	unsigned char attr;
};

/* Punteros a memoria fuera del programa */
void far *far *ivt = (void far *far *)0x00000000;
struct mem_video_t far *pantalla = (struct mem_video_t far *)0xB8000000;

/* Punteros a las ISR originales */
void (far *orig_timer)();
void (far *orig_teclado)();

/* Variables para definir al gusanito */
unsigned int gusanito[NIB_MAX] = { 0, 0, 0, 0, /* offsets de las posiciones */
								   0, 0, 0, 0, /* de cada caracter del      */
								   0, 0, 0, 0, /* gusanito                  */
								   0, 0, 0, 0 };
unsigned int longitud_gusanito = 1;          /* longitud inicial          */
unsigned char direccion_gusanito = RIGHT;    /* direccion inicial         */

/* Variables globales de la ISR del timer */
unsigned int paso_pendiente = 0;

/* Variables globales de la ISR del teclado */
unsigned char tecla_anterior = 0;
unsigned int finalizado = 0;

void setear_80x25()
{
	/* Carga y activa la font 8x16 en 200 scanlines */
	asm mov ax, 0x1114
	asm xor bl, bl
	asm int 0x10
}

void setear_80x50()
{
	/* Carga y activa la font 8x8 en 400 scanlines */
	asm mov ax, 0x1112
	asm xor bl, bl
	asm int 0x10
}

/* Modifica la IVT para atender a la interrupcion num utilizando el codigo
   que se encuentra en la posicion de memoria p (como puntero far) */
void set_isr(unsigned int num, void far *p)
{
	asm cli;
	ivt[num] = p;
	asm sti;
}

/* Obtiene de la IVT el puntero far a la ISR correspondiente a la
   interrupcion num */
void far *get_isr(unsigned int num)
{
	void (far *isr)();
	asm cli;
	isr = ivt[num];
	asm sti;
	return isr;
}

unsigned int calc_siguiente(unsigned int actual, unsigned char direccion)
{
	switch (direccion) {
		case UP:
			return actual - COLUMNAS;
		case DOWN:
			return actual + COLUMNAS;
		case LEFT:
			return actual - 1;
		case RIGHT:
			return actual + 1;
	}
	return 0; /* No tiene que llegar */
}

void mover_gusanito(unsigned int pos_siguiente)
{
	unsigned int i;
	/* Limpiar en pantalla la posicion de mas a la izquierda */
	pantalla[gusanito[0]].ch = NIB_BLANK;
	/* Shiftear la lista de posiciones a la izquierda */
	for (i = 1; i < longitud_gusanito; i++)
		gusanito[i-1] = gusanito[i];
	/* Agregar nueva posicion a la derecha */
	gusanito[longitud_gusanito-1] = pos_siguiente;
}

void crecer_gusanito(unsigned int pos_siguiente)
{
	longitud_gusanito++;
	gusanito[longitud_gusanito-1] = pos_siguiente;
}

void dibujar_gusanito()
{
	unsigned int i;
	for (i = 0; i < longitud_gusanito; i++)
		pantalla[gusanito[i]].ch = NIB_CHAR;
}

void avanzar_gusanito(unsigned char direccion)
{
	unsigned int pos_siguiente =
		calc_siguiente(gusanito[longitud_gusanito-1], direccion);
	unsigned char chsig = pantalla[pos_siguiente].ch;

	if (longitud_gusanito == NIB_MAX ||
			(chsig == NIB_BLANK || chsig == NIB_SPACE || chsig == NIB_CHAR))
		mover_gusanito(pos_siguiente);
	else
		crecer_gusanito(pos_siguiente);
}

/* Rutina de atencion de interrupciones para el teclado */
void interrupt far rutina_teclado()
{
	unsigned char presionada;
	unsigned char rawcode;
	int scancode;

	/* Obtener tecla presionada en raw y el scancode correspondiente */
	rawcode = inp(0x60); // leo del puerto de hardware 0x60
	scancode = rawcode & 0x7F; // 7 bits menos significativos
	presionada = !(rawcode & 0x80); // bit mas significativo

	// COMPLETAR RUTINA

	tecla_anterior = rawcode; // guardo tecla en un buffer
	outp(0x20, 0x20); /* EOI */
}

/* Rutina de atencion de interrupciones para el reloj */
void interrupt far rutina_reloj()
{
	// COMPLETAR RUTINA
}

int main(void)
{
	/* Cambio modo de video para que el gusanito se vea cuadrado */
	setear_80x50();

	// COMPLETAR: setear en la IVT las ISRs del timer y el teclado

	dibujar_gusanito();
	while (!finalizado) {
		if (paso_pendiente) {
			avanzar_gusanito(direccion_gusanito);
			dibujar_gusanito();
			paso_pendiente = 0;
		}
	}

	// COMPLETAR: restaurar estado en la IVT

	/* Restauro modo de video original */
	setear_80x25();

	return 0;
}
