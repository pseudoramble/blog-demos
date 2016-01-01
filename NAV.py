class NAV:
    """
     Our first example of a Python built-in. This should be familiar if you've implemented a class before.
     This completes some of what a constructor would provide in other languages.
    """
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price

    """
     Okay, so now we know we want to implement the greater-than operator (>). Let's do it!
     We'll only compare the same ticker to itself. Otherwise, we'll say that this isn't implemented.
     
     One nice feature in this implementation - We just delegated the real work to the Real implementation
      of __gt__ (https://docs.python.org/3.5/library/numbers.html#numbers.Real)
    """
    def __gt__(self, other):
        if self.ticker == other.ticker:
            return self.price > other.price
        else:
            return NotImplemented

