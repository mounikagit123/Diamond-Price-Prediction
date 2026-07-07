# 💎 Diamond Price Prediction using Machine Learning

An end-to-end Machine Learning application that predicts the market price of a diamond based on its physical characteristics. The project uses a **CatBoost Regressor** for prediction and is deployed as an interactive **Streamlit** web application.

---

## 📖 Project Overview

Diamond pricing depends on several factors such as carat, cut, color, clarity, depth, and dimensions. Estimating the price manually can be difficult due to the complex relationship between these features.

This project builds a regression model that learns these relationships from historical diamond data and predicts the price of unseen diamonds with high accuracy.

The application provides a simple web interface where users can enter diamond specifications and instantly receive a predicted price.

---

## 🚀 Features

- Interactive Streamlit web application
- Real-time diamond price prediction
- CatBoost Regressor model
- Complete Machine Learning pipeline
- Input validation
- Model serialization using Joblib
- Fast predictions using a cached model

---

## 📊 Dataset

The project is trained using the **Diamonds Dataset** containing information about thousands of diamonds.

### Input Features

| Feature | Description |
|----------|-------------|
| Carat | Weight of the diamond |
| Cut | Diamond cut quality |
| Color | Diamond color grade |
| Clarity | Diamond clarity grade |
| Depth | Total depth percentage |
| Table | Table width percentage |
| x | Length (mm) |
| y | Width (mm) |
| z | Height (mm) |

**Target Variable**

- Price

---

## ⚙️ Machine Learning Workflow

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Ordinal Encoding
        │
        ▼
Train-Test Split
        │
        ▼
Model Training
        │
        ▼
Hyperparameter Tuning
        │
        ▼
Cross Validation
        │
        ▼
Model Evaluation
        │
        ▼
Pipeline Serialization
        │
        ▼
Streamlit Deployment
```

---

## 🤖 Machine Learning Model

**Algorithm Used**

- CatBoost Regressor

The model was selected after comparing multiple regression algorithms based on prediction accuracy and generalization performance.

---

## 📈 Model Performance

### Test Dataset

| Metric | Value |
|---------|--------|
| R² Score | **0.9825** |
| MAE | **278.79** |
| RMSE | **524.55** |

### Validation Dataset

| Metric | Value |
|---------|--------|
| R² Score | **0.9838** |
| MAE | **286.02** |
| RMSE | **518.81** |

These results demonstrate that the model generalizes well to unseen data with similar characteristics.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- CatBoost
- Streamlit
- Joblib
- Git
- GitHub

---

## 📂 Project Structure

```
Diamond-Price-Prediction
│
├── app.py
├── diamond_pipeline.pkl
├── requirements.txt
├── README.md
└── images/
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/LasyaE/Diamond-Price-Prediction.git
```

Move into the project directory

```bash
cd Diamond-Price-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💻 Application

Users provide the following inputs:

- Carat
- Cut
- Color
- Clarity
- Depth
- Table
- Length (x)
- Width (y)
- Height (z)

The application preprocesses the inputs using the saved encoder and predicts the diamond price using the trained CatBoost model.

---

## 📌 Future Enhancements

- Batch prediction using CSV upload
- Live exchange rate conversion
- Docker containerization
- CI/CD deployment
- Model monitoring
- Prediction history dashboard

---

## 👩‍💻 Author

**Lasya Reddy**

B.Tech in Artificial Intelligence & Machine Learning

---

## ⭐ Acknowledgement

This project was developed as an end-to-end Machine Learning application to demonstrate practical skills in data preprocessing, model development, evaluation, deployment, and web application development.