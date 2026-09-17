import streamlit as st
import joblib

model=joblib.load("multilinear_regression_house_price.pkl")
st.title("House Price Prediction")
area=st.number_input("Enter Area:", min_value=600.0 ,max_value=3000.0, value=600.0)
bedrooms=st.number_input("Enter no of bedrooms:", min_value=1 ,max_value=4, value=3)
floors=st.number_input("Enter no of floors:", min_value=0 ,max_value=10, value=1)

if st.button("Predict"):
   if bedrooms < 1 or bedrooms > 4:
     st.error("Please enter the number of bedrooms between 1 and 4.")
   elif floors < 0 or floors > 10:
     st.error("Please enter the number of floors between 0 and 10.")
   elif area < 600.0 or area > 3000.0:
     st.error("Please enter the area between 600 and 3000.")
   else:  
    prediction=model.predict([[area,bedrooms,floors]])
    st.success(f"Predicted price: {prediction[0]:.2f} Lakhs")
