# README
### PythonHue lets you directly connect to a hue bridge in python.
<br>

## Examples:
<br>

### This code lets you just enter one of the commands ON, OFF, 1, 2, and 3 and it will execute the command.
### You can also insert one of the colors ORANGE, WHITE, GREEN, BLUE, PINK or RED.


```
  if __name__ == "__main__":
    lamp = '1'
    hue = Hue('asd-asd', '123.456.789', lamp)
    while (command := input("Kommando: ")) != "X":
        try:
            if command == "ON" or "on":
                hue.set_lamp(True)
            if command == "OFF" or "off":
                hue.set_lamp(False)
            if command == "1":
                lamp = '1'
            if command == '2':
                lamp = '2'
            if command == '3':
                lamp = '3'
            else:
                hue.set_color("command")
        except Exception as e:
            print(f"exception: {e}")
            pass
        except IOError:
            print("file not found")
        else:
            print("succesfully excecuted the command!")
    print("program closed")
```

    
    
