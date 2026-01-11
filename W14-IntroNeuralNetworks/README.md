# 🧠 Week 14: Introduction to Neural Networks

## 📝 Overview

This module introduces the fundamentals of **Deep Learning** and **Artificial Neural Networks (ANN)**. It marks the transition from traditional machine learning algorithms to deep learning architectures capable of modeling complex non-linear relationships.

## 📚 Key Concepts

- **Artificial Neural Networks (ANN):** Understanding neurons, layers (Input, Hidden, Output), and weights.
- **Forward & Backward Propagation:** The mechanism of learning and error correction.
- **Activation Functions:**
  - **Sigmoid:** S-shaped curve, outputs between 0 and 1.
  - **Tanh:** Hyperbolic tangent, outputs between -1 and 1.
  - **ReLU (Rectified Linear Unit):** Solves vanishing gradient problem, outputs 0 or input.
- **Loss Functions:** Measuring error (e.g., Mean Squared Error for regression).
- **Optimizers:** Algorithms to update weights (e.g., Stochastic Gradient Descent - SGD).

## 🛠️ Techniques & Tools

- **TensorFlow & Keras:** Using the Sequential API to build models.
- **Data Preprocessing for DL:**
  - **StandardScaler:** Essential for neural network convergence.
  - **Log Transformation:** Handling skewed data distributions.
  - **Missing Value Imputation:** Using grouped medians.
- **Model Evaluation:** R², RMSE, MAE, and MAPE.

## 📂 Projects

### 🚗 [Used Car Price Prediction](./UsedCars)

**Objective:** Develop a neural network model to predict the selling price of used cars based on specifications like brand, model, year, engine, and mileage.

**Highlights:**
- **Iterative Approach:** Started with a simple perceptron and evolved to multi-layer networks.
- **Architecture Tuning:** Experimented with different numbers of hidden layers (1 to 2) and neurons (32, 64, 128).
- **Activation Analysis:** Compared performance of Sigmoid, Tanh, and ReLU.
- **Results:** The final model with ReLU activation achieved an **R² of ~0.84** on test data.

---

[**🔙 Back to Main Repository**](../readme.md)