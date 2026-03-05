# 🔧 Week 15: Optimizing Neural Networks

## 📝 Overview

This module focuses on ** optimization techniques** for neural networks to prevent overfitting, improve generalization, and enhance model performance. It builds upon Week 14's fundamentals with regularization methods and normalization techniques.

## 📚 Key Concepts

- **Regularization Techniques:**
 - **Dropout:** Randomly deactivating neurons during training to prevent co-adaptation and overfitting.
 - **Batch Normalization:** Normalizing inputs of each layer to stabilize and accelerate training.
 - **L1/L2 Regularization:** Adding penalty terms to the loss function to constrain weights.
- **Optimization Strategies:**
 - **Learning Rate Scheduling:** Dynamic adjustment of learning rates during training.
 - **Early Stopping:** Monitoring validation performance to prevent overfitting.
- ** Architectures:** Building deeper networks with multiple hidden layers.

## 🛠️ Techniques & Tools

- **TensorFlow & Keras:** Implementing Dropout and BatchNormalization layers.
- **Hyperparameter Tuning:** Experimenting with different dropout rates, batch sizes, and learning rates.
- **Model Comparison:** Evaluating performance across various architectures.

## 📂 Projects

### 🔢 [MNIST Digit Classification](./Optimizing_Neural_Networks_Notebook.ipynb)

**Objective:** Classify handwritten digits (0-9) using optimized neural network architectures.

**Dataset:**

- 70,000 grayscale images (28x28 pixels)
- Train: 60,000 images | Test: 10,000 images
- Pixel values normalized to [0, 1] range

**Highlights:**

- **Optimization Techniques Applied:**
 - Dropout layers to reduce overfitting
 - Batch Normalization for faster convergence
 - Multiple hidden layer configurations
- **Performance Metrics:** Accuracy, Loss tracking across epochs
- **Comparative Analysis:** Baseline vs. optimized models

---

### 💳 [Credit Card Fraud Detection](./CreditCard)

**Objective:** Detect fraudulent credit card transactions using neural networks optimized for imbalanced datasets.

**Highlights:**

- Handling highly imbalanced data (fraudulent vs. legitimate transactions)
- Application of dropout and regularization techniques
- Binary classification with optimized neural network architecture

---

### 👔 [Job Change Prediction](./JobChange)

**Objective:** Predict whether an employee is likely to change jobs based on demographic and work-related features.

**Highlights:**

- Multi-feature analysis for employee retention prediction
- Neural network optimization for classification tasks
- Practical HR analytics application

---

### 📊 [MNIST Example (Lecture)](./MNIST-ExampleInLecture)

**Objective:** Step-by-step demonstration of neural network optimization concepts from the lecture.

**Highlights:**

- Foundational example illustrating dropout and batch normalization
- Clear visualization of optimization impact on model performance

---

## What I Learned

- **Dropout** effectively prevents overfitting by randomly dropping neurons during training.
- **Batch Normalization** stabilizes training and allows for higher learning rates.
- Proper regularization techniques significantly improve model generalization.
- Balancing model complexity with regularization is crucial for optimal performance.

---

[**🔙 Back to Main Repository**](../readme.md)


---

## Tech Stack
### Packages Needed For This Module:
- `keras`
- `matplotlib`
- `numpy`
- `pandas`
- `seaborn`
- `sklearn`
- `tensorflow`
