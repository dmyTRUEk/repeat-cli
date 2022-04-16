# Repeat CLI:
Simple python3 script for repeating given command N times.


## Usage:
```
$ repeat-cli 5 echo Hello World!
```
Result:
```
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
```


## Installation:
### Linux:
1. Download `repeat-cli.py`
2. Put it in some folder in `$PATH`, for example `~/.local/bin/`:  
  `$ mv repeat-cli.py ~/.local/bin/repeat-cli`
3. Give it executable permission: `$ chmod +x ~/.local/bin/repeat-cli`


## TODO:
- rewrite using Python 3.10 power: `match sys.argv: …`

