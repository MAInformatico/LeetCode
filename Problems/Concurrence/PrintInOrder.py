import threading
class Foo:
    def __init__(self):
        self.print_lock=threading.Lock()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.print_lock:
        # printFirst() outputs "first". Do not change or remove this line.
            printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.print_lock:
        # printSecond() outputs "second". Do not change or remove this line.
            printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.print_lock:
        # printThird() outputs "third". Do not change or remove this line.
            printThird()
