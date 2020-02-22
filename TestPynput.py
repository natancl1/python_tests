from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.up:
       print('UP')
    elif key == keyboard.Key.down:
       print('DOWN')
    elif key == keyboard.Key.right:
       print('RIGHT')
    elif key == keyboard.Key.left:
       print('LEFT')
    else:
       listener.stop()

with keyboard.Listener(on_press=on_press) as listener: listener.join()

listener = keyboard.Listener(on_press=on_press)
listener.start()
