# 🧠 AI & Machine Learning Experiments

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)](https://scikit-learn.org/)
[![Data Analysis](https://img.shields.io/badge/EDA-Pandas%20%7C%20NumPy-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A comprehensive collection of machine learning experiments, exploratory data analysis, and AI applications built during my journey of mastering data science and artificial intelligence.

### **\*** THIS IS AUTO GENERATED README **\***

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Projects](#-projects)
- [Weekly Learning Modules](#-weekly-learning-modules)
- [Installation](#-installation)
- [Usage](#-usage)
- [Key Learnings](#-key-learnings)
- [Future Roadmap](#-future-roadmap)
- [Contact](#-contact)

---

## 🎯 Overview

This repository serves as a documented journey through the world of **Artificial Intelligence** and **Machine Learning**. Each project and module represents hands-on experience with different ML algorithms, data preprocessing techniques, and real-world problem-solving approaches.

**What you'll find here:**

- 🔬 **Practical ML implementations** from scratch to production-ready models
- 📊 **Exploratory Data Analysis (EDA)** techniques and visualizations
- 🎯 **End-to-end ML projects** solving real business problems
- 📚 **Structured learning modules** covering fundamental to advanced topics
- 🧪 **Experimentation** with various algorithms and optimization techniques

---

## 🛠️ Tech Stack

### Core Technologies

```
Python 3.8+  |  Pandas  |  NumPy  |  Scikit-learn
```

### Data Visualization

```
Matplotlib  |  Seaborn  |  Plotly  |  Plotly Express
```

### Machine Learning Frameworks

```
Scikit-learn  |  XGBoost  |  Statsmodels  |  MLxtend
```

### Additional Tools

```
Jupyter Notebooks  |  VKPyKit (Custom ML Toolkit)
```

---

## 🎁 VKPyKit - Custom Python Toolkit

One of the key innovations in this repository is **VKPyKit**, a custom Python package developed to streamline machine learning workflows and reduce repetitive code across projects.

**📦 Package:** [VKPyKit on PyPI](https://pypi.org/project/VKPyKit/)
**Installation:** `pip install vkpykit`

### Modules

- **EDA Module:** Automated exploratory data analysis functions
- **DT Module:** Decision Tree utilities and visualization helpers
- **MLM Module:** Machine Learning Model utilities for ensemble methods

### Usage in Projects

VKPyKit has been extensively used in:

- **P2: Personal Loan Campaign** - EDA and Decision Tree modeling
- **P3: EasyVisa Project** - All three modules (EDA, DT, MLM) for comprehensive ensemble analysis

### Benefits

✅ **Code Reusability** - Write once, use across all projects
✅ **Standardization** - Consistent analysis patterns
✅ **Efficiency** - Reduced development time
✅ **Version Control** - Packaged and published on PyPI

---

## 🚀 Projects

### 🏨 [P0: Hotel Cancellation Prediction](./P0-AIApplicationCaseStudy-HotelCancellation)

**Domain:** Hospitality & Revenue Management
**Objective:** Predict hotel booking cancellations to optimize revenue and resource allocation

**Dataset:**

- 36,275 hotel booking records
- 19 features: lead time, special requests, market segment, pricing, arrival dates, etc.
- Target: Booking status (Canceled/Not Canceled)
- Includes rebooked flags for customer retention analysis

**Techniques & Models:**

- Extensive exploratory data analysis with visualizations
- Feature engineering (date transformations, categorical encoding)
- Classification algorithms for cancellation prediction
- Market segment analysis (Online vs Offline bookings)

**Key Highlights:**

- Analyzed booking patterns across different market segments
- Identified key cancellation drivers: lead time, special requests, room pricing
- Weekend vs. weekday booking behavior analysis
- Built predictive models to identify high-risk bookings
- Provided actionable insights for revenue optimization and overbooking strategies

**📖 [View Detailed README](./P0-AIApplicationCaseStudy-HotelCancellation/README.md)**

---

### 🍔 [P1: FoodHub Order Analysis](./P1-FoodHub)

**Domain:** Food Delivery & Customer Analytics
**Objective:** Analyze food delivery patterns to improve customer experience and operational efficiency

**Dataset:**

- 1,898 food delivery orders
- 9 features: order_id, customer_id, restaurant_name, cuisine_type, cost, day_of_the_week, rating, food_preparation_time, delivery_time
- **No missing values** - Clean dataset
- Mixed data types: 4 integer, 1 float, 4 object columns

**Analysis Performed:**

- **Order Statistics:**
  - Average cost per order: $16.50
  - Average food preparation time: 27.4 minutes
  - Average delivery time: 24.2 minutes
- **Cuisine Distribution:** American, Mexican, and various international cuisines
- **Time Analysis:** Weekday vs. Weekend ordering patterns
- **Rating Analysis:** Handling "Not given" ratings appropriately

**Key Highlights:**

- Comprehensive data quality checks and treatment
- Deep-dive analysis of order trends and customer behavior
- Identified correlations between cuisine type, cost, and delivery performance
- Restaurant performance comparison across multiple metrics
- Data-driven recommendations for improving operational efficiency

**📖 [View Detailed README](./P1-FoodHub/README.md)**

---

### 💳 [P2: Personal Loan Campaign](./P2-PersonalLoanCampaign)

**Domain:** Banking & Financial Services
**Objective:** Predict customers likely to accept personal loan offers through targeted marketing

**Dataset:**

- 5,000 customer records
- 14 features: ID, Age, Experience, Income, ZIPCode, Family, CCAvg, Education, Mortgage, Personal_Loan, Securities_Account, CD_Account, Online, CreditCard
- Target: Personal_Loan (Binary classification)
- Highly imbalanced dataset requiring special handling

**Techniques & Models:**

- Decision Tree Classification (primary model)
- Comprehensive feature importance analysis
- Customer segmentation based on demographics and banking behavior
- **Custom VKPyKit Library:** Utilized personal Python package for streamlined EDA and DT modeling
- Feature engineering and selection

**Key Features Analyzed:**

- Demographics: Age (23-67 years), Experience, Family Size
- Financial indicators: Income, CCAvg (credit card spending), Mortgage
- Banking relationship: Securities Account, CD Account, Online banking, Credit Card
- Education level (1, 2, 3 - ordinal encoding)

**Key Highlights:**

- Built customer propensity models for targeted marketing campaigns
- Identified high-value customer segments most likely to accept loans
- Income and CCAvg emerged as strong predictors of loan acceptance
- Applied decision trees to understand feature importance and decision boundaries
- Optimized campaign ROI through data-driven targeting strategies

**📖 [View Detailed README](./P2-PersonalLoanCampaign/README.md)**

---

### 🌍 [P3: EasyVisa - Immigration Approval Prediction](./P3-EnsembleLearning-Visa)

**Domain:** Immigration & Government Services
**Objective:** Predict visa certification decisions using advanced ensemble learning techniques

**Dataset:**

- 25,480 visa application records
- 12 features: case_id, continent, education_of_employee, has_job_experience, requires_job_training, no_of_employees, yr_of_estab, region_of_employment, prevailing_wage, unit_of_wage, full_time_position, case_status
- Target: case_status (Certified/Denied - Binary classification)
- **No missing values** - High-quality dataset
- 9 categorical features, 2 integer, 1 float

**Advanced Techniques:**

- **Ensemble Methods:** Bagging, Random Forest, AdaBoost, Gradient Boosting, XGBoost, Stacking
- **Class Imbalance Handling:**
  - SMOTE (Synthetic Minority Over-sampling Technique)
  - Random undersampling
  - Comparative analysis: Original vs. Oversampled vs. Undersampled data
- **Hyperparameter Tuning:**
  - GridSearchCV for exhaustive parameter search
  - RandomizedSearchCV for efficient optimization
- **Custom Toolkit:** Extensive use of **VKPyKit** (EDA, DT, MLM modules)
- **Feature Engineering:** Wage normalization (Hour to Year conversion)

**Models Implemented:**

1. Decision Tree (baseline)
2. Bagging Classifier
3. Random Forest
4. AdaBoost
5. Gradient Boosting
6. XGBoost
7. Stacking Classifier
8. Tuned versions of top performers (with GridSearch/RandomizedSearch)

**Key Highlights:**

- Comprehensive model comparison across 10+ ensemble configurations
- Generated multiple performance comparison visualizations:
  - Model Comparison - Original Data
  - Model Comparison - OverSampled
  - Model Comparison - UnderSampled Data
  - Model Comparison - Oversampled Tuned Data
- Detailed performance metrics: Accuracy, Precision, Recall, F1-Score
- Feature importance analysis across different ensemble methods
- Confusion matrices and classification reports for each model
- Achieved significant performance improvements through systematic tuning
- Education level and prevailing wage identified as key predictors

**📖 [View Detailed README](./P3-EnsembleLearning-Visa/README.md)**

---

### ⚡ [P4: RenewableEnergyWind - Predictive Maintenance](./P4-RenewableEnergyWind)

**Domain:** Renewable Energy & IoT
**Objective:** Predict wind turbine generator failures before they occur to enable predictive maintenance and reduce operational costs

**Dataset:**

- 25,000 sensor measurements total (20,000 train / 5,000 test)
- 40 predictive features (anonymized sensor data from wind turbines)
- Target: Binary classification (1 = Failure, 0 = No Failure)
- **Encrypted/ciphered** sensor data for confidentiality
- Highly imbalanced dataset requiring class weighting techniques

**Advanced Techniques:**

- **Deep Learning:** Multiple neural network architectures using TensorFlow/Keras
- **Feature Scaling:** StandardScaler for neural network optimization
- **Regularization:** Dropout layers and Batch Normalization
- **Class Imbalance:** Class weighting to address failure detection sensitivity
- **Architectures:** 3-5 layer Sequential networks with varying configurations
- **Custom Toolkit:** VKPyKit for preprocessing and utilities

**Neural Network Models:**

1. Baseline 3-Layer Network (unscaled vs. scaled)
2. Dropout-Regularized Models (various dropout rates)
3. Class-Weighted Networks for imbalanced data
4. Deep Networks (4-5 layers)
5. Batch-Normalized architectures
6. Combination models (Dropout + Class Weights + Scaling)

**Key Technical Insights:**

- **Feature Scaling:** Scaled models consistently outperformed unscaled versions for neural networks
- **Non-Linear Patterns:** Weak linear correlations (max 0.37) justify deep learning approach
- **Regularization:** Dropout and Batch Normalization prevent overfitting
- **Class Weights:** Improved model sensitivity to failure cases
- **Cost Analysis:** Optimized for business metrics (repair vs. replacement vs. inspection costs)

**Key Highlights:**

- Comprehensive neural network experimentation with 15+ model configurations
- Systematic comparison of scaled vs. unscaled data performance
- Feature engineering from encrypted sensor measurements
- Cost-benefit analysis aligned with business objectives (TP=Repair, FN=Replacement, FP=Inspection)
- Built production-ready predictive maintenance system
- Demonstrated critical importance of data preprocessing for deep learning

**📖 [View Detailed README](./P4-RenewableEnergyWind/README.md)**

---

## 📚 Weekly Learning Modules

A structured 12-week learning path from Python fundamentals to advanced ML pipelines, featuring hands-on exercises and real-world case studies.

---

### 🔰 Foundations

#### **[W0: Python Training](./W0-PythonTrainings)**

**Focus:** Python programming fundamentals and advanced concepts**Content:** 125+ Python exercises and examples

- Core Python syntax and data structures
- Object-oriented programming principles
- File I/O and system operations
- Python best practices and debugging techniques

**📖 [View Detailed README](./W0-PythonTrainings/README.md)**

#### **[W1: Python Essentials](./W1-PythonEssentials)**

**Focus:** Core Python libraries for data science**Topics Covered:**

- **NumPy:** Array operations, mathematical functions, linear algebra
- **Pandas:** DataFrames, data manipulation, aggregation, and transformation
- **Python for DS:** Introduction to data science workflows
- **OOP in Python:** Classes, inheritance, encapsulation
- **OS Module:** File system operations and automation

**Case Study:** MovieLens dataset - Introduction to recommendation systems

**📖 [View Detailed README](./W1-PythonEssentials/README.md)**

---

### 📊 Data Analysis & Visualization

#### **[W2: MovieLens Analysis](./W2-MovieLens)**

**Focus:** Introduction to recommendation systems and data exploration**Dataset:** MovieLens movie ratings

- Data loading and preprocessing
- User behavior analysis
- Movie rating distributions
- Basic recommendation algorithms

**📖 [View Detailed README](./W2-MovieLens/README.md)**

#### **[W3: Exploratory Data Analysis](./W3-ExploratoryDataAnalysis)**

**Focus:** Comprehensive EDA techniques and statistical visualization
**Content:** 14 notebooks and exercises

**Case Studies:**

- **Uber Case Study:** Ride-sharing patterns and demand forecasting
- **General EDA Practice:** Multiple datasets with varying characteristics

**Techniques Learned:**

- Univariate, bivariate, and multivariate analysis
- Statistical measures (mean, median, mode, variance, standard deviation)
- Distribution analysis and outlier detection
- Correlation analysis and heatmaps
- **Visualization Libraries:** Matplotlib, Seaborn, Plotly
- Data quality assessment and missing value treatment

**📖 [View Detailed README](./W3-ExploratoryDataAnalysis/README.md)**

#### **[W4: Text Data Analysis](./W4-AnalyzeTextData)**

**Focus:** Natural language processing and text mining fundamentals**Topics:**

- Regular expressions (RegEx) for pattern matching
- Text cleaning and preprocessing
- Data extraction from unstructured text
- String manipulation and parsing techniques

**📖 [View Detailed README](./W4-AnalyzeTextData/README.md)**

---

### 🎯 Supervised Learning

#### **[W5: Linear Regression](./W5-LinearRegression)**

**Focus:** Regression modeling, assumptions, and evaluation
**Content:** 11 notebooks across 5 case studies

**Case Studies:**

1. **Anime Rating Prediction:** Predicting anime ratings based on features
2. **Auto MPG:** Fuel efficiency prediction, regression assumptions validation
3. **Sales Forecasting:** Revenue prediction using multiple features
4. **Used Cars Pricing (Cars4u):** Price prediction based on car characteristics
5. **Practice Exercises:** Simple Linear Regression fundamentals

**Techniques Learned:**

- Simple and Multiple Linear Regression
- **Regression Assumptions:** Linearity, homoscedasticity, normality, independence
- Feature selection and engineering
- Model evaluation: R², RMSE, MAE, adjusted R²
- Residual analysis and diagnostics
- Multicollinearity detection (VIF)

**📖 [View Detailed README](./W5-LinearRegression/README.md)**

#### **[W6: Decision Trees](./W6-DecisionTree)**

**Focus:** Tree-based classification and regression algorithms
**Content:** 6 notebooks across 3 case studies

**Case Studies:**

1. **Credit Card Approval:** Binary classification for credit decisions
2. **Loan Delinquency:** Predicting loan default risk
3. **Machine Failure Prediction:** Predictive maintenance for equipment

**Techniques Learned:**

- Decision Tree algorithms (CART, ID3, C4.5 concepts)
- Entropy and Information Gain
- Gini impurity as splitting criterion
- Tree pruning to prevent overfitting
- Hyperparameter tuning (max_depth, min_samples_split, min_samples_leaf)
- Feature importance analysis
- Visualization of decision boundaries and trees

**📖 [View Detailed README](./W6-DecisionTree/README.md)**

---

### 🔍 Unsupervised Learning

#### **[W7: K-Means Clustering](./W7-ClusteringKMeans)**

**Focus:** Partitioning-based clustering algorithms
**Content:** 4 notebooks across 2 major case studies

**Case Studies:**

1. **Credit Card Customer Segmentation:** Identifying customer groups for targeted marketing
2. **Retail Customer Segmentation:** Customer behavior clustering for business insights

**Techniques Learned:**

- K-Means algorithm and convergence
- **Elbow Method** for optimal K selection
- **Silhouette Score** for cluster validation
- Feature scaling and normalization importance
- Cluster profiling and interpretation
- Customer segmentation strategies

**📖 [View Detailed README](./W7-ClusteringKMeans/README.md)**

#### **[W8: Hierarchical Clustering](./W8-ClusteringHierarchical)**

**Focus:** Hierarchical clustering methods and dimensionality reduction
**Content:** 4 notebooks

**Case Studies:**

1. **Customer Spending Analysis:** Hierarchical clustering on customer expenditure data
2. **Principal Component Analysis (PCA):** Dimensionality reduction techniques

**Techniques Learned:**

- Agglomerative (bottom-up) clustering
- Divisive (top-down) clustering
- **Dendrograms** for hierarchy visualization
- Linkage methods: single, complete, average, Ward
- Distance metrics: Euclidean, Manhattan, Cosine
- **PCA:** Feature extraction, variance explanation, component interpretation
- Scree plots for component selection

**📖 [View Detailed README](./W8-ClusteringHierarchical/README.md)**

---

### 🚀 Advanced Techniques

#### **[W9: Ensemble Learning - Bagging](./W9-EnsembleLearning-Bagging)**

**Focus:** Bootstrap Aggregating and Random Forests
**Content:** 4 notebooks across 2 case studies

**Case Studies:**

1. **Diabetes Risk Prediction:** Health risk assessment using ensemble methods
2. **Loan Default Prediction:** Credit risk modeling with bagging

**Techniques Learned:**

- **Bootstrap Sampling** and aggregation
- **Random Forest Classifier/Regressor**
- Out-of-Bag (OOB) error estimation
- Feature importance from ensemble models
- Variance reduction through bagging
- Comparison: Single Decision Tree vs. Bagging vs. Random Forest

**📖 [View Detailed README](./W9-EnsembleLearning-Bagging/README.md)**

#### **[W10: Ensemble Learning - Boosting](./W10-EnsembleLearning-Boosting)**

**Focus:** Sequential ensemble methods and boosting algorithms
**Content:** 4 notebooks across 2 case studies

**Case Studies:**

1. **Credit Default Prediction:** Binary classification with boosting
2. **Wine Quality Prediction:** Multi-class quality rating prediction

**Techniques Learned:**

- **AdaBoost:** Adaptive boosting with weighted samples
- **Gradient Boosting:** Loss function optimization
- **XGBoost:** Extreme gradient boosting with regularization
- Learning rate and n_estimators tuning
- Bias-variance tradeoff in boosting
- Performance comparison across boosting algorithms

**📖 [View Detailed README](./W10-EnsembleLearning-Boosting/README.md)**

#### **[W11: Model Tuning &amp; Optimization](./W11-EnsembleLearning-ModelTuning)**

**Focus:** Hyperparameter optimization and advanced model validation
**Content:** 7 notebooks across 3 case studies

**Case Studies:**

1. **Diabetes Dataset:** K-fold cross-validation techniques
2. **Job Market Data:** Employment prediction with tuned models
3. **Loan Dataset:** Class imbalance handling with sampling techniques

**Techniques Learned:**

- **K-Fold Cross-Validation:** Robust model evaluation
- **Stratified K-Fold:** Maintaining class distribution
- **GridSearchCV:** Exhaustive hyperparameter search
- **RandomizedSearchCV:** Efficient parameter sampling
- **SMOTE:** Synthetic Minority Over-sampling Technique
- **Random Undersampling:** Balancing majority class
- **Oversampling vs. Undersampling:** Comparative analysis
- Pipeline creation for reproducible workflows
- Nested cross-validation for unbiased evaluation

**📖 [View Detailed README](./W11-EnsembleLearning-ModelTuning/README.md)**

#### **[W12: ML Pipelines](./W12-MLPipelines)**

**Focus:** Streamlined ML workflows with scikit-learn pipelines
**Content:** End-to-end pipeline implementation

**Projects:**

1. **SimplePipeline:** Diabetes risk prediction using Pipeline and make_pipeline

**Techniques Learned:**

- **sklearn.pipeline.Pipeline:** Creating named pipeline steps for explicit control
- **sklearn.pipeline.make_pipeline:** Simplified pipeline creation with automatic naming
- **Pipeline Benefits:**
  - Prevents data leakage in preprocessing
  - Ensures fit/transform separation between train and test data
  - Single object for entire ML workflow
  - Seamless integration with cross-validation
  - Production-ready model deployment
- **StandardScaler Integration:** Feature standardization within pipelines
- **Cross-Validation with Pipelines:** Proper CV workflow maintenance
- **Pipeline Component Access:** Accessing and manipulating named steps
- **End-to-End Workflow Automation:** From raw data to predictions

**Key Highlights:**

- Comparison of `Pipeline` vs `make_pipeline` approaches
- Prevention of common pitfalls (data leakage, preprocessing errors)
- Building reproducible and maintainable ML workflows
- Integration of preprocessing and modeling in a single object
- Applied to medical diagnostics (Pima Indians Diabetes dataset)

**📖 [View Module README](./W12-MLPipelines/README.md)** | **[View SimplePipeline README](./W12-MLPipelines/SimplePipeline/README.md)**

#### **[W13: Ridge vs Lasso Regression](./W13-RidgeLassoComparision)**

**Focus:** Comparing regularization techniques (Ridge vs Lasso)  
**Content:** Regression comparison on car fuel efficiency dataset

**Case Study:**

1. **Car MPG Prediction:** Predicting miles per gallon using Ridge and Lasso regression

**Techniques Learned:**

- **Ridge Regression (L2):** Shrinks coefficients toward zero
- **Lasso Regression (L1):** Performs feature selection by zeroing out coefficients
- **Feature Scaling:** StandardScaler for regularized models
- **Cross-Validation:** Finding optimal regularization parameters
- **Model Comparison:** Ridge vs Lasso vs standard Linear Regression
- **Metrics:** R² score, MSE, RMSE

**Key Highlights:**

- Feature scaling is crucial for regularized models
- Ridge works better when all features contribute
- Lasso performs automatic feature selection
- Cross-validation helps find optimal regularization strength

**📖 [View Detailed README](./W13-RidgeLassoComparision/README.md)**

---

### 🧠 Deep Learning

#### **[W14: Introduction to Neural Networks](./W14-IntroNeuralNetworks)**

**Focus:** Fundamentals of Deep Learning and Artificial Neural Networks (ANN)
**Content:** Hands-on implementation of regression using TensorFlow/Keras

**Projects:**

1. **Used Car Price Prediction:** Building a pricing model using Neural Networks.

**Techniques Learned:**

- **Keras Sequential API:** Constructing models layer-by-layer
- **Network Architecture:** Designing Input, Hidden, and Output layers
- **Activation Functions:** Impact of ReLU, Sigmoid, and Tanh on learning
- **Optimizers & Loss:** Using SGD and Mean Squared Error for regression
- **Model Tuning:** Experimenting with epochs, batch sizes, and neurons
- **Preprocessing for DL:** Log-transformation and scaling for convergence

**Key Highlights:**

- Iteratively built and compared 8 different NN architectures
- Achieved ~84% R² on test data using a ReLU-activated network
- Demonstrated the trade-off between model complexity and training time

**📖 [View Detailed README](./W14-IntroNeuralNetworks/README.md)**

---

#### **[W15: Optimizing Neural Networks](./W15-OptimizingNeuralNetworks)**

**Focus:** Advanced optimization techniques for neural networks to prevent overfitting and improve generalization
**Content:** Hands-on implementation of regularization and normalization techniques

**Projects:**

1. **MNIST Digit Classification:** Implementing Dropout and Batch Normalization for handwritten digit recognition.
2. **Credit Card Fraud Detection:** Optimizing neural networks for imbalanced datasets.
3. **Job Change Prediction:** Employee retention prediction using optimized neural network architectures.

**Techniques Learned:**

- **Dropout:** Random neuron deactivation to prevent overfitting
- **Batch Normalization:** Stabilizing and accelerating training through layer normalization
- **L1/L2 Regularization:** Weight constraint techniques
- **Learning Rate Scheduling:** Dynamic learning rate adjustment
- **Early Stopping:** Preventing overfitting through validation monitoring
- **Hyperparameter Tuning:** Optimizing dropout rates, batch sizes, and network architectures

**Key Highlights:**

- Comparative analysis of baseline vs. optimized models
- Hands-on implementation of advanced regularization techniques
- Application to real-world problems (fraud detection, employee analytics)
- Understanding the impact of optimization on model generalization

**📖 [View Detailed README](./W15-OptimizingNeuralNetworks/README.md)**

---

### 💬 Natural Language Processing

#### **[W16: Natural Language Processing](./W16-NaturalLanguageProcessing)**

**Focus:** NLP fundamentals, word embeddings, and text classification
**Content:** 3 comprehensive projects on sentiment analysis and text categorization

**Projects:**

##### **1. [Movie Review Sentiment Analysis](./W16-NaturalLanguageProcessing/Movies)**

**Problem:** Binary sentiment classification of movie reviews
**Dataset:** Movie reviews with positive/negative labels

**Techniques:**

- Text preprocessing (tokenization, lemmatization, stopword removal)
- **GloVe word embeddings** (100-dimensional vectors)
- Random Forest classification
- NLTK for text processing

**Results:** ~84% train accuracy, ~81% test accuracy

**📖 [View Detailed README](./W16-NaturalLanguageProcessing/Movies/README.md)**

##### **2. [Product Review Sentiment Analysis](./W16-NaturalLanguageProcessing/ProductReview)**

**Problem:** Sentiment classification for product reviews
**Dataset:** Product review text with sentiment labels

**Techniques:**

- GloVe pre-trained embeddings
- Document-level embedding (averaging word vectors)
- Text cleaning and preprocessing
- Classification modeling

**Key Learning:** Word embeddings generalize across different domains

**📖 [View Detailed README](./W16-NaturalLanguageProcessing/ProductReview/README.md)**

##### **3. [Article Categorization](./W16-NaturalLanguageProcessing/WordEmbedding)**

**Problem:** Multi-class classification of news articles by topic/category
**Dataset:** News articles with category labels

**Techniques:**

- **GloVe embeddings** for semantic representation
- Random Forest for multi-class classification
- Text preprocessing pipeline
- Feature importance analysis

**Business Context:**

- Content recommendation systems
- Automatic article tagging
- Personalized news feeds

**Key Learning:** Pre-trained embeddings save massive training time and work well for classification

**📖 [View Detailed README](./W16-NaturalLanguageProcessing/WordEmbedding/README.md)**

**Common NLP Techniques Across Projects:**

- Tokenization and text cleaning
- Lemmatization using NLTK WordNet
- Stopword removal
- GloVe word embeddings (Global Vectors for Word Representation)
- Document vectorization strategies
- Text classification with ensemble methods

#### **[W17: Attention Mechanisms & Transformers](./W17-AttentionMechanism-Transformers)**

**Focus:** Modern NLP with transformers and attention mechanisms  
**Content:** 2 projects exploring transformers for text classification

**Projects:**

##### **1. [Transformer-Based Movie Reviews](./W17-AttentionMechanism-Transformers/HandsOn-MoviewReviews)**

**Problem:** Movie review sentiment analysis using transformers
**Dataset:** Movie reviews dataset

**Techniques:**

- **Sentence Transformers** - pre-trained transformer models
- Contextualized embeddings (context-aware word representations)
- Attention mechanisms
- PyTorch for deep learning

**Key Learning:** Transformers capture context better than static embeddings like GloVe

**📖 [View Detailed README](./W17-AttentionMechanism-Transformers/HandsOn-MoviewReviews/README.md)**

##### **2. [News Article Categorization with Transformers](./W17-AttentionMechanism-Transformers/NewsArticles)**

**Problem:** Multi-class article categorization using attention mechanisms
**Dataset:** News articles with category labels

**Techniques:**

- Pre-trained sentence transformers
- Attention mechanisms for document understanding
- Transfer learning with BERT/RoBERTa-based models
- Multi-class classification

**Key Learning:** Transformers handle longer documents and context better than embedding averaging

**📖 [View Detailed README](./W17-AttentionMechanism-Transformers/NewsArticles/README.md)**

**Module Overview:**

- Understanding attention mechanisms (self-attention)
- Transformer architecture fundamentals
- Using pre-trained transformer models
- sentence-transformers library
- Comparing transformers vs traditional embeddings

**📖 [View Module README](./W17-AttentionMechanism-Transformers/README.md)**

---

### 📈 Learning Progression

```
Week 0-1:  Python Fundamentals
  ↓
Week 2-4:  Data Analysis & Visualization
  ↓
Week 5-6:  Supervised Learning (Regression & Classification)
  ↓
Week 7-8:  Unsupervised Learning (Clustering & PCA)
  ↓
Week 9-11: Advanced Ensemble Methods & Optimization
  ↓
Week 12:   ML Pipelines & Workflow Automation
  ↓
Week 13:   Regularization (Ridge & Lasso Regression)
  ↓
Week 14-15: Deep Learning (Neural Networks & Optimization)
  ↓
Week 16:   Natural Language Processing (Word Embeddings & Text Classification)
  ↓
Week 17:   Attention Mechanisms & Transformers (Modern NLP)
```

**Total Content:**

- **125+** Python training exercises
- **50+** Jupyter notebooks
- **19+** real-world case studies
- **10+** different ML algorithms implemented
- **Complete ML workflow automation** with pipelines
- **Deep Learning fundamentals** with TensorFlow/Keras
- **NLP projects** with word embeddings and text classification
- **Transformers & Attention** mechanisms for modern NLP

---

## 💻 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/AI-ML-Experiments.git
   cd AI-ML-Experiments
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

The main packages used in this repository include:

- `numpy` - Numerical computing
- `pandas` - Data manipulation and analysis
- `matplotlib` & `seaborn` - Static visualizations
- `plotly` & `plotly-express` - Interactive visualizations
- `scikit-learn` - Machine learning algorithms
- `xgboost` - Gradient boosting framework
- `statsmodels` - Statistical modeling
- `mlxtend` - ML extensions and utilities
- `vkpykit` - Custom ML toolkit

---

## 🎮 Usage

### Running Jupyter Notebooks

1. Navigate to the desired project directory:

   ```bash
   cd P3-EnsembleLearning-Visa
   ```

2. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Open the `.ipynb` file and run the cells sequentially.

### Project Structure

Each project folder typically contains:

- 📓 **Jupyter Notebooks** - Complete code with analysis and visualizations
- 📊 **Datasets** - CSV or other data files
- 📈 **Visualizations** - Generated plots and charts
- 📄 **HTML exports** - Notebook exports for easy viewing

---

## 🎓 Key Learnings

Throughout these projects and modules, I've gained expertise in:

### Data Science Fundamentals

✅ Data cleaning and preprocessing
✅ Exploratory Data Analysis (EDA)
✅ Feature engineering and selection
✅ Handling missing values and outliers
✅ Data visualization and storytelling

### Machine Learning

✅ Supervised learning (Classification & Regression)
✅ Unsupervised learning (Clustering)
✅ Ensemble methods (Bagging, Boosting, Stacking)
✅ Model evaluation and validation
✅ Cross-validation techniques
✅ Hyperparameter tuning

### Advanced Topics

✅ Handling imbalanced datasets
✅ Model interpretation and explainability
✅ Performance optimization
✅ Pipeline creation for reproducibility
✅ Custom library development (VKPyKit)

---

## 🔮 Future Roadmap

### Short-term Goals

- [ ] Deep Learning with TensorFlow/PyTorch
- [ ] Natural Language Processing projects
- [ ] Computer Vision applications
- [ ] Time Series forecasting

### Long-term Goals

- [ ] Deploy ML models as web services
- [ ] Contribute to open-source ML libraries
- [ ] Build end-to-end MLOps pipelines
- [ ] Explore reinforcement learning

---

## 📧 Contact

**Vishal Khapre**

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Acknowledgments

This repository represents learning from various sources including:

- Online courses and tutorials
- Data science community best practices
- Open-source ML libraries and their documentation
- Real-world industry applications
