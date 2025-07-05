# Ethical Audit Dashboard

This project explores how we can use data to flag potential ethical issues in healthcare delivery. The current version focuses on diabetes care in Canada, using publicly available health datasets to analyze fairness across subgroups.

## What it does

- Loads and processes real-world demographic and health data
- Trains a basic machine learning model to predict healthcare outcomes
- Compares model performance across subgroups (e.g. gender, income level)
- Highlights areas where treatment or access may be unequal
- Presents findings in a clean, interactive dashboard

## Why it matters

Data and algorithms are shaping healthcare decisions more than ever. This tool is a small step toward making those systems more transparent, especially when it comes to how different populations are treated.

## Built with

- Python (Pandas, Scikit-learn)
- Streamlit for the dashboard
- Publicly sourced Canadian health datasets

## Next steps

- Add more fairness metrics (e.g. equal opportunity, demographic parity)
- Expand to other conditions and datasets
- Improve model accuracy and interpretability
