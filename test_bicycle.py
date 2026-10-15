import unittest
from bicycle import Bicycle


class TestBicycleRentalSystem(unittest.TestCase):

  def setUp(self):
    self.bike = Bicycle("B100", "Trek", "Domane", 50.0)

  def test_initialization_valid(self):
    """Test 1: Successful initialization with valid attributes."""
    self.assertEqual(self.bike.item_id, "B100")
    self.assertEqual(self.bike.brand, "Trek")
    self.assertEqual(self.bike.model, "Domane")
    self.assertEqual(self.bike.daily_rate, 50.0)
    self.assertFalse(self.bike.is_rented)

  def test_initialization_invalid_rate(self):
    """Test 2: Initialization with a negative or zero daily rate raises ValueError."""
    with self.assertRaises(ValueError):
      Bicycle("B101", "Brand", "Model", 0.0)
    with self.assertRaises(ValueError):
      Bicycle("B102", "Brand", "Model", -15.0)

  def test_rent_bicycle_success(self):
    """Test 3: Renting an available bicycle changes state to True."""
    self.bike.rent_bicycle()
    self.assertTrue(self.bike.is_rented)

  def test_rent_bicycle_already_rented(self):
    """Test 4: Renting an already rented bicycle raises ValueError."""
    self.bike.rent_bicycle()
    with self.assertRaises(ValueError):
      self.bike.rent_bicycle()

  def test_return_bicycle_success(self):
    """Test 5: Returning a rented bicycle changes state to False."""
    self.bike.rent_bicycle()
    self.bike.return_bicycle()
    self.assertFalse(self.bike.is_rented)

  def test_return_bicycle_not_rented(self):
    """Test 6: Returning a bicycle that is not rented raises ValueError."""
    with self.assertRaises(ValueError):
      self.bike.return_bicycle()

  def test_calculate_rental_cost_valid(self):
    """Test 7: Accurate calculation of rental cost for valid days."""
    cost = self.bike.calculate_rental_cost(3)
    self.assertEqual(cost, 150.0)

  def test_calculate_rental_cost_invalid_days(self):
    """Test 8: Calculating cost for zero or negative days raises ValueError."""
    with self.assertRaises(ValueError):
      self.bike.calculate_rental_cost(0)
    with self.assertRaises(ValueError):
      self.bike.calculate_rental_cost(-5)

  def test_from_string_valid(self):
    """Test 9: Creating a Bicycle using the classmethod from_string."""
    data = "B200, Scott, Speedster, 40.0"
    bike = Bicycle.from_string(data)
    self.assertEqual(bike.item_id, "B200")
    self.assertEqual(bike.brand, "Scott")
    self.assertEqual(bike.model, "Speedster")
    self.assertEqual(bike.daily_rate, 40.0)

  def test_from_string_invalid_format(self):
    """Test 10: Invalid string format in from_string raises ValueError."""
    with self.assertRaises(ValueError):
      Bicycle.from_string("B200, Scott, Speedster")  # Missing rate
    with self.assertRaises(ValueError):
      Bicycle.from_string("B200, Scott, Speedster, not_a_number")


if __name__ == "__main__":
  unittest.main()