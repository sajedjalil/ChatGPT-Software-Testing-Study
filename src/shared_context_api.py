import sys

from chatgpt_wrapper import ChatGPT
from constant import *


class SharedContextAPI:
    bot: ChatGPT = None

    def __init__(self):
        self.bot = ChatGPT()

    def get_api_response(self, input_string):
        return self.bot.ask(input_string)


if __name__ == '__main__':
    shared_context = SharedContextAPI()

    for input in sys.argv[1:]:
        print(shared_context.get_api_response(input))
        print(response_separator)
