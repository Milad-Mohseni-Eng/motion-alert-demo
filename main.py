from machine import Pin
import utime

# Pin configuration
led = Pin(14, Pin.OUT)        # GP14 - LED output
buzzer = Pin(16, Pin.OUT)     # GP16 - Buzzer output
button = Pin(28, Pin.IN)      # GP28 - Input (simulated button or trigger)

while True:
    if button.value() == 1:
        # LED blinking and fast buzzer pulses
        for _ in range(10):          # Blink and pulse 10 times
            led.toggle()             # Toggle LED state
            buzzer.toggle()          # Toggle buzzer state
            utime.sleep(0.05)        # 50 ms delay
        led.value(0)                 # Ensure LED is off after blinking
        buzzer.value(0)              # Ensure buzzer is off after pulsing
    else:
        # Button not pressed → everything off
        led.value(0)
        buzzer.value(0)

    utime.sleep(0.1)                 # Small loop delay
