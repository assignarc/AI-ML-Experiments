# ⚡ P4: Renewable Energy Wind - Predictive Maintenance

## 📝 Overview

This project applies **machine learning and deep learning** to predict wind turbine generator failures before they occur. Using sensor data from ReneWind (a fictional renewable energy company), I built multiple neural network architectures to enable **predictive maintenance** and minimize operational costs.

## 🎯 Business Context

Wind energy is crucial for reducing environmental impact. Predictive maintenance uses sensor data to predict component degradation and failure patterns. By identifying failures before they happen, maintenance costs can be drastically reduced compared to reactive repairs or complete replacement.

## 💡 Problem Statement

**Objective:** Build classification models to predict generator failures so turbines can be repaired **before** breaking down.

**Cost Analysis:**

- **True Positives (TP):** Predicted failures → Repair costs
- **False Negatives (FN):** Missed failures → Expensive replacement costs
- **False Positives (FP):** False alarms → Inspection costs

**Cost Hierarchy:** `Inspection < Repair << Replacement`

## The Data

- **Training Set:** 20,000 observations
- **Test Set:** 5,000 observations
- **Features:** 40 predictive variables (anonymized sensor data)
- **Target:** Binary (1 = Failure, 0 = No Failure)
- **Data:** Encrypted/ciphered version of actual sensor measurements

## 🧠 Models & Techniques

### Neural Network Architectures

Built multiple neural network models using **TensorFlow/Keras** with different configurations:

- **3-Layer Sequential Networks** with varying hidden units
- **Dropout layers** for regularization
- **Batch Normalization** for training stability
- **Class weighting** to handle imbalanced data
- **Data scaling** using StandardScaler

### Model Variants Explored

1. **Simple 3-Layer Network (Baseline)**
2. **Dropout-Regularized Models** (various dropout rates)
3. **Class-Weighted Models** (addressing class imbalance)
4. **Scaled vs. Unscaled** comparison
5. **Deep Networks** (4-5 layers with different architectures)

### What I Found

**✅ Feature Scaling is Critical**

- Scaled models consistently outperformed unscaled versions
- Neural networks require normalized features for optimal convergence

**✅ Non-Linear Patterns**

- Weak linear correlations (max 0.37) justify deep learning approach
- Neural networks capture complex, non-linear failure patterns

**✅ Class Imbalance Handling**

- Class weights improved model sensitivity to failure cases
- Balanced precision-recall tradeoffs

## 📈 Evaluation Metrics

Models evaluated using:

- **Accuracy**
- **Precision & Recall**
- **F1-Score**
- **Confusion Matrix analysis**
- **Cost-benefit analysis** (repair vs. replacement vs. inspection)

## 🛠 Tools & Technologies

- **Python:** pandas, numpy, matplotlib, seaborn
- **Deep Learning:** TensorFlow, Keras (Sequential API)
- **VKPyKit Custom Library:** Custom ML utilities
- **Scikit-learn:** StandardScaler, train_test_split, metrics

## What I Learned

- **Data preprocessing** is crucial for neural network performance
- **Feature scaling** dramatically improves model convergence
- Deep learning excels at capturing **non-linear relationships**
- **Regularization techniques** (Dropout,Batch Norm) prevent overfitting
- Business context (cost analysis) guides **metric optimization**

## 📂 Project Files

- `RenewableEnergyWindNotebook.ipynb` - Main analysis notebook
- `Train.csv` - Training dataset (20,000 samples)
- `Test.csv` - Test dataset (5,000 samples)

---

[**🔙 Back to Main Repository**](../readme.md)


---

## Tech Stack
### Packages Needed For This Module:
- `VKPyKit`
- `copy`
- `imblearn`
- `matplotlib`
- `numpy`
- `pandas`
- `seaborn`
- `sklearn`
- `tensorflow`
- `xgboost`
