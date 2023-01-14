import sys
import time

from chatgpt_wrapper import ChatGPT
from constant import Constant


class SharedContextAPI:
    bot: ChatGPT = None

    def __init__(self):
        self.bot = ChatGPT()

    def get_api_response(self, input_string):
        return self.bot.ask(input_string)


if __name__ == '__main__':
    shared_context = SharedContextAPI()

    for input in sys.argv[1:]:
        time.sleep(Constant.interval_delay)
        print(shared_context.get_api_response(input))
        print(Constant.response_separator)
