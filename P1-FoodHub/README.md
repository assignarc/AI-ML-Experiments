# 🍔 FoodHub Order Analysis

> **Data Analytics Project:** Understanding food delivery patterns to optimize customer experience and operational efficiency

---

## 📋 Project Overview

**Domain:** Food Delivery & Customer Analytics  
**Project Type:** Exploratory Data Analysis (EDA)  
**Difficulty Level:** Beginner to Intermediate

### Business Problem

FoodHub, a food aggregator company, needs to analyze customer ordering behavior to:

- Understand customer preferences and ordering patterns
- Identify operational inefficiencies
- Improve delivery times and customer satisfaction
- Optimize restaurant partnerships

---

## 📊 Dataset

**Source:** FoodHub order records  
**Records:** 1,898 food delivery orders  
**Features:** 9 variables  
**Data Quality:** No missing values - Clean dataset

### Data Dictionary

| Column                  | Description                      | Type    | Example     |
| ----------------------- | -------------------------------- | ------- | ----------- |
| `order_id`              | Unique order identifier          | Integer | 1477147     |
| `customer_id`           | Unique customer identifier       | Integer | 337525      |
| `restaurant_name`       | Name of the restaurant           | Object  | Shake Shack |
| `cuisine_type`          | Type of cuisine ordered          | Object  | American    |
| `cost_of_the_order`     | Total order cost in USD          | Float   | 20.45       |
| `day_of_the_week`       | Weekday or Weekend               | Object  | Weekday     |
| `rating`                | Customer rating (or "Not given") | Object  | 5           |
| `food_preparation_time` | Time in minutes                  | Integer | 25          |
| `delivery_time`         | Time in minutes                  | Integer | 23          |

---

## 🎯 Analysis Objectives

### 1. Order Statistics

- Calculate average order value
- Analyze order frequency patterns
- Identify peak ordering times

### 2. Restaurant Performance

- Compare restaurants by order volume
- Analyze preparation and delivery times
- Evaluate customer ratings

### 3. Cuisine Preferences

- Identify popular cuisine types
- Analyze pricing by cuisine
- Customer preferences analysis

### 4. Time Analysis

- Weekday vs. Weekend patterns
- Preparation time efficiency
- Delivery time optimization

### 5. Customer Behavior

- Rating patterns
- Order value distribution
- Repeat customer analysis

---

## 📈 Key Statistics

**Order Metrics:**

- **Average Order Cost:** $16.50
- **Average Preparation Time:** 27.4 minutes
- **Average Delivery Time:** 24.2 minutes
- **Total Processing Time:** ~51.6 minutes average

**Data Distribution:**

- **Data Types:** 4 Integer, 1 Float, 4 Object columns
- **Cuisine Variety:** American, Mexican, and international options
- **Rating System:** Numerical ratings + "Not given" option

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical data visualization
- **Jupyter Notebook** - Interactive analysis

---

## 📁 Project Structure

```
P1-FoodHub/
├── P1_FoodHub_VK_Notebook_Full_Code.ipynb
├── P1-FoodHub-VK_Notebook_Full_Code_Submission.ipynb
├── P1_FoodHub_VK_Notebook_Full_Code.csv
├── P1_FoodHub_VK_Notebook_Full_Code.html
└── README.md (this file)
```

---

## 🚀 How to Use

### Installation

```bash
# Install required packages
pip install pandas numpy matplotlib seaborn jupyter

# Or use the requirements.txt from main repository
pip install -r ../requirements.txt
```

### Run the Analysis

```bash
# Launch Jupyter Notebook
jupyter notebook P1_FoodHub_VK_Notebook_Full_Code.ipynb
```

---

## 📊 Analysis Workflow

1. **Data Loading & Inspection**

   - Load CSV data
   - Check data types and structure
   - Verify data quality (1,898 rows × 9 columns)

2. **Data Cleaning**

   - Handle "Not given" ratings
   - Check for missing values (None found ✓)
   - Verify data consistency

3. **Exploratory Analysis**

   - Univariate analysis (distributions)
   - Bivariate analysis (relationships)
   - Statistical summaries

4. **Visualization**

   - Order cost distributions
   - Cuisine popularity charts
   - Time analysis plots
   - Rating distributions

5. **Insights & Recommendations**
   - Key findings summary
   - Business recommendations
   - Operational improvements

---

## 💡 Key Findings

### Customer Preferences

- Cuisine distribution reveals customer favorites
- Price sensitivity patterns identified
- Rating behavior analyzed

### Operational Insights

- Preparation time varies by restaurant and cuisine
- Delivery efficiency metrics calculated
- Weekday vs. Weekend differences observed

### Restaurant Performance

- Top-performing restaurants by volume
- Quality vs. Speed tradeoff analysis
- Customer satisfaction patterns

---

## 📚 Skills Demonstrated

✅ **Data Cleaning:** Handling mixed data types, treating special values  
✅ **Statistical Analysis:** Descriptive statistics, distributions, correlations  
✅ **Data Visualization:** Multiple chart types for effective communication  
✅ **Business Thinking:** Translating data into actionable insights  
✅ **Python Proficiency:** Pandas, NumPy, Matplotlib/Seaborn

---

## 🎓 Learning Outcomes

From this project, you'll learn:

- How to perform comprehensive EDA
- Techniques for handling categorical data
- Statistical analysis for business insights
- Effective data visualization strategies
- Drawing meaningful conclusions from data

---

## 📊 Sample Visualizations

The notebook includes:

- 📊 Bar charts for cuisine distribution
- 📈 Histograms for order cost analysis
- 🕒 Time series for ordering patterns
- ⭐ Rating distribution analysis
- 📉 Box plots for delivery time comparison

---

## 🔗 Related Projects

- [P0: Hotel Cancellation Prediction](../P0-AIApplicationCaseStudy-HotelCancellation)
- [P2: Personal Loan Campaign](../P2-PersonalLoanCampaign)
- [P3: EasyVisa Immigration](../P3-EnsembleLearning-Visa)

---

## 🔗 Links

- [Back to Main Repository](../)
- [View Full Code Notebook](./P1_FoodHub_VK_Notebook_Full_Code.ipynb)
- [View HTML Export](./P1_FoodHub_VK_Notebook_Full_Code.html)

---

**Author:** Vishal Khapre  
**Project Type:** Exploratory Data Analysis  
**Domain:** Food Delivery Analytics
