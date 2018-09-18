class Harness():
    "Class for holding a test harness"

    def __init__(self):
        "Constructor"
        self.test_suite = []
        self.true_positives = 0
        self.true_negatives = 0
        self.false_positives = 0
        self.false_negatives = 0

    def add_test(self, test):
        "Adding a test"
        self.test_suite.append(test)

    def run_tests(self):
        "Running all tests"
        for test in self.test_suite:
            try:
                if (test.run_test() == ('T', 'T')): # true positive
                    self.true_positives += 1
                elif (test.run_test() == ('F', 'F')): # true negative
                    self.true_negatives += 1
                elif (test.run_test() == ('T', 'F')): # false positive
                    self.false_positives += 1
                elif (test.run_test() == ('F', 'T')): # false negative
                    self.false_negatives += 1
            except Exception:
                pass

        return (self.true_positives, self.true_negatives, self.false_positives, self.false_negatives)

    def calculate_precision(self):
        """
        precision = true positive / (true positive + false positive)
        """
        return (self.true_positives / (self.true_positives + self.false_positives))

    def calculate_recall(self):
        """
        recall = true positives / (true positives + false negatives)
        """
        return (self.true_positives / (self.true_positives + self.false_negatives))

    def calculate_accuracy(self):
        """
        accuracy = (true positives + true negatives) / number of tests
        """
        return ((self.true_positives + self.true_negatives) / len(self.test_suite))

    def calculate_specificity(self):
        """
        specificity = (true negatives / (true negatives + false positives))
        """
        return (self.true_negatives / (self.true_negatives + self.false_positives))


