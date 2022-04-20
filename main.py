import datetime


def log_decor(input_patch):
    def _log_decor(run_function):
        def new_function(*args, **kwargs):
            now = datetime.datetime.now()
            start = now.strftime("%d-%m-%Y %H:%M")
            result = run_function(*args, **kwargs)
            data_string = str(
                f'В {start} вызывается функция {run_function} c аргументами {args} и {kwargs} с результатом: {result}') + '\n'
            with open('logs.txt', 'ab') as file:
                file.write(data_string.encode('utf-8'))
            return result
        return new_function

    return _log_decor


logs_patch = 'logs.txt'
log_decor_patch = log_decor(logs_patch)


@log_decor_patch
def summat(a, b):
    return a + b


summat(3, 6)
