# 5 Round Differential Visualizer of Present

## Requirements

To install the necessary dependencies run the following command:
```bash
pip install -r requirements.txt
```

## Usage
To start the visualizer, run the following command in a terminal:
```bash
python3 main.py
```

## Configuration
The configuration file is located in `options.json`. The following options are available:
```json
{
    "stop": false, // NOT TO BE SET BY USER
    "next": false, // NOT TO BE SET BY USER
    "useSbox": true, // TRUE if only differentials allowed by ddt is to be used, FALSE otherwise
    "round": 1, // set the round number where one sbox should be active [0, 4]
    "sbox": 3 // set the sbox number which should be active [0, 15]
}
```

## Controls
The following controls are available:
- `n` - draw next line

## Sample Image
![visualizer](https://github.com/Coder-Jojo/present_5_round_visualizer/blob/main/preview.png)


