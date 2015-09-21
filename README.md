# themis-attack-py
[![Latest Version](https://img.shields.io/pypi/v/themis.attack.svg?style=flat-square)](https://pypi.python.org/pypi/themis.attack)
[![License](https://img.shields.io/github/license/aspyatkin/themis-attack-py.svg?style=flat-square)](https://github.com/aspyatkin/themis-attack-py/blob/master/LICENSE)
[![Dependencies status](https://img.shields.io/gemnasium/aspyatkin/themis-attack-py.svg?style=flat-square)](https://gemnasium.com/aspyatkin/themis-attack-py)
[![Code Climate](https://img.shields.io/codeclimate/github/aspyatkin/themis-attack-py.svg?style=flat-square)](https://codeclimate.com/github/aspyatkin/themis-attack-py)  
[Themis Finals](https://github.com/aspyatkin/themis-finals) attack helper library.

## Installation
```
$ pip install themis.attack
```

## Usage
### Command line mode
```
$ THEMIS_HOST=10.0.0.2 themis-attack 035585b41e6bbd70834a05690d2575ad=
```
**Note:** 10.0.0.2 stands for and IP address of contest checking system.

You can pass several flags at once. Please be aware of flag submitting restrictions (see [Themis Attack Protocol](https://github.com/aspyatkin/themis-attack-protocol) for additional information).

### Library mode
```python
from themis.attack import Carrier

carrier = Carrier('10.0.0.2')
flags = [
    '035585b41e6bbd70834a05690d2575ad=',
    'cdfdc8cbdcbe4c1e2e7378c52e1f35a5='
]

results = carrier.attack(*flags)  # [0, 0] - stands for two successful attacks
```
To get information about all available result codes, please check out [Themis Attack Protocol](https://github.com/aspyatkin/themis-attack-protocol).  
**Note:** `themis.attack.Carrier.attack` method can throw exceptions. These exceptions are subclasses of `themis.attack.AttackBaseError` class.

## See also
- [themis-finals](https://github.com/aspyatkin/themis-finals)
- [themis-finals-guidelines](https://github.com/aspyatkin/themis-finals-guidelines)
- [themis-finals-infrastructure](https://github.com/aspyatkin/themis-finals-infrastructure)
- [themis-attack-protocol](https://github.com/aspyatkin/themis-attack-protocol)
- [themis-attack-result](https://github.com/aspyatkin/themis-attack-result)
- [themis-checker-server](https://github.com/aspyatkin/themis-checker-server)
- [themis-checker-result](https://github.com/aspyatkin/themis-checker-result)
- [themis-checker-py](https://github.com/aspyatkin/themis-checker-py)

## License
MIT @ [Alexander Pyatkin](https://github.com/aspyatkin)
