"""
carbon_calculator.py
A simple command-line tool that estimates a person's yearly carbon
footprint (in kg CO2e) based on electricity use, travel, and diet.

Emission factors are approximate, commonly-cited averages for India
(sources: IPCC, CEA India, published carbon footprint studies).
Meant as an educational estimate, not a precise/certified measurement.
"""

# ---- Emission factors (kg CO2 per unit) ----
ELECTRICITY_FACTOR = 0.82      # kg CO2 per kWh (India grid average)
CAR_FACTOR = 0.21              # kg CO2 per km (average petrol car)
BIKE_FACTOR = 0.10             # kg CO2 per km (two-wheeler)
BUS_FACTOR = 0.05              # kg CO2 per km (public bus, per passenger)
FLIGHT_FACTOR = 0.15           # kg CO2 per km (domestic flight, per passenger)

DIET_FACTORS = {
    "non-vegetarian": 2.5,     # tonnes CO2e per year (approx.)
    "vegetarian": 1.7,
    "vegan": 1.5,
}
# ----------------------------------------------


def get_number(prompt):
    """Asks for a number, keeps asking until the input is valid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_diet_choice():
    print("\nDiet type:")
    print("1. Non-vegetarian")
    print("2. Vegetarian")
    print("3. Vegan")
    choice = input("Choose 1, 2, or 3: ").strip()
    mapping = {"1": "non-vegetarian", "2": "vegetarian", "3": "vegan"}
    return mapping.get(choice, "vegetarian")


def calculate_footprint():
    print("=== Carbon Footprint Calculator ===\n")

    monthly_electricity_kwh = get_number("Average monthly electricity use (kWh): ")
    weekly_car_km = get_number("Weekly car travel distance (km, 0 if none): ")
    weekly_bike_km = get_number("Weekly two-wheeler distance (km, 0 if none): ")
    weekly_bus_km = get_number("Weekly bus/public transport distance (km, 0 if none): ")
    yearly_flight_km = get_number("Approx. total flight distance per year (km, 0 if none): ")
    diet = get_diet_choice()

    # Yearly calculations
    electricity_emissions = monthly_electricity_kwh * 12 * ELECTRICITY_FACTOR
    car_emissions = weekly_car_km * 52 * CAR_FACTOR
    bike_emissions = weekly_bike_km * 52 * BIKE_FACTOR
    bus_emissions = weekly_bus_km * 52 * BUS_FACTOR
    flight_emissions = yearly_flight_km * FLIGHT_FACTOR
    diet_emissions = DIET_FACTORS[diet] * 1000  # convert tonnes to kg

    total_kg = (electricity_emissions + car_emissions + bike_emissions +
                bus_emissions + flight_emissions + diet_emissions)
    total_tonnes = total_kg / 1000

    # ---- Results ----
    print("\n=== Your Estimated Yearly Carbon Footprint ===")
    print(f"Electricity: {electricity_emissions:,.0f} kg CO2e")
    print(f"Car travel: {car_emissions:,.0f} kg CO2e")
    print(f"Two-wheeler travel: {bike_emissions:,.0f} kg CO2e")
    print(f"Bus travel: {bus_emissions:,.0f} kg CO2e")
    print(f"Flights: {flight_emissions:,.0f} kg CO2e")
    print(f"Diet ({diet}): {diet_emissions:,.0f} kg CO2e")
    print("-" * 40)
    print(f"TOTAL: {total_kg:,.0f} kg CO2e  (~{total_tonnes:.2f} tonnes/year)")

    # Simple comparison for context
    india_avg = 1.9  # tonnes CO2e per person per year (approx. national average)
    if total_tonnes > india_avg:
        print(f"\nThis is above the Indian average of ~{india_avg} tonnes/year.")
    else:
        print(f"\nThis is below the Indian average of ~{india_avg} tonnes/year.")


if __name__ == "__main__":
    calculate_footprint()
