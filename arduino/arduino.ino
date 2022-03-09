#include "Adafruit_APDS9960.h"

Adafruit_APDS9960 apds;

void setup() {
  Serial.begin(9600);

  if (!apds.begin()) {
    Serial.println("Falha ao inicializar o dispositivo. Verifique as conexões!");
  }
  else {
    Serial.println("Dispositivo inicializado!");
  }

  apds.enableProximity(true);
  apds.enableGesture(true);
}

void loop() {
  uint8_t gesture = apds.readGesture();

  if (gesture == APDS9960_DOWN) Serial.write("down\n");
  if (gesture == APDS9960_UP) Serial.write("up\n");
  if (gesture == APDS9960_LEFT) Serial.write("left\n");
  if (gesture == APDS9960_RIGHT) Serial.write("right\n");
}
