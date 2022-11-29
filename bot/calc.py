import random
from random import randint
import telebot
from telebot import types
from simpleeval import simple_eval


if message.startswith("!число"):
    _, math_str = message.split(' ', 1)
    result = simple_eval(math_str)
    print(result)