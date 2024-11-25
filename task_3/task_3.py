import unittest
import math

def time_to_cyclic(hour: int) -> tuple:
    """
    Convert a given hour into sine and cosine components to represent time cyclically.

    Args:
    hour (int): The hour of the day (0-23).

    Returns:
    tuple: The sine and cosine values for the given hour.
    
    Raises:
    ValueError: If the hour is not between 0 and 23.
    """
    # Ensure the hour is within the valid range
    if not (0 <= hour < 24):
        raise ValueError("Hour must be in the range [0, 23]")

    # Calculate sine and cosine values based on the hour's position on the 24-hour cycle
    time_sin = math.sin(2 * math.pi * hour / 24)
    time_cos = math.cos(2 * math.pi * hour / 24)
    return time_sin, time_cos


# Unit tests to verify the correctness of the transformation
class TestTimeToCyclic(unittest.TestCase):

    def test_midnight(self):
        """Test the transformation for midnight (00:00)."""
        sin, cos = time_to_cyclic(0)
        self.assertAlmostEqual(sin, 0, places=5)  # Sine should be close to 0
        self.assertAlmostEqual(cos, 1, places=5)  # Cosine should be close to 1

    def test_noon(self):
        """Test the transformation for noon (12:00)."""
        sin, cos = time_to_cyclic(12)
        self.assertAlmostEqual(sin, 0, places=5)  # Sine should be close to 0
        self.assertAlmostEqual(cos, -1, places=5)  # Cosine should be close to -1

    def test_six_am(self):
        """Test the transformation for 6:00 AM."""
        sin, cos = time_to_cyclic(6)
        self.assertAlmostEqual(sin, 1, places=5)  # Sine should be close to 1
        self.assertAlmostEqual(cos, 0, places=5)  # Cosine should be close to 0

    def test_six_pm(self):
        """Test the transformation for 6:00 PM."""
        sin, cos = time_to_cyclic(18)
        self.assertAlmostEqual(sin, -1, places=5)  # Sine should be close to -1
        self.assertAlmostEqual(cos, 0, places=5)  # Cosine should be close to 0

    def test_wrap_around(self):
        """Test the cyclic wrap-around property between 23:00 and 01:00."""
        sin_23, cos_23 = time_to_cyclic(23)
        sin_1, cos_1 = time_to_cyclic(1)
        distance = math.sqrt((sin_23 - sin_1) ** 2 + (cos_23 - cos_1) ** 2)
        self.assertLess(distance, 0.55)  # Should be close, as these hours are cyclically near

    def test_invalid_hour(self):
        """Ensure invalid hours (outside 0-23 range) raise a ValueError."""
        with self.assertRaises(ValueError):
            time_to_cyclic(-1)
        with self.assertRaises(ValueError):
            time_to_cyclic(24)

if __name__ == "__main__":
    unittest.main()
