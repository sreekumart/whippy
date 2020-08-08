from threading import Lock


class WhippyConfig:

    def __init__(self):
        self.error_threshold = 5
        self.max_thread_pool_size = 10
        self.max_queue_size = 10
        self.circuit_open = False
        self.auto_reset = False
        self.lock = Lock()
        self.current_error_count = 0
        self.current_queue_size = 0
        self.max_time_out = 5





