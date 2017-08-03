#coding=utf-8

quotes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')


class QuoteModel:
    def __init__(self):
        self.view = QuoteTerminalView()

    def get_quote(self):
        try:
            n = self.view.select_quote()
            n = int(n)
        except Exception as err:
            self.view.error("Incorrect index '{}'".format(n))
        try:
            if n >= 1:
                value = quotes[n]
            else:
                value = 'number must >= 1'
        except Exception as err:
            value = 'Not found!'
        return value


class QuoteTerminalView:
    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            quote = self.model.get_quote()
            valid_input = True
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while 1:
        controller.run()


if __name__ == '__main__':
    main()