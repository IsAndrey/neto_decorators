# neto_decorators

### Для подключения модуля в ваш проект используйте команду
```
pip install git+https://github.com/IsAndrey/neto_decorators.git
```

### В модуле импортируйте декоратор logger
```
from neto_decorators import logger


@logger('main.log')
def main():
   ...
```