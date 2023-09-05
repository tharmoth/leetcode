import time

class Foo:

    def __init__(self):
        self.first_fired = False
        self.second_fired = False

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.first_fired = True

    def second(self, printSecond: 'Callable[[], None]') -> None:

        while not self.first_fired:
            time.sleep(.001)

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.second_fired = True

    def third(self, printThird: 'Callable[[], None]') -> None:

        while not self.first_fired or not self.second_fired:
            time.sleep(.001)

        # printThird() outputs "third". Do not change or remove this line.
        printThird()

# Im not going to bother with implmementing the main right now