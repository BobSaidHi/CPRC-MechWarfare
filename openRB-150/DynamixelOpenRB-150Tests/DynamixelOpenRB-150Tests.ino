#include <Dynamixel2Arduino.h>

// See https://github.com/ROBOTIS-GIT/Dynamixel2Arduino/blob/master/examples/basic

//OpenRB does not require the DIR control pin.
#define DXL_SERIAL Serial1
#define DEBUG_SERIAL Serial
const int DXL_DIR_PIN = -1;

const uint8_t DXL_ID = 6;
const float DXL_PROTOCOL_VERSION = 1.0;
uint32_t BAUDRATE = 1000000; //1Mbsp

Dynamixel2Arduino dxlLeg(DXL_SERIAL, DXL_DIR_PIN);

//This namespace is required to use Control table item names
using namespace ControlTableItem;

// Test
//int printDebug = 0;

void setup() {
  // put your setup code here, to run once:

  //Serial.begin(115200);
  //Serial.println("Hello World!");

  // Use UART port of DYNAMIXEL Shield to debug.
  DEBUG_SERIAL.begin(115200);
  
  // Set Port baudrate. This has to match with DYNAMIXEL baudrate.
  dxlLeg.begin(BAUDRATE);
  // Set Port Protocol Version. This has to match with DYNAMIXEL protocol version.
  dxlLeg.setPortProtocolVersion(DXL_PROTOCOL_VERSION);

  DEBUG_SERIAL.print("PROTOCOL ");
  DEBUG_SERIAL.print(DXL_PROTOCOL_VERSION, 1);
  DEBUG_SERIAL.print(", ID ");
  DEBUG_SERIAL.print(DXL_ID);
  DEBUG_SERIAL.print(": ");
  if(dxlLeg.ping(DXL_ID) == true) {
    DEBUG_SERIAL.print("ping succeeded!");
    DEBUG_SERIAL.print(", Baudrate: ");
    DEBUG_SERIAL.println(BAUDRATE);
  }
  else {
    DEBUG_SERIAL.print("ping failed!");
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println("Hello World!");
  //DEBUG_SERIAL.print("PROTOCOL ");
  //if(printDebug < 100) {
  DEBUG_SERIAL.print("PROTOCOL ");
  DEBUG_SERIAL.print(DXL_PROTOCOL_VERSION, 1);
  DEBUG_SERIAL.print(", ID ");
  DEBUG_SERIAL.print(DXL_ID);
  DEBUG_SERIAL.print(": ");
  if(dxlLeg.ping(DXL_ID) == true) {
    DEBUG_SERIAL.print("ping succeeded!");
    DEBUG_SERIAL.print(", Baudrate: ");
    DEBUG_SERIAL.println(BAUDRATE);
  }
  else {
    DEBUG_SERIAL.print("ping failed!");
  }
  //}
  //printDebug+=1;
}

