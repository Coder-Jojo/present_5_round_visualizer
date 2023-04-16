import threading
import json
from gui import run_gui
from logic import logic
from lsbox import logic_sbox
from sbox_layer import SboxLayer
from lines import Lines


lines = Lines()
sbox_layer1 = SboxLayer()
sbox_layer2 = SboxLayer()
sbox_layer3 = SboxLayer()
sbox_layer4 = SboxLayer()
sbox_layer5 = SboxLayer()

sbox_layers = [sbox_layer1, sbox_layer2, sbox_layer3, sbox_layer4, sbox_layer5]

with open('./options.json', 'r') as f:
    options = json.load(f)

if options["round"] > 4 or options["round"] < 0:
    print("round must be between 0 and 4")

if options["sbox"] > 15 or options["sbox"] < 0:
    print("sbox must be between 0 and 15")

if __name__ == '__main__':
    if options['useSbox']:
        path_logic = logic_sbox
    else:
        path_logic = logic
    threading.Thread(target=path_logic, args=[sbox_layers, lines, options]).start()
    run_gui(sbox_layers, lines, options)