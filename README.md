# thoughtful_ai

Tech screen solution for Arthur Bayerlein

## Dependencies

- Python 3.x

## Configuration

The thresholds for determining if a package is **bulky** or **heavy** are configurable via the `config.ini` file.

- **max_volume:** The volume threshold in cubic centimeters.
- **max_dimension:** The maximum dimension threshold in centimeters.
- **max_mass:** The mass threshold in kilograms.

## Install

All packages are in the standard library, but `requirements.txt` added for extensibility: 
```
pip3 install -r requirements.txt
```

## How to Run

- You can test the sorting function by running the dispatcher.py script:
```
python3 dispatcher.py
```
- Running tests: 
```
python3 -m unittest discover tests
```

