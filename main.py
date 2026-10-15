from bicycle import Bicycle


def main():
  print("=== Bicycle Rental System Demonstration ===\n")

  # Instantiating 4 bicycle objects (including one via classmethod)
  bike1 = Bicycle("B001", "Trek", "Marlin 5", 25.0)
  bike2 = Bicycle("B002", "Giant", "Escape 3", 20.0)
  bike3 = Bicycle("B003", "Specialized", "Allez", 45.0)
  bike4 = Bicycle.from_string("B004,Cannondale,Trail 7,30.0")

  bikes = [bike1, bike2, bike3, bike4]

  print("Initial Fleet Status:")
  for b in bikes:
    print(
        f"- ID: {b.item_id}, {b.brand} {b.model}, Rate: €{b.daily_rate:.2f}/day,"
        f" Rented: {b.is_rented}"
    )

  print("\n--- Successful Operations ---")
  try:
    print(f"Renting bicycle {bike1.item_id}...")
    bike1.rent_bicycle()
    print(f"Status of {bike1.item_id} is rented: {bike1.is_rented}")

    days = 4
    cost = bike1.calculate_rental_cost(days)
    print(
        f"Rental cost for {days} days on {bike1.brand} {bike1.model}:"
        f" €{cost:.2f}"
    )

    print(f"Returning bicycle {bike1.item_id}...")
    bike1.return_bicycle()
    print(f"Status of {bike1.item_id} is rented: {bike1.is_rented}")
  except Exception as e:
    print(f"Unexpected error: {e}")

  print("\n--- Unsuccessful Operations & Exception Handling ---")

  # 1. Renting an already rented bike
  try:
    print(f"Renting {bike2.item_id} twice:")
    bike2.rent_bicycle()
    print(f"First rental successful. Attempting to rent again...")
    bike2.rent_bicycle()
  except ValueError as e:
    print(f"Caught expected error: {e}")

  # 2. Returning a bike that isn't rented
  try:
    print(f"\nAttempting to return unrented bike {bike1.item_id}:")
    bike1.return_bicycle()
  except ValueError as e:
    print(f"Caught expected error: {e}")

  # 3. Invalid daily rate
  try:
    print(f"\nAttempting to create a bike with negative rate:")
    Bicycle("B999", "BadBrand", "BadModel", -10.0)
  except ValueError as e:
    print(f"Caught expected error: {e}")

  # 4. Invalid rental duration calculation
  try:
    print(f"\nAttempting to calculate cost for -3 days:")
    bike3.calculate_rental_cost(-3)
  except ValueError as e:
    print(f"Caught expected error: {e}")

  print("\n=== Demonstration Completed ===")


if __name__ == "__main__":
  main()