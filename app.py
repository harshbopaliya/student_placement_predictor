from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model and scaler with error handling
try:
    model = joblib.load('placement_predictor_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    model = None
    scaler = None

def validate_input(data):
    """
    Validate input data in order: IQ, CGPA, 10th %, 12th %, Communication Skills
    Returns tuple of (is_valid, error_message)
    """
    try:
        # Convert all inputs to float
        values = [float(x) for x in data]

        # Validate IQ (first input)
        if not 0 <= values[0] <= 300:
            return False, "Error: IQ should be between 0 and 300"

        # Validate CGPA (second input)
        if not 1 <= values[1] <= 10:
            return False, "Error: CGPA should be between 1 and 10"

        # Validate 10th percentage (third input)
        if not 0 <= values[2] <= 100:
            return False, "Error: 10th percentage should be between 0 and 100%"

        # Validate 12th percentage (fourth input)
        if not 0 <= values[3] <= 100:
            return False, "Error: 12th percentage should be between 0 and 100%"

        # Validate communication skills (fifth input)
        if not 0 <= values[4] <= 10:
            return False, "Error: Communication skills should be between 0 and 10"

        return True, ""

    except ValueError:
        return False, "Error: All inputs must be valid numbers"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not scaler:
        return render_template('index.html', 
                               prediction_text="Error: Model or scaler not loaded. Please contact the administrator.")

    try:
        # Extract data from form
        input_values = list(request.form.values())

        # Check for empty inputs
        if not input_values:
            return render_template('index.html', prediction_text="Error: No input provided")

        # Validate input
        is_valid, error_message = validate_input(input_values)
        if not is_valid:
            return render_template('index.html', prediction_text=error_message)

        # Convert to float array and reshape
        final_features = np.array([float(x) for x in input_values]).reshape(1, -1)

        # Scale the features
        scaled_features = scaler.transform(final_features)

        # Make prediction
        prediction = model.predict(scaled_features)
        output = 'Placed' if prediction[0] == 1 else 'Not Placed'

        return render_template('index.html', prediction_text=f'Prediction: {output}')

    except Exception as e:
        return render_template('index.html', 
                               prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
