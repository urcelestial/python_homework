# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        positional_args = list(args) if args else "none"
        keyword_args = kwargs if kwargs else "none"

        result = func(*args, **kwargs)

        return_value = "none" if result is None else result

        logger.log(logging.INFO, f"function: {func_name}")
        logger.log(logging.INFO, f"positional parameters: {positional_args}")
        logger.log(logging.INFO, f"keyword parameters: {keyword_args}")
        logger.log(logging.INFO, f"return: {return_value}")

        return result
    return wrapper

@logger_decorator
def greeting():
    return None

@logger_decorator
def numbers(*args):
    return True

@logger_decorator
def student_info(**kwargs):
    return logger_decorator

greeting()
numbers(5, 10)
student_info(name="Alice", age=20, major="Computer Science")