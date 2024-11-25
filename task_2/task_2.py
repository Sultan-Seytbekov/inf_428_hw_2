import numpy as np
import unittest

def generate_random_data(mean: int, variance: int, num_samples: int) -> np.ndarray:
    """Generate random threat scores within a specified range around a mean with given variance."""
    lower_bound = max(mean - variance, 0)
    upper_bound = min(mean + variance + 1, 90)  # Ensure threat scores are within 0-90
    
    if lower_bound >= upper_bound:
        lower_bound = upper_bound - 1  # Avoid an invalid range

    return np.random.randint(lower_bound, upper_bound, num_samples)

def calculate_aggregated_threat_score(department_data: list) -> float:
    """Calculate the aggregated threat score based on department threat scores and their importance."""
    total_weighted_score = 0
    total_importance = 0

    for importance, threat_scores in department_data:
        department_mean_score = np.mean(threat_scores)  # Calculate the department's mean score
        weighted_score = department_mean_score * importance  # Weight the mean score by importance
        total_weighted_score += weighted_score
        total_importance += importance

    # Normalize the aggregated score to stay within the 0 - 90 range
    aggregated_score = total_weighted_score / total_importance
    return min(90, max(0, aggregated_score))  # Cap score at 90 and ensure it doesn't go below 0

# Unit tests to verify different scenarios
class TestAggregatedThreatScore(unittest.TestCase):

    def setUp(self):
        """Initialize the common sample size for all tests."""
        self.num_samples = 50

    def test_case1_no_outliers(self):
        """Test case where all departments have similar threat scores and equal importance."""
        data = [
            (3, generate_random_data(45, 5, self.num_samples)),
            (3, generate_random_data(50, 5, self.num_samples)),
            (3, generate_random_data(48, 5, self.num_samples)),
            (3, generate_random_data(47, 5, self.num_samples)),
            (3, generate_random_data(46, 5, self.num_samples))
        ]
        score = calculate_aggregated_threat_score(data)
        self.assertTrue(0 <= score <= 90, "Score out of range")

    def test_case2_high_variance(self):
        """Test case where some departments have high variance in threat scores."""
        data = [
            (5, generate_random_data(60, 20, self.num_samples)),
            (2, generate_random_data(30, 25, self.num_samples)),
            (1, generate_random_data(25, 30, self.num_samples)),
            (4, generate_random_data(45, 10, self.num_samples)),
            (3, generate_random_data(50, 15, self.num_samples))
        ]
        score = calculate_aggregated_threat_score(data)
        self.assertTrue(0 <= score <= 90, "Score out of range")

    def test_case3_varying_importance(self):
        """Test case where departments have different importance levels."""
        data = [
            (1, generate_random_data(20, 5, self.num_samples)),
            (2, generate_random_data(35, 5, self.num_samples)),
            (5, generate_random_data(70, 5, self.num_samples)),
            (4, generate_random_data(55, 5, self.num_samples)),
            (3, generate_random_data(45, 5, self.num_samples))
        ]
        score = calculate_aggregated_threat_score(data)
        self.assertTrue(0 <= score <= 90, "Score out of range")

    def test_case4_extreme_values(self):
        """Test case where some departments have extreme threat scores."""
        data = [
            (5, generate_random_data(85, 2, self.num_samples)),
            (5, generate_random_data(80, 2, self.num_samples)),
            (5, generate_random_data(90, 0, self.num_samples)),
            (5, generate_random_data(87, 1, self.num_samples)),
            (5, generate_random_data(86, 1, self.num_samples))
        ]
        score = calculate_aggregated_threat_score(data)
        self.assertTrue(0 <= score <= 90, "Score out of range")

    def test_case5_all_low_threat(self):
        """Test case where all departments have low threat scores."""
        data = [
            (2, generate_random_data(5, 2, self.num_samples)),
            (3, generate_random_data(10, 3, self.num_samples)),
            (1, generate_random_data(2, 1, self.num_samples)),
            (4, generate_random_data(8, 2, self.num_samples)),
            (5, generate_random_data(6, 1, self.num_samples))
        ]
        score = calculate_aggregated_threat_score(data)
        self.assertTrue(0 <= score <= 90, "Score out of range")

if __name__ == "__main__":
    unittest.main()
