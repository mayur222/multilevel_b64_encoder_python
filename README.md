# Multilevel Base64 encoding for python scripts
Convert python script in multilevel base64 encoded script which works as seamlessly as you original script.


##How to use
```
$ python3 Encoder.py -h
usage: Encoder.py [-h] [-o [OUTPUT]] [-f] [code] level

Convert python script to multilevel base64 encoded script

positional arguments:
  code
  level                 Number of levels of encoding

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
```

##Usage
```
python3 Encoder.py TestFile.py 30
```
**Note:** Don't increase level too much as it can hang your system.
