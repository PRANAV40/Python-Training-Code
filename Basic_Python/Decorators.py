# Decorator using func under func
# def outer_func(func):
#     def inner_func():
#         print("This is inner func.")
#         return func()
#
#     print("Before Return.")
#     return inner_func
#
#
# def argument_func():
#     print("This is argument func.")
#
#
# variable_outer_func = outer_func(argument_func)
# print("Before executing variable outer func.")
# variable_outer_func()

# Decorator by using @ sign
# def outer_func(func):
#     def inner_func():
#         print("This is Inner Func. ")
#         return func()
#
#     print("Before Return")
#     return inner_func
#
#
# @outer_func
# def argument_func():
#     print("This is argument func. ")
#
#
# argument_func()


# Real time example of decorators using cron jobs
import time
from datetime import datetime


def log_datetime_decorator(func):
    '''Log the date and time of a function'''

    def wrapper_func():
        print(f"Function: {func.__name__}")
        print(f"Run on: {datetime.today().strftime('%y-%m-%d %H:%M:%S')}")
        print(f'{"-------------------------"}')
        func()
    return wrapper_func


@log_datetime_decorator
def daily_cron_job():
    time.sleep(9)
    print("Daily cron jobs finished.")


@log_datetime_decorator
def weekly_cron_jobs():
    time.sleep(40.5)
    print("Weekly cron jobs finished.")


@log_datetime_decorator
def monthly_cron_jobs():
    time.sleep(2.1)
    print("Monthly cron jobs finished.")


daily_cron_job()
weekly_cron_jobs()
monthly_cron_jobs()
daily_cron_job()
