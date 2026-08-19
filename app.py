"""
app.py
Streamlit web version of the carbon footprint calculator.
Run locally with: streamlit run app.py
"""

import streamlit as st

# ---- Emission factors (kg CO2 per unit) ----
ELECTRICITY_FACTOR = 0.82
CAR_FACTOR = 0.21
BIKE_FACTOR = 0.10
BUS_FACTOR = 0.05
FLIGHT_FACTOR = 0.15

DIET_FACTORS = {
    "Non-vegetarian": 2.5,
    "Vegetarian": 1.7,
    "Vegan": 1.5,
}
# ----------------------------------------------

st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌍")

st.title("🌍 Carbon Footprint Calculator")
st.write(
    "Estimate your yearly carbon footprint based on electricity use, "
    "travel habits, and diet. Built as part of my BTech in Climate Change."
)

st.header("Your usage")

monthly_electricity_kwh = st.number_input(
    "Average monthly electricity use (kWh)", min_value=0.0, value=200.0, step=10.0
)
weekly_car_km = st.number_input(
    "Weekly car travel distance (km)", min_value=0.0, value=0.0, step=5.0
)
weekly_bike_km = st.number_input(
    "Weekly two-wheeler distance (km)", min_value=0.0, value=0.0, step=5.0
)
weekly_bus_km = st.number_input(
    "Weekly bus/public transport distance (km)", min_value=0.0, value=0.0, step=5.0
)
yearly_flight_km = st.number_input(
    "Approx. total flight distance per year (km)", min_value=0.0, value=0.0, step=100.0
)
diet = st.selectbox("Diet type", list(DIET_FACTORS.keys()))

if st.button("Calculate my footprint"):
    electricity_emissions = monthly_electricity_kwh * 12 * ELECTRICITY_FACTOR
    car_emissions = weekly_car_km * 52 * CAR_FACTOR
    bike_emissions = weekly_bike_km * 52 * BIKE_FACTOR
    bus_emissions = weekly_bus_km * 52 * BUS_FACTOR
    flight_emissions = yearly_flight_km * FLIGHT_FACTOR
    diet_emissions = DIET_FACTORS[diet] * 1000

    total_kg = (electricity_emissions + car_emissions + bike_emissions +
                bus_emissions + flight_emissions + diet_emissions)
    total_tonnes = total_kg / 1000

    st.header("Your results")

    st.metric("Total yearly footprint", f"{total_tonnes:.2f} tonnes CO2e")

    st.subheader("Breakdown")
    breakdown = {
        "Electricity": electricity_emissions,
        "Car travel": car_emissions,
        "Two-wheeler travel": bike_emissions,
        "Bus travel": bus_emissions,
        "Flights": flight_emissions,
        f"Diet ({diet})": diet_emissions,
    }
    st.bar_chart(breakdown)

    india_avg = 1.9
    if total_tonnes > india_avg:
        st.warning(f"This is above the Indian average of ~{india_avg} tonnes/year.")
    else:
        st.success(f"This is below the Indian average of ~{india_avg} tonnes/year.")

st.caption(
    "Emission factors are approximate averages for India (IPCC, CEA India). "
    "Meant as an educational estimate, not a certified carbon audit."
)
