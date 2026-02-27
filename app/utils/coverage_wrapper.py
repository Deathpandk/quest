import os
import sys

from coverage import Coverage


class TestEnv:
    COVERAGE_MINIMUM = 80

    def __init__(self):
        self.test_running = self.is_test_running()
        if self.test_running:
            os.environ.setdefault("ENV", "test")
            self.cov = Coverage()
            self.cov.erase()
            self.cov.start()

    @classmethod
    def is_test_running(cls):
        try:
            return sys.argv[1] == "test"
        except IndexError:
            return False

    def finish(self):
        if self.test_running:
            self.cov.stop()
            self.cov.save()
            self.cov.html_report()
            covered = self.cov.report()
            print(f"Coverage minimum at {self.COVERAGE_MINIMUM}%, current: {round(covered, 2)}%")
            if covered < self.COVERAGE_MINIMUM:
                print("Failed due to coverage")
                sys.exit(1)
