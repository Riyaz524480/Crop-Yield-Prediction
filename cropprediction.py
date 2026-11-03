#from turtle import lt

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Crop Yield Prediction", layout="wide")

st.markdown("""
<div style='text-align:center; font-size:18px; color:gray;'>
© 2026 Riyaz Ahmad & Group | 🌾 Crop Yield Prediction App
</div>
""", unsafe_allow_html=True)


st.title("🌾 Crop Yield Prediction Dashboard")



# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Crop_data.csv")

# Encode categorical data
le_soil = LabelEncoder()
le_state = LabelEncoder()

df['Soil_Type'] = le_soil.fit_transform(df['Soil_Type'])
df['State'] = le_state.fit_transform(df['State'])

# Features & Target
X = df[['Rainfall', 'Temperature', 'Soil_Type', 'Fertilizer', 'Area', 'State']]
y = df['Yield']

# Train Model
model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Sidebar Input Panel
# -----------------------------
st.sidebar.header("🔧 Input Parameters")

#rainfall = st.sidebar.slider("Rainfall (mm)", 50, 400, 180)
rainfall = st.sidebar.number_input(
    "Rainfall (mm)",
    min_value=50,
    max_value=400,
    value=180,
    step=1
)

temperature = st.sidebar.slider("Temperature (°C)", 10, 40, 25)

soil_type = st.sidebar.selectbox("Soil Type", le_soil.classes_)
fertilizer = st.sidebar.selectbox("Fertilizer Used", [0, 1])
area = st.sidebar.slider("Area (hectares)", 1.0, 5.0, 2.5)

state = st.sidebar.selectbox("State", le_state.classes_)

# Encode inputs
soil_encoded = le_soil.transform([soil_type])[0]
state_encoded = le_state.transform([state])[0]

# -----------------------------
# Layout (Columns)
# -----------------------------
col1, col2 = st.columns([1, 1])

# -----------------------------
# Prediction Section
# -----------------------------
with col1:
    st.subheader("📈 Prediction Result")

    if st.button("Predict Yield"):
        prediction = model.predict([[rainfall, temperature, soil_encoded, fertilizer, area, state_encoded]])
        st.success(f"🌱 Predicted Yield: {prediction[0]:.2f} tons/hectare")


# -----------------------------
# Intelligent Condition Messages
# -----------------------------
st.subheader("🧠 Crop Condition Analysis")

if rainfall > 250 and 20 <= temperature <= 28 and soil_type == "Loamy" and fertilizer == 1:
    st.success("✅ Excellent conditions! This is ideal for high crop production.")

elif rainfall > 180 and fertilizer == 1:
    st.info("👍 Good conditions for crop growth. Expected moderate to high yield.")

elif rainfall < 120:
    st.warning("⚠️ Low rainfall detected. Crop yield may decrease.")

elif temperature > 35:
    st.warning("🌡️ High temperature may stress crops and reduce yield.")

elif soil_type == "Sandy":
    st.warning("🌱 Sandy soil retains less water. Consider irrigation.")

else:
    st.info("ℹ️ Conditions are average. Yield may vary depending on other factors.")


# -----------------------------
# Data Visualization Section
# -----------------------------
with col2:
    st.subheader("📊 Visualizations")

    tab1, tab2, tab3 = st.tabs(["Distribution", "Rainfall vs Yield", "Area vs Yield"])

    with tab1:
        fig1 = plt.figure()

        sns.kdeplot(df[df['Soil_Type']==0]['Yield'], label="Loamy", fill=True)
        sns.kdeplot(df[df['Soil_Type']==1]['Yield'], label="Clay", fill=True)

        plt.legend()
        plt.title("Yield Distribution by Soil Type")

        st.pyplot(fig1)
    
    with tab2:
        fig2 = plt.figure()
        sns.scatterplot(x=df['Rainfall'], y=df['Yield'])
        plt.title("Rainfall vs Yield")
        st.pyplot(fig2)

    with tab3:
        fig3 = plt.figure()

        sns.kdeplot(
            x=df['Area'],
            y=df['Yield'],
            fill=True
        )

        plt.title("Area vs Yield Density")

        st.pyplot(fig3)
