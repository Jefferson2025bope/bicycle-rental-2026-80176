from abc import ABC, abstractmethod


class RentalItem(ABC):
  """Abstract base class representing any rental item in the shop."""

  def __init__(self, item_id: str, brand: str, model: str, daily_rate: float):
    self.item_id = item_id
    self.brand = brand
    self.model = model
    self.daily_rate = daily_rate
    self.is_rented = False

  @abstractmethod
  def calculate_rental_cost(self, days: int) -> float:
    """Calculate rental cost based on duration."""
    pass

  @classmethod
  @abstractmethod
  def from_string(cls, data_string: str):
    """Alternative constructor from a delimited string."""
    pass