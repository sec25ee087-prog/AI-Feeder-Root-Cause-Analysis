# Technical Design / Architecture

## Purpose
Demonstrate an AI-assisted interface that uses voltage, current, and temperature readings
to estimate a likely feeder condition from a labelled example dataset.

## Data flow
1. A user enters voltage (V), current (A), and sensor temperature (°C).
2. The Streamlit interface sends the values to the prediction function.
3. A Random Forest classifier trained on the bundled synthetic dataset predicts a class.
4. The interface displays the predicted class and model confidence.

## Prototype architecture
`Sensors (future integration) -> Microcontroller/data logger (future integration) -> CSV/API input -> ML model -> Dashboard`

## Current scope and limitations
- The included CSV is synthetic educational data, not measured utility data.
- Labels are illustrative and do not prove actual fault causes.
- A single voltage/current/temperature reading may not distinguish all fault types.
- No relay operation, automatic switching, or direct grid connection is implemented.
- Field deployment requires qualified engineering review, calibrated sensors, protection coordination,
  secure communications, validated data, and testing under applicable electrical safety rules.

## Future work
- Collect labelled measurements from a safe lab setup or approved utility source.
- Document sensor models, ratings, accuracy, mounting method, and calibration.
- Add timestamp, feeder/phase identifier, and sensor-health checks.
- Evaluate with separate real-world test data and report precision, recall, and confusion matrix.
- Add data logging and alerts only after validation.
