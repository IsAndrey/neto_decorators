from datetime import datetime as dt


def logger(path):

    def __logger(old_function):

        def new_function(*args, **kwargs):
            datetime = str(dt.now())[:-7]  # отсекаем милисекунды
            function_name = old_function.__name__
            params = []
            if args is not None:
                params.extend([str(a) for a in args])
            if kwargs is not None:
                params.extend([f'{k}={v}' for k, v in kwargs.items()])
            params = ', '.join(params)
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(
                    f'{datetime} - {function_name}({params}) => {result}\n'
                )
            return result

        return new_function

    return __logger