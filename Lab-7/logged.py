import logging


def logged(exception, mode="file"):
    def decorator(method):
        def wrapper(*args, **kwargs):
            try:
                result = method(*args, **kwargs)
                return result
            except exception as e:
                if mode == "console":
                    logging.error(f"Exception {exception.__name__}: {str(e)}")
                elif mode == "file":
                    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
                    logging.error(f"Exception {exception.__name__}: {str(e)}")
                else:
                    raise ValueError("Invalid logging mode")
        return wrapper
    return decorator
