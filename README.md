# Student Placement Predictor

The **Student Placement Predictor** is a machine learning web application that predicts whether a student will be placed or not based on the following input parameters:

1. **IQ** (Intelligence Quotient)  
2. **CGPA** (Cumulative Grade Point Average)  
3. **10th Percentage**  
4. **12th Percentage**  
5. **Communication Skills**

The application is hosted live at:  
👉 **[Student Placement Predictor](https://careermatch-c90f.onrender.com/)**

---

## 🚀 Features

- Easy-to-use web interface styled with CSS.  
- Validates inputs to ensure realistic data ranges.  
- Uses a Logistic Regression model to predict placement outcomes.  
- Provides real-time predictions with minimal delay.  

---

## 🖥️ How to Use

1. Visit the live app: **[https://careermatch-c90f.onrender.com/](https://careermatch-c90f.onrender.com/)**  
2. Enter the following values:
   - IQ (0 to 300)
   - CGPA (1 to 10)
   - 10th Percentage (0% to 100%)
   - 12th Percentage (0% to 100%)
   - Communication Skills (0 to 10)
3. Click the **Predict** button.
4. View the result:
   - **"Placed"**: The model predicts the student will be placed.
   - **"Not Placed"**: The model predicts the student will not be placed.

---

## 📦 Project Structure

- **`app.py`**: The Flask application containing routes and logic for predictions.  
- **`placement_predictor_model.pkl`**: The pre-trained Logistic Regression model for predictions.  
- **`scaler.pkl`**: The scaler used for input normalization.  
- **`templates/index.html`**: The front-end HTML file for user interaction.  
- **`static/style.css`**: CSS file for styling the web interface.  

---

## 🔧 Technologies Used

- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS (via `static/style.css`)  
- **Machine Learning**: Scikit-learn (Logistic Regression)  
- **Hosting**: Render  

---

## 📘 Input Validation

To ensure reliable predictions, the app validates inputs based on the following criteria:

- **IQ**: 0 to 300  
- **CGPA**: 1 to 10  
- **10th Percentage**: 0% to 100%  
- **12th Percentage**: 0% to 100%  
- **Communication Skills**: 0 to 10  

If any of these criteria are not met, an error message is displayed.

---

## 🛠️ How to Run Locally

1. Clone the repository:  
   ```bash
   git clone https://github.com/harshbopaliya/student_placement_predictor.git

2. Install dependencies:
   ```bash
    pip install -r requirements.txt
   
3. Run the application:
   ```bash
    python app.py

Open the app in your browser at http://127.0.0.1:5000/.

## 🌟 Future Enhancements

Add more features for better prediction accuracy.

Enhance the UI further with animations and responsiveness.

Support additional machine learning models for comparison.

## 🪇️ Links

Live App: **[Student Placement Predictor](https://careermatch-c90f.onrender.com/)**

Repository: **[Github Repo](https://github.com/harshbopaliya/student_placement_predictor/tree/main)**

## 🧥 Contributing

Feel free to fork the project and submit a pull request for enhancements or bug fixes.

## 📄 License

This project is licensed under the MIT License.

Enjoy using the Student Placement Predictor 🎓
