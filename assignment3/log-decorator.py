# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
...
# To write a log record:
logger.log(logging.INFO, "this string would be logged")

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        positional_args = list(args) if args else "none"
        keyword_args = kwargs if kwargs else "none"

        result = func(*args, **kwargs)

        log_message = (
            f"function: {func_name}, "
            f"positional args: {positional_args}, "
            f"keyword args: {keyword_args}, "
            f"result: {result}"
        )

        logger.log(logging.INFO, log_message)

        return result
    return wrapper

@logger_decorator
def greeting():
    print("Hello, World!")

@logger_decorator
def numbers(num1, num2):
    compare = type(num1) == type(num2)
    print(f"Are the two numbers of the same type? {compare}")
    
@logger_decorator
def student_info(**kwargs):
    info = ",".join([f"{key}={value}" for key, value in kwargs.items()])
    print(f"Student Information: {info}")

greeting()
numbers(5, 10)
student_info(name="Alice", age=20, major="Computer Science")