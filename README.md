# MPG ML Project
This project predicts the Miles Per Gallon (MPG) value for vehicles based on different parameters using a Machine Learning model. The project interface is built using Streamlit for easy and interactive user input.

![image](https://github.com/user-attachments/assets/0787976e-8645-499c-ba85-ab47f09e44c8)


Project Overview
The MPG (Miles Per Gallon) prediction model helps estimate the fuel efficiency of vehicles based on several input parameters:
<ul>
  <li>Displacement (Engine Size in cubic inches)</li>
  <li>Horsepower (Engine Power)</li>
  <li>Horsepower (Engine Power)</li>
  <li>Weight (Vehicle Weight)</li>
  <li>Acceleration (Vehicle Acceleration)</li>
</ul>
The model calculates the predicted MPG value using these parameters.

Features:
User-Friendly Interface: Streamlit-based UI for inputting values.
Real-Time Prediction: Displays the predicted MPG as soon as inputs are provided.
Interactive Controls: Sliders for easy adjustment of input parameters.
Screenshot

How to Run the Project
<ul>
  <li>Clone the repository: git clone https://github.com/your-username/mpg-ml-project.git</li>
  <li>Install the required dependencies: pip install -r requirements.txt</li>
  <li>Run the Streamlit app: streamlit run app.py</li>
</ul>

How It Works
The model takes in four key parameters:
<ol>
  <li>Displacement: Represents the engine's cylinder volume.</li>
  <li>Horsepower: The vehicle's power output.</li>
  <li>Weight: The total weight of the vehicle.</li>
  <li>Acceleration: How quickly the vehicle can increase its speed.</li>
</ol>

Based on these inputs, the trained machine learning model predicts the fuel efficiency in terms of MPG.

Predicted MPG
The prediction for the entered parameters is displayed in real-time in the interface.

Tech Stack:
<ol>
  <li>Python</li>
  <li>Streamlit (for UI)</li>
  <li>Scikit-learn (for Machine Learning model)</li>
  <li>Pandas (for data manipulation)</li>
  <li>NumPy (for numerical calculations)</li>
  <li>Model Training</li>
</ol>
The machine learning model was trained using a dataset of vehicles with known MPG values. The model learns patterns and relationships between the input parameters (displacement, horsepower, weight, and acceleration) and the corresponding MPG values.
