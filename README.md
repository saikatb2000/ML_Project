# MPG ML Project
This project predicts the Miles Per Gallon (MPG) value for vehicles based on different parameters using a Machine Learning model. The project interface is built using Streamlit for easy and interactive user input.

![image](https://github.com/user-attachments/assets/0787976e-8645-499c-ba85-ab47f09e44c8)


Project Overview
The MPG (Miles Per Gallon) prediction model helps estimate the fuel efficiency of vehicles based on several input parameters:

Displacement (Engine Size in cubic inches)
Horsepower (Engine Power)
Weight (Vehicle Weight)
Acceleration (Vehicle Acceleration)
The model calculates the predicted MPG value using these parameters.

Features:
User-Friendly Interface: Streamlit-based UI for inputting values.
Real-Time Prediction: Displays the predicted MPG as soon as inputs are provided.
Interactive Controls: Sliders for easy adjustment of input parameters.
Screenshot

How to Run the Project
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/mpg-ml-project.git
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:
bash
Copy code
streamlit run app.py
How It Works
The model takes in four key parameters:

Displacement: Represents the engine's cylinder volume.
Horsepower: The vehicle's power output.
Weight: The total weight of the vehicle.
Acceleration: How quickly the vehicle can increase its speed.
Based on these inputs, the trained machine learning model predicts the fuel efficiency in terms of MPG.

Predicted MPG
The prediction for the entered parameters is displayed in real-time in the interface.

Tech Stack
Python
Streamlit (for UI)
Scikit-learn (for Machine Learning model)
Pandas (for data manipulation)
NumPy (for numerical calculations)
Model Training
The machine learning model was trained using a dataset of vehicles with known MPG values. The model learns patterns and relationships between the input parameters (displacement, horsepower, weight, and acceleration) and the corresponding MPG values.
