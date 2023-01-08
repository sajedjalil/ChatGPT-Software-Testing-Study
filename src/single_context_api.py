from chatgpt_wrapper import ChatGPT
import sys
from constant import *

class SingleContextAPI():
    bot: ChatGPT = None

    def __init__(self):
        self.bot = ChatGPT()

    def get_api_response(self, input_string):
        return self.bot.ask(input_string)


if __name__ == '__main__':
    single_context = SingleContextAPI()

    for input in sys.argv[1:]:
        print(single_context.get_api_response(input))
        print(response_separator)
