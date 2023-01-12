# Almost a circle
Project completed during my **Fullstack Software Engineering** program at **ALX**. It aims to learn about unit testing, serialization, deserialization, JSON, `args` and `kwargs` in **Python**.

## Technologies
* Python Scripts are written with Python
* Tested on Ubuntu

## Files

Inside `models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | convert the directory as a package |
| `base.py` | Base class of geometrical instances |
| `rectangle.py` | inherit attributes references from `Base` class |
| `square.py` | inherit attributes references from `Square` class |

Each class contains public/private attributes, class and static methods. Also, these classes raise exceptions when required.

Inside `tests/test_models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | convert the directory as a package |
| `test_base.py` | contain unittests to `Base` class |
| `test_rectangle.py` | contain unittests to `Rectangle` class |
| `test_square.py` | contain unittests to `Square` class |
