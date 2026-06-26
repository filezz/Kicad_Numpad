# Kicad_Numpad
A Numpad designed completly from scratch, using KICAD, RP2040 and MicroPython

BOM : 
  -Raspberry PI RP2040 pico - The brain 
  -Cherry MX switches 
  -1N4148 Diodes 
  -Custom PCB 
  
The main logic : 
By using a diode matrix, the keys can be indexed. The keys are pulled up high, so when a key is pressed it closes a circuit and current flows one way. Becasue the diodes are arrranged a matrix we can exactly know what column and what row wax pressed.

