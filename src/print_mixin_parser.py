class PrintMixin:
    """Mixin class for string representation"""

    def __str__(self):
        return f"{type(self).__name__}, url: {self.url}, headers: {self.headers}, params: {self.params}"
