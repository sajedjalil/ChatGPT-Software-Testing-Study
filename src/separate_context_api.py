import sys
import time


from constant import Constant
from chatgpt_wrapper import ChatGPT


class SeparateContextAPI:
    bot: ChatGPT = None

    def __init__(self):
        self.bot = ChatGPT()

    def get_api_response(self, input_string):
        return self.bot.ask(input_string)


if __name__ == '__main__':
    separate_context = SeparateContextAPI()

    input = sys.argv[1]
    time.sleep( Constant.interval_delay)
    print(separate_context.get_api_response(input))
