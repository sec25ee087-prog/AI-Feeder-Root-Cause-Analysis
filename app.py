import streamlit as st
from model import load_data, train_model, predict_cause

st.set_page_config(page_title="AI Feeder Root Cause Analysis", page_icon="⚡")
st.title("⚡ AI-Based Root Cause Analysis for Power Distribution Feeders")
st.write(
    "Educational prototype: enter feeder readings to estimate a likely condition. "
    "The bundled dataset is synthetic and is not validated for field protection decisions."
)

data = load_data()
model, accuracy = train_model(data)

with st.sidebar:
    st.header("Feeder measurements")
    voltage = st.number_input("Voltage (V)", min_value=0.0, max_value=500.0, value=230.0, step=1.0)
    current = st.number_input("Current (A)", min_value=0.0, max_value=500.0, value=5.0, step=0.5)
    temperature = st.number_input("Sensor temperature (°C)", min_value=-20.0, max_value=250.0, value=35.0, step=1.0)
    run = st.button("Analyze readings", type="primary")

st.metric("Demo model test accuracy", f"{accuracy:.0%}")
st.caption("Accuracy is measured on a held-out split of synthetic sample data; it does not represent real-world performance.")

if run:
    cause, confidence = predict_cause(model, voltage, current, temperature)
    st.subheader("Analysis result")
    st.write(f"**Estimated condition:** {cause}")
    st.write(f"**Model confidence:** {confidence:.1%}")
    st.warning(
        "This is a demonstration result, not a confirmed electrical diagnosis. "
        "Use approved protection equipment and qualified electrical personnel for real feeders."
    )

with st.expander("View sample data"):
    st.dataframe(data.head(20), use_container_width=True)
