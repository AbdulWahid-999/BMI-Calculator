import streamlit as st

# Title
st.title("💪 BMI Calculator")
st.write("This app calculates your Body Mass Index (BMI) based on your height and weight.")

# Choose input method
input_method = st.radio("Choose Input Method", ("Sliders", "Manual Input"))

# Height and Weight Inputs
if input_method == "Sliders":
    height = st.slider("Enter your height (in cm)", 100, 250, 170)
    weight = st.slider("Enter your weight (in Kg)", 30, 200, 70)
else:
    height = st.number_input("Enter your height (in cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("Enter your weight (in Kg)", min_value=30, max_value=200, value=70)

# BMI Calculation
cal_bmi = weight / ((height / 100) ** 2)

# Determine BMI Category
if cal_bmi < 18.5:
    category = "Underweight"
    color = "blue"
elif 18.5 <= cal_bmi < 24.9:
    category = "Normal weight"
    color = "green"
elif 25 <= cal_bmi < 29.9:
    category = "Overweight"
    color = "orange"
else:
    category = "Obesity"
    color = "red"

# Display BMI Result
st.markdown(f"## Your BMI: **{cal_bmi:.1f}**")
st.markdown(f"### Your BMI Category: <span style='color:{color}; font-size:24px;'>{category}</span>", unsafe_allow_html=True)

# Add a BMI Progress Bar (scales BMI to 100)
st.progress(min(int(cal_bmi * 2.5), 100))

# BMI Chart Image
st.image("https://www.researchgate.net/profile/Pratik-Gada/publication/336145476/figure/fig1/AS:811747364724736@1569918960322/BMI-Chart.png", width=500)

# Health Tips Based on BMI Category
tips = {
    "Underweight": "📌 Consider increasing your calorie intake with nutritious foods.",
    "Normal weight": "✅ Great! Maintain a balanced diet and regular exercise.",
    "Overweight": "⚠️ Try incorporating more physical activity and mindful eating habits.",
    "Obesity": "🚨 Consider consulting a healthcare professional for personalized guidance."
}
st.info(tips[category])

# Reset Button
if st.button("Reset"):
    st.rerun()
