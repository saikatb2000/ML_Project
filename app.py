import pickle

import streamlit as st

st.title('MPG ML Project')
## 'displacement', 'horsepower', 'weight', 'acceleration'

displacement = st.number_input("Displacement", value=300, placeholder="Enter a value for displacement")
horsepower = st.number_input("Horsepower", value=130, placeholder="Enter a value for horsepower")
weight = st.number_input("Weight", value=3000, placeholder="Enter a value for weight")
acceleration = st.number_input("Acceleration", value=12, placeholder="Enter a value for acceleration")

st.write(displacement, horsepower, weight, acceleration)
loaded_model = pickle.load(open('mpg_regression.sav', 'rb'))
prediction = loaded_model.predict([[displacement,horsepower,weight,acceleration]])
st.subheader(f'Predicted mpg value for above parameter is {prediction[0]}')
# st.write(prediction)


