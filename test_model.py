import unittest
from model import load_data, train_model, predict_cause

class TestFeederPrototype(unittest.TestCase):
    def test_dataset_has_expected_columns(self):
        data = load_data()
        self.assertTrue({"voltage_v", "current_a", "temperature_c", "label"}.issubset(data.columns))
        self.assertGreater(len(data), 0)

    def test_model_trains_and_predicts(self):
        data = load_data()
        model, score = train_model(data)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
        label, confidence = predict_cause(model, 230, 5, 35)
        self.assertIsInstance(label, str)
        self.assertGreaterEqual(confidence, 0.0)
        self.assertLessEqual(confidence, 1.0)

if __name__ == "__main__":
    unittest.main()
