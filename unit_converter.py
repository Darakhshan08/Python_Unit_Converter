import streamlit as st

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin"""
    # Convert to Kelvin first
    if from_unit == 'Celsius':
        kelvin = value + 273.15
    elif from_unit == 'Fahrenheit':
        kelvin = (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        kelvin = value
    else:
        return None
    
    # Convert from Kelvin to target unit
    if to_unit == 'Celsius':
        return kelvin - 273.15
    elif to_unit == 'Fahrenheit':
        return (kelvin - 273.15) * 9/5 + 32
    elif to_unit == 'Kelvin':
        return kelvin
    else:
        return None

# Define conversion factors (to base units)
units = {
    'Length': {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    },
    'Weight': {
        'kilograms': 1,
        'grams': 0.001,
        'milligrams': 0.000001,
        'pounds': 0.453592,
        'ounces': 0.0283495,
        'tons': 1000
    },
    'Temperature': {
        'Celsius': None,
        'Fahrenheit': None,
        'Kelvin': None
    },
    'Area': {
        'square meters': 1,
        'square kilometers': 1e6,
        'square miles': 2589988.11,
        'acres': 4046.86,
        'hectares': 10000,
        'square feet': 0.092903,
        'square inches': 0.00064516
    },
    'Volume': {
        'liters': 1,
        'milliliters': 0.001,
        'cubic meters': 1000,
        'gallons': 3.78541,
        'cubic feet': 28.3168,
        'cubic inches': 0.0163871
    },
    'Time': {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'years': 31536000  # Non-leap year approximation
    }
}

# Streamlit UI
st.title(" Unit Converter")
st.write("A comprehensive unit conversion tool with multiple measurement categories")

# Category selection
category = st.selectbox("Select Measurement Category", list(units.keys()))

# Unit selection columns
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", units[category].keys())
with col2:
    to_unit = st.selectbox("To", units[category].keys())

# Value input
value = st.number_input("Enter Value", value=0.0, format="%f")

# Conversion logic
if st.button("Convert"):
    try:
        if category == 'Temperature':
            result = convert_temperature(value, from_unit, to_unit)
        else:
            # Convert through base unit
            base_value = value * units[category][from_unit]
            result = base_value / units[category][to_unit]
        
        # Display result with appropriate formatting
        if abs(result) >= 10000 or abs(result) <= 0.001:
            st.success(f"{value} {from_unit} = {result:.4e} {to_unit}")
        else:
            st.success(f"{value} {from_unit} = {result:,.4f} {to_unit}")
            
    except Exception as e:
        st.error(f"Error in conversion: {str(e)}")

# Category descriptions
st.markdown("---")
st.markdown("**Supported Categories:**")
st.markdown("- **Length:** Meters, Kilometers, Miles, Feet, Inches")
st.markdown("- **Weight:** Kilograms, Grams, Pounds, Ounces")
st.markdown("- **Temperature:** Celsius, Fahrenheit, Kelvin")
st.markdown("- **Area:** Square meters, Hectares, Acres")
st.markdown("- **Volume:** Liters, Gallons, Cubic meters")
st.markdown("- **Time:** Seconds, Hours, Days, Years")