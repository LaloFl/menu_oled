import machine, ssd1306, os, utime, framebuf
import utils

# Conexión con OLED
i2c = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

btn_select = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
btn_up = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
btn_down = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

cols_coords = [
    {"x":0,"y":0},
    {"x":0,"y":28},
    {"x":0,"y":56},
]

options=[
    "Option #1",
    "Option #2",
    "Option #3",
    "Option #4",
    "Option #5",
    "Option #6",
]

selected=0
while True:
    select = btn_select.value()
    up = btn_up.value()
    down = btn_down.value()
    try:
        selected = (selected + (1 if down == 0 else -1 if up == 0 else len(options)-1 if up == 0 and selected == 0 else 0)) % len(options)
    except:
        pass
    
    if any([up == 0, down == 0, select == 0]):
        utime.sleep_ms(150)
    oled.fill(0)
    oled.text(options[len(options) - 1 if selected - 1 == -1 else selected-1], cols_coords[0]["x"],cols_coords[0]["y"])
    oled.text(options[selected] +" <--", cols_coords[1]["x"] ,cols_coords[1]["y"])
    oled.text(options[(selected+1) % len(options)], cols_coords[2]["x"],cols_coords[2]["y"])
    
    if (select == 0):
        utime.sleep_ms(150)
        while True:
            oled.fill(0)
            oled.text("Selected: ", 0,0)
            oled.text(options[selected], 30,30)
            oled.show()
            if (btn_select.value() == 0):
                utime.sleep_ms(150)
                break
    oled.show()
    

