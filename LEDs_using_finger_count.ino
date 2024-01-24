int ledPino1 = 3;  // Pino do primeiro LED
int ledPino2 = 5;  // Pino do segundo LED
int ledPino3 = 7;  // Pino do terceiro LED

void setup() {
  Serial.begin(9600);
  pinMode(ledPino1, OUTPUT);
  pinMode(ledPino2, OUTPUT);
  pinMode(ledPino3, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read(); // Lê o comando enviado pelo Python
    
    if (comando == '1') {
      digitalWrite(ledPino1, HIGH); // Liga o primeiro LED
      Serial.println("LED 1 ligado");
    } else if (comando == '2') {
      digitalWrite(ledPino2, HIGH); // Liga o segundo LED
      Serial.println("LED 2 ligado");
    } else if (comando == '3') {
      digitalWrite(ledPino3, HIGH); // Liga o terceiro LED
      Serial.println("LED 3 ligado");
    } else if (comando == '0') {
      digitalWrite(ledPino1, LOW); // Desliga o primeiro LED
      digitalWrite(ledPino2, LOW); // Desliga o segundo LED
      digitalWrite(ledPino3, LOW); // Desliga o terceiro LED
      Serial.println("Todos os LEDs desligados");
    }
  }
}
