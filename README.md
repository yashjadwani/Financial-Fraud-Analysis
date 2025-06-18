# 💳 Financial Fraud Analysis Using Machine Learning

## 🧾 Intoduction
This project applies machine learning techniques to detect and analyse fraudulent financial transactions. Traditional fraud detection methods rely on static rule-based systems, which can be bypassed as fraud tactics evolve. By utilising supervised and unsupervised learning, this project aims to develop dynamic models that can effectively adapt and identify fraudulent behaviour based on historical data.

The analysis includes exploratory data analysis (EDA), correlation heatmaps, feature engineering, and the development of classification models such as Logistic Regression, Random Forest, and XGBoost. It leverages data from real or simulated transaction histories and includes an optional pipeline to extract data from a database.

## 📁 Repository Structure
The repository is structured as follows:

* Datasets - Contains raw and processed transaction data.
* Corr Plot - Correlation heatmap (Corr plot.png) to visualise feature relationships.

### CODE Files

* db_connection.py - Connects to a relational database (PostgreSQL/MySQL) and retrieves transaction data. Handles credentials and environment variables.
* fraud_detection.ipynb - Performs EDA with data cleaning, preprocessing, and visualisation of missing values, class imbalance, and feature distributions.
* fraud_detection_model.ipynb - Builds ML pipelines with classification, cross-validation, evaluation metrics, and visualisations like confusion matrices, ROC curves, and feature importance.

## 📌 Methodology

The project follows a structured data science pipeline:

### 🔍 Data Extraction
- Retrieve the JSONs and CSVs from Pandas.
- Retrieve transactional data via SQL query using `db_connection.py`.

### 🧹 Data Preprocessing
- Handle missing values, convert data types, and normalise features.
- Address class imbalance (fraud cases are typically rare).

### 📊 Exploratory Data Analysis
- Visualise correlations, feature distributions, and class separations.
- Identify key patterns or anomalies in fraudulent vs. non-fraudulent transactions.

### 🧠 Feature Engineering
- Create new variables based on domain knowledge (e.g., transaction frequency, amount thresholds).

### 🤖 Model Building
- Train Logistic Regression, Random Forest, and XGBoost models.
- Use `GridSearchCV` and cross-validation for hyperparameter tuning.

### 📈 Model Evaluation
- Evaluate models using precision, recall, F1-score, and ROC AUC.
- Visualise results with confusion matrices, ROC curves, and feature importance plots.


## 📌 Conclusion
This project concludes that machine learning models can provide significant improvements over rule-based fraud detection systems. However, challenges such as imbalanced data, feature drift, and evolving fraud strategies must be addressed through continuous data updates and retraining. By building a scalable and interpretable fraud detection system, this project showcases how data science can enhance financial security.

## 📦Dependencies
This project uses several Python packages and libraries, including:

* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* xgboost
* sqlalchemy
* sklearn
