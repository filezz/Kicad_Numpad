# Kicad_Numpad
A Numpad designed completly from scratch, using KICAD, RP2040 and MicroPython

BOM : 
  -Raspberry PI RP2040 pico - The brain 
  -Cherry MX switches 
  -1N4148 Diodes 
  -Custom PCB 
  
The main logic : 
By using a diode matrix, the keys can be indexed. The keys are pulled up high, so when a key is pressed it closes a circuit and current flows one way. Becasue the diodes are arrranged a matrix we can exactly know what column and what row wax pressed.


Below are attached Screenshots of the Kicad project : 

<img width="2880" height="1672" alt="Screenshot from 2026-03-25 18-13-17" src="https://github.com/user-attachments/assets/8fc8b398-cb85-4614-924b-353ed31cc3a9" />

<img width="2001" height="986" alt="Screenshot from 2026-03-25 18-16-48" src="https://github.com/user-attachments/assets/8ca3f36d-659d-466e-81a2-b4fb32e6e370" />

