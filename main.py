import streamlit as st

st.markdown("# Unit Converter - [Abdullah Sheikh](https://github.com/AbdullahSheikh7)")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

if category == "Length":
  units = ["Meters", "Kilometers", "Feet", "Miles"]
elif category == "Weight":
  units = ["Kilograms", "Grams", "Pounds", "Ounces"]
else:
  units = ["Celsius", "Fahrenheit", "Kelvin"]

with st.container():
  from_unit = st.selectbox("From Unit", units)
  to_units = units
  to_units.remove(from_unit)
  to_unit = st.selectbox("To Unit", to_units)

value = st.number_input(f"Enter value in {from_unit}", min_value=0.0, format="%.2f")

def convert(value, from_unit, to_unit, category):
  if category == "Length":
    conversions = {
      ("Meters", "Kilometers"): value / 1000,
      ("Meters", "Feet"): value * 3.28084,
      ("Meters", "Miles"): value * 0.000621371,
      ("Kilometers", "Meters"): value * 1000,
      ("Kilometers", "Feet"): value * 3280.84,
      ("Kilometers", "Miles"): value * 0.621371,
      ("Feet", "Meters"): value / 3.28084,
      ("Feet", "Kilometers"): value / 3280.84,
      ("Feet", "Miles"): value / 5280,
      ("Miles", "Meters"): value / 0.000621371,
      ("Miles", "Kilometers"): value / 0.621371,
      ("Miles", "Feet"): value * 5280,
    }

  elif category == "Weight":
    conversions = {
      ("Kilograms", "Grams"): value * 1000,
      ("Kilograms", "Pounds"): value * 2.20462,
      ("Kilograms", "Ounces"): value * 35.274,
      ("Grams", "Kilograms"): value / 1000,
      ("Grams", "Pounds"): value * 0.00220462,
      ("Grams", "Ounces"): value * 0.035274,
      ("Pounds", "Kilograms"): value / 2.20462,
      ("Pounds", "Grams"): value / 0.00220462,
      ("Pounds", "Ounces"): value * 16,
      ("Ounces", "Kilograms"): value / 35.274,
      ("Ounces", "Grams"): value / 0.035274,
      ("Ounces", "Pounds"): value / 16,
    }

  elif category == "Temperature":
    if from_unit == "Celsius":
      if to_unit == "Fahrenheit":
        return value * 9/5 + 32
      elif to_unit == "Kelvin":
        return value + 273.15

    elif from_unit == "Fahrenheit":
      if to_unit == "Celsius":
        return (value - 32) * 5/9
      elif to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15

    elif from_unit == "Kelvin":
      if to_unit == "Celsius":
        return value - 273.15
      elif to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

  return conversions.get((from_unit, to_unit), "Conversion not available")

result = convert(value, from_unit, to_unit, category)

if result != "Conversion not available":
  st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
else:
  st.error(result)
