from flask import Flask, jsonify

app = Flask(__name__)

# Hypothetical climate change data
climate_change_data = {
    "temperature_increase": 1.5,  # in degrees Celsius
    "sea_level_rise": 20,  # in centimeters
    "greenhouse_gas_levels": {
        "CO2": 415,  # in parts per million
        "Methane": 1877  # in parts per billion
    },
    "global_average_temperature": {
        "2020": 14.9,
        "2021": 15.1,
        "2022": 15.3
    }
}

@app.route('/api/climate_change', methods=['GET'])
def get_climate_change_data():
    return jsonify(climate_change_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
