from flask import Flask, request, jsonify
from fractions import Fraction

def denominator(decimal_value, n, N):
    return (Fraction(decimal_value / 2**(n*2)).limit_denominator(N)).denominator
app = Flask(__name__)

@app.route('/denominator', methods=['POST'])
def denominator_endpoint():
    try:
        data = request.get_json()
        decimal_value = data.get('decimal_value')
        n = data.get('n')
        N = data.get('N')

        if not all(isinstance(param, (int, float)) for param in [decimal_value, n]) or not isinstance(N, int):
            return jsonify({'error': 'Invalid input. Ensure decimal_value and n are numbers, and N is an integer.'}), 400
        result = denominator(decimal_value, n, N)
        return jsonify({'denominator': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
