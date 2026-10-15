from rental_item import RentalItem


class Bicycle(RentalItem):

  def __init__(self, item_id: str, brand: str, model: str, daily_rate: float):
    if daily_rate <= 0:
      raise ValueError("Daily rate must be a positive number.")
    super().__init__(item_id, brand, model, daily_rate)

  def rent_bicycle(self):
    """Marks the bicycle as rented if it is currently available."""
    if self.is_rented:
      raise ValueError(f"Bicycle {self.item_id} is already rented.")
    self.is_rented = True

  def return_bicycle(self):
    """Marks the bicycle as available if it is currently rented."""
    if not self.is_rented:
      raise ValueError(f"Bicycle {self.item_id} is not currently rented.")
    self.is_rented = False

  def calculate_rental_cost(self, days: int) -> float:
    """Calculates total cost for a given number of days."""
    if not isinstance(days, int) or days <= 0:
      raise ValueError("Rental duration in days must be a positive integer.")
    return self.daily_rate * days

  @classmethod
  def from_string(cls, data_string: str):
    """Alternative constructor: creates a Bicycle instance from a comma-separated string

    Format: 'id,brand,model,daily_rate'
    """
    parts = [p.strip() for p in data_string.split(",")]
    if len(parts) != 4:
      raise ValueError("Invalid format. Expected 'id,brand,model,daily_rate'.")

    item_id, brand, model, rate_str = parts
    try:
      daily_rate = float(rate_str)
    except ValueError as e:
      raise ValueError("Daily rate must be a valid number.") from e

    return cls(item_id, brand, model, daily_rate)