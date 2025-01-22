#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "arduino_secrets.h"
#include "thingProperties.h"
#include "DHT.h"

// Pin Configuration
#define DHT_PIN 4         // DHT Sensor connected to D2
#define MQ2_PIN 33        // MQ2 connected to D32
#define MQ5_PIN 32        // MQ5 connected to D33
#define MQ135_PIN 35      // MQ135 connected to D35
#define SDA_PIN 22        // I2C SDA
#define SCL_PIN 21        // I2C SCL

// DHT Sensor Type
#define DHTTYPE DHT11
DHT dht(DHT_PIN, DHTTYPE);

// LCD setup
LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address, 16 columns, 2 rows

// Gas sensor standard ranges
#define MQ2_MIN 2
#define MQ2_MAX 50
#define MQ5_MIN 5
#define MQ5_MAX 60
#define MQ135_MIN 10
#define MQ135_MAX 70

// Callback Functions
void onTemperatureChange() {
  Serial.println("Temperature value updated.");
}

void onHumidityChange() {
  Serial.println("Humidity value updated.");
}

void onMq2Change() {
  Serial.println("MQ2 value updated.");
}

void onMq5Change() {
  Serial.println("MQ5 value updated.");
}

void onMq135Change() {
  Serial.println("MQ135 value updated.");
}

void setup() {
  // Start Serial Monitor
  Serial.begin(115200);
  Serial.println("Starting ESP32 IoT with LCD...");

  // Initialize I2C and LCD
  Wire.begin(SDA_PIN, SCL_PIN); // Custom I2C pins
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Initializing...");
  Serial.println("LCD initialized and backlight turned on.");

  // Initialize DHT Sensor
  dht.begin();
  Serial.println("DHT sensor initialized.");

  // Initialize IoT Cloud
  initProperties();
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();

  // Display readiness on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("System Ready");
  delay(2000);
}

void loop() {
  ArduinoCloud.update();

  // Read sensor data
  float temperatureValue = dht.readTemperature();
  float humidityValue = dht.readHumidity();
  int mq2Value = analogRead(MQ2_PIN);
  int mq5Value = analogRead(MQ5_PIN);
  int mq135Value = analogRead(MQ135_PIN);

  // Convert gas sensor values to percentages
  float mq2Percentage = map(mq2Value, 0, 4095, 0, 100);
  float mq5Percentage = map(mq5Value, 0, 4095, 0, 100);
  float mq135Percentage = map(mq135Value, 0, 4095, 0, 100);

  // Apply standard limits for gas sensors
  if (mq2Percentage < MQ2_MIN || mq2Percentage > MQ2_MAX) {
    mq2Percentage = 0; // Set to 0 if out of range
  }
  if (mq5Percentage < MQ5_MIN || mq5Percentage > MQ5_MAX) {
    mq5Percentage = 0; // Set to 0 if out of range
  }
  if (mq135Percentage < MQ135_MIN || mq135Percentage > MQ135_MAX) {
    mq135Percentage = 0; // Set to 0 if out of range
  }

  // Update IoT Cloud variables
  temperature = temperatureValue;
  humidity = humidityValue;
  mq2 = mq2Percentage;
  mq5 = mq5Percentage;
  mq135 = mq135Percentage;

  // Display data on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperatureValue);
  lcd.print("C");
  lcd.setCursor(0, 1);
  lcd.print("Hum: ");
  lcd.print(humidityValue);
  lcd.print("%");
  delay(2000);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("MQ2: ");
  lcd.print(mq2Percentage);
  lcd.print("%");
  lcd.setCursor(0, 1);
  lcd.print("MQ5: ");
  lcd.print(mq5Percentage);
  lcd.print("%");
  delay(2000);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("MQ135: ");
  lcd.print(mq135Percentage);
  lcd.print("%");
  delay(2000);
}
