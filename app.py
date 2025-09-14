from flask import Flask, request, jsonify
from hmpi_calculator import calculate_indices

app = Flask(__name__)

@app.route('/api/hmpi/calculate', methods=['POST'])
def calculate_hmpi():
    data = request.get_json()
    heavy_metal_concentrations = data.get('heavyMetalConcentrations')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not heavy_metal_concentrations or not isinstance(heavy_metal_concentrations, dict):
        return jsonify({'error': 'Invalid input: heavyMetalConcentrations is required and should be an object with metal concentrations.'}), 400

    indices_result = calculate_indices(heavy_metal_concentrations)
    if latitude is not None:
        indices_result['latitude'] = latitude
    if longitude is not None:
        indices_result['longitude'] = longitude
    return jsonify(indices_result), 200

if __name__ == '__main__':
    app.run(port=3001, debug=True)
