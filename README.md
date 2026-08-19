# Carbon Footprint Calculator
🔗 **[Try it live](https://carbon-footprint-calculator-4pdshkc6r33pnqrkfazuzl.streamlit.app)**

A simple Python command-line tool that estimates a person's yearly carbon
footprint (in kg CO2e) based on electricity use, travel habits, and diet.

Built as a personal project alongside my B.Tech in Climate Change at
Anant National University, to apply basic carbon accounting concepts
in a small, practical tool.

## What it does

Asks the user a few questions about their:
- Monthly electricity usage
- Weekly car, two-wheeler, and bus travel
- Yearly flight distance
- Diet type (non-vegetarian / vegetarian / vegan)

...and calculates an estimated total yearly carbon footprint, broken down
by category, along with a comparison to the Indian national average.

## Sample output

```
=== Your Estimated Yearly Carbon Footprint ===
Electricity: 1,968 kg CO2e
Car travel: 1,135 kg CO2e
Two-wheeler travel: 260 kg CO2e
Bus travel: 130 kg CO2e
Flights: 0 kg CO2e
Diet (vegetarian): 1,700 kg CO2e
----------------------------------------
TOTAL: 5,193 kg CO2e  (~5.19 tonnes/year)

This is above the Indian average of ~1.9 tonnes/year.
```

## How to run it

1. Clone this repository:
   ```
   git clone https://github.com/VRAJCODES-bit/carbon-footprint-calculator.git
   cd carbon-footprint-calculator
   ```

2. Run it (no extra libraries needed — pure Python):
   ```
   python carbon_calculator.py
   ```

3. Answer the prompts with your own usage estimates.

## Emission factors used

Approximate averages for India, based on commonly cited sources
(IPCC, CEA India, published carbon footprint studies):

| Category | Factor |
|---|---|
| Electricity | 0.82 kg CO2/kWh |
| Car | 0.21 kg CO2/km |
| Two-wheeler | 0.10 kg CO2/km |
| Bus | 0.05 kg CO2/km |
| Domestic flight | 0.15 kg CO2/km |
| Non-vegetarian diet | 2.5 tonnes CO2e/year |
| Vegetarian diet | 1.7 tonnes CO2e/year |
| Vegan diet | 1.5 tonnes CO2e/year |

This is meant as an educational estimate, not a precise or certified
carbon audit.

## Tech used

- Python (no external libraries required)

## Possible next steps

- Add a simple web interface (e.g. with Streamlit)
- Let users save/compare results over time
- Add more categories (waste, shopping habits, home heating)
