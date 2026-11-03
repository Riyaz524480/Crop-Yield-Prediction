# 🌾 Crop Yield Prediction Dashboard

### Machine Learning Project Using Python and Streamlit

The **Crop Yield Prediction Dashboard** is an interactive machine learning application designed to predict crop yield based on agricultural parameters such as rainfall, temperature, soil type, fertilizer usage, cultivated area, and state.

The application uses **Linear Regression** to estimate crop yield and provides visualizations to explore relationships between agricultural factors and crop production.


## 🚀 Live Demo

**Live Application:** Add your deployed Streamlit URL here.

**GitHub Repository:** `https://github.com/Riyaz524480`

## 📌 Project Overview

Agricultural production depends on several environmental and farming-related factors. This project demonstrates how machine learning can be used to analyze these factors and estimate crop yield from user-provided inputs.

The dashboard allows users to enter agricultural conditions, generate a yield prediction, view crop condition messages, and explore interactive data visualizations.

## ✨ Features

- **Crop Yield Prediction:** Estimates crop yield using a trained Linear Regression model.
- **Rainfall Input:** Enter rainfall values between 50 and 400 mm.
- **Temperature Selection:** Select temperature values between 10°C and 40°C.
- **Soil Type Selection:** Choose the available soil types from the dataset.
- **Fertilizer Selection:** Specify whether fertilizer is used (0 if not used and 1 if used).
- **Cultivated Area:** Select the agricultural area in hectares.
- **State Selection:** Choose a state available in the dataset.
- **Crop Condition Analysis:** Displays rule-based messages based on rainfall, temperature, soil type, and fertilizer usage.
- **Data Visualization:** Displays yield distributions and relationships between rainfall, area, and crop yield.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming |
| Streamlit | Interactive web dashboard |
| Pandas | Dataset loading and processing |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning and categorical encoding |
| Linear Regression | Crop yield prediction |
| LabelEncoder | Encoding categorical variables |

## 📂 Project Structure

```text
CropYieldPrediction/
│
├── app.py
├── Crop_data.csv
├── requirements.txt
└── README.md
```

**Note:** Replace `app.py` with the actual filename of your Python application if it is different.

## 📊 Dataset Description

The application uses `Crop_data.csv` as its input dataset.

The dataset is expected to contain the following columns:

| Column | Description |
|---|---|
| Rainfall | Rainfall amount in millimetres |
| Temperature | Temperature in degrees Celsius |
| Soil_Type | Category representing soil type |
| Fertilizer | Fertilizer usage indicator |
| Area | Cultivated area in hectares |
| State | State associated with the agricultural record |
| Yield | Crop yield, used as the prediction target |

The dataset must contain valid values for the required columns and should be placed in the same directory as the Python application.

## ⚙️ Machine Learning Methodology

### 1. Data Loading

Pandas loads the agricultural dataset from `Crop_data.csv`.

### 2. Data Preprocessing

The `LabelEncoder` from Scikit-learn converts categorical variables such as `Soil_Type` and `State` into numerical representations.

### 3. Feature Selection

The model uses six input features:

- Rainfall
- Temperature
- Soil Type
- Fertilizer
- Area
- State

The target variable is `Yield`.

### 4. Model Training

A Linear Regression model is trained using the dataset:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
```

### 5. Prediction

When the user clicks **Predict Yield**, the application uses the selected input parameters to estimate crop yield.

### 6. Condition Analysis

The application applies predefined rules to display messages about rainfall, temperature, soil type, and fertilizer usage.

These messages are rule-based interpretations and are separate from the Linear Regression prediction.

## 📈 Visualizations

The dashboard includes three visualization tabs:

1. **Yield Distribution by Soil Type:** Uses kernel density estimation to visualize yield distributions for selected encoded soil categories.
2. **Rainfall vs Yield:** Uses a scatter plot to examine the relationship between rainfall and crop yield.
3. **Area vs Yield Density:** Uses a two-dimensional kernel density plot to explore the distribution of cultivated area and yield.

These visualizations help users explore patterns in the dataset.

## 💻 Installation and Setup

### Prerequisites

- Python 3.10 or another Python version compatible with the installed dependencies
- pip package manager
- Git (optional)

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd CropYieldPrediction
```

Replace the repository URL and directory name with your actual details.

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install the required packages directly:

```bash
pip install streamlit pandas matplotlib seaborn scikit-learn
```

### Step 3: Verify the dataset

Make sure `Crop_data.csv` is present in the project directory and contains all the required columns.

### Step 4: Run the application

If your main file is `app.py`, execute:

```bash
streamlit run app.py
```

If your file has another name, replace `app.py` with that filename.

### Step 5: Open the dashboard

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to interact with the application.

## ☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

1. Upload the application code, `Crop_data.csv`, and `requirements.txt` to a GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in using GitHub.
4. Create a new public app from your repository.
5. Select the correct branch and main Python file.
6. Click **Deploy**.
7. Add the generated public URL to the Live Demo section of this README.

Ensure that the dataset is included in the repository if the application loads it directly using `pd.read_csv("Crop_data.csv")` and the dataset is suitable for public sharing.

## 🎯 Project Objectives

- Demonstrate the practical application of machine learning in agriculture.
- Predict crop yield from selected agricultural parameters.
- Explore agricultural data through statistical visualizations.
- Build an interactive dashboard using Streamlit.
- Gain experience in data preprocessing, model training, and application deployment.

## ⚠️ Limitations

- The model's predictive performance depends on the quality, size, and representativeness of the dataset.
- The current code trains and evaluates the model on the same dataset; it does not include a separate test set or cross-validation.
- Label encoding treats categorical values as numerical codes, which may introduce an artificial ordering.
- The crop condition messages are based on manually defined rules and are not independently validated agronomic recommendations.
- Predictions should not be treated as guaranteed agricultural outcomes.

## 🔮 Future Enhancements

- Evaluate model performance using a train-test split and appropriate regression metrics.
- Compare Linear Regression with Random Forest and other regression algorithms.
- Add crop selection and fertilizer recommendations.
- Improve categorical feature encoding.
- Add model evaluation metrics and feature importance analysis.
- Improve the dashboard's design and usability.

## 👨‍💻 Author

**Riyaz Ahmad & Group**

Project: Crop Yield Prediction Dashboard

Technologies: Python, Machine Learning, Streamlit, and Data Visualization.

## 📄 License

No license has been specified for this project yet. Unless you add a license, others should not assume that they have permission to reuse, modify, or redistribute the source code.

---

*This project is developed for educational and demonstration purposes. Predictions depend on the dataset and model assumptions and should not replace expert agricultural advice.*
