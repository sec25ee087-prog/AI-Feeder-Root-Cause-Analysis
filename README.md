# AI-Based Root Cause Analysis for Power Distribution Feeders

An educational software prototype for exploring how voltage, current, and temperature readings
could support feeder-condition classification.

**Important:** The bundled data is synthetic. This prototype is for demonstration only and must not
be used to make live electrical protection, switching, or safety decisions.

## Features
- Streamlit dashboard for entering voltage, current, and temperature.
- Random Forest classifier trained on example data.
- Displays estimated class and model confidence.
- Sample CSV, architecture notes, and basic unit tests.

## Requirements
- Python 3.10 or newer
- pip

## Setup
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Create a virtual environment (recommended):
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the dashboard: `streamlit run app.py`
6. Open the local URL printed in the terminal.

## Run tests
`python -m unittest discover -s tests -v`

## Data format
`data/sample_data.csv` contains:
- `voltage_v`: voltage in volts
- `current_a`: current in amperes
- `temperature_c`: temperature in degrees Celsius
- `label`: illustrative condition label

## Environment variables
No environment variables or API keys are required by this demo.

## Architecture
See `docs/architecture.md`.

## Suggested repository checklist
- [x] README with setup steps
- [x] Technical design document
- [x] Sample data and tests
- [x] License file
- [ ] Replace synthetic data with validated, properly labelled measurements before claiming field accuracy
- [ ] Add sensor wiring, calibration, installation, and safety documentation before hardware deployment

## License
Released under the MIT License; see `LICENSE`.
