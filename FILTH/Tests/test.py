class Test:
    """
    Superclass for tests-- to implement a test, override it.
    """
    def __init__(self, actual_output, expected_output):
        "Constructor"
        self.actual_output = actual_output
        self.expected_output = expected_output
        self.result = ('F', 'F')

    def __str__(self):
        "ToString"
        return "Expected: {0} / Actual: {1}".format(self.expected_output, self.actual_output)

    def run_test(self):
        "Test running mechanism."
        try:
            if self.actual_output == self.expected_output:
                if self.actual_output == True and self.expected_output == True: # True Positive
                    self.result = ('T', 'T')
                elif self.actual_output == False and self.expected_output == False: # True Negative
                    self.result = ('F', 'F')
            else:
                if self.actual_output == True and self.expected_output == False: # False Positive
                    self.result = ('T', 'F')
                elif self.actual_output == False and self.expected_output == True: # False Negative
                    self.result = ('F', 'T')

        except Exception:
            self.result = (F, F)
        finally:
            return self.result
