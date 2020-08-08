

class CircuitOpenException(Exception):

    def __init__(self, message):
        self.message = message


class QueueFullException(Exception):

    def __init__(self, message):
        self.message = message


class RejectedExecutionException(Exception):

    def __init__(self, message):
        self.message = message