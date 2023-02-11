import threading
from gui import run_gui
from logic import logic
from sbox_layer import SboxLayer
from lines import Lines


lines = Lines()
sbox_layer1 = SboxLayer()
sbox_layer2 = SboxLayer()
sbox_layer3 = SboxLayer()
sbox_layer4 = SboxLayer()
sbox_layer5 = SboxLayer()

sbox_layers = [sbox_layer1, sbox_layer2, sbox_layer3, sbox_layer4, sbox_layer5]

options = {
    'stop': False,
    'next': False
}

if __name__ == '__main__':
    threading.Thread(target=logic, args=[sbox_layers, lines, options]).start()
    run_gui(sbox_layers, lines, options)