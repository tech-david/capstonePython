import unittest
import numpy as np
from model.regression.LogisticModel import get_cv_results, what_best_model, best_score_after_tscv


class MyTestCase(unittest.TestCase):
    def test_model(self):
        model = what_best_model()
        results = get_cv_results()
        model_results = results['params']
        score = best_score_after_tscv()
        # Test case: Trains best model
        # Checking score is maximum score
        self.assertEqual(score,
                         np.max(results['mean_test_score']),
                         "Score should be maximum of results")
        # Checking the solver in the model exists in the model selectort
        self.assertIn(model.solver,
                      [key for i in model_results for key in i.values()],
                      "Solver must exist in the list of results")


if __name__ == '__main__':
    unittest.main()
