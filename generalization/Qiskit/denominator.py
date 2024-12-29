from flask import Flask, request, jsonify
from fractions import Fraction

# Define the function
def denominator(decimal_value, n, N):
    return (Fraction(decimal_value / 2**(n*2)).limit_denominator(N)).denominator

# Create the Flask app
app = Flask(__name__)

@app.route('/denominator', methods=['POST'])
def denominator_endpoint():
    try:
        # Parse JSON input
        data = request.get_json()
        
        # Extract parameters
        decimal_value = data.get('decimal_value')
        n = data.get('n')
        N = data.get('N')

        # Validate parameters
        if not all(isinstance(param, (int, float)) for param in [decimal_value, n]) or not isinstance(N, int):
            return jsonify({'error': 'Invalid input. Ensure decimal_value and n are numbers, and N is an integer.'}), 400

        # Compute the result
        result = denominator(decimal_value, n, N)

        # Return the result as JSON
        return jsonify({'denominator': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
