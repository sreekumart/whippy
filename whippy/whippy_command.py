from threading import Lock
from whippy.exception.whippy_exception import CircuitOpenException
import concurrent.futures
from whippy.whippy_config import WhippyConfig


class WhippyCommand:

    _default_config = WhippyConfig()

    def __init__(self, config=_default_config):
        self.error_threshold = 5
        self.max_thread_pool_size = 10
        self.max_queue_size = 10
        self.circuit_open = False
        self.auto_reset = False
        self.lock = Lock()
        self.current_error_count = 0
        self.current_queue_size = 0
        self.max_time_out = 5
        self.child_thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers=self.max_thread_pool_size)

    def execute(self, func):
        def run(*args, **kwargs):
            self.lock.acquire()
            try:
                if self.current_error_count >= self.error_threshold or self.circuit_open:
                    raise CircuitOpenException('Circuit Open: Error Threshold Exceeded')
            finally:
                self.lock.release()
            try:
                child_thread_result = self.child_thread_executor.submit(func, *args)
                child_thread_result.result(self.max_time_out)
            except concurrent.futures.TimeoutError:
                self._update_execute_failure()
                raise concurrent.futures.TimeoutError('TimeOutError')
            except Exception as exception:
                self._update_execute_failure()
                raise exception
            else:
                self._update_execute_success()
                return child_thread_result.result()
        return run

    def _update_execute_success(self):
        self.lock.acquire()
        if self.current_error_count > 0:
            self.current_error_count -= 1
        if self.current_error_count < self.error_threshold:
            self.circuit_open = False
        self.lock.release()

    def _update_execute_failure(self):
        self.lock.acquire()
        self.current_error_count += 1
        if self.current_error_count >= self.error_threshold:
            self.circuit_open = True
        self.lock.release()

    def queue(self):
        pass








