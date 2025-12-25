# 📝 W4: Analyzing Text Data

> **Text Analytics Module:** NLP fundamentals and text mining techniques

---

## 📋 Module Overview

**Focus:** Natural Language Processing & Text Mining  
**Content:** 3 comprehensive notebooks  
**Difficulty:** Intermediate  
**Prerequisites:** W1-W3 (Python, Pandas, Data Analysis)

---

## 📚 Content Structure

### 1. Regular Expressions & Data Cleaning

**File:** `ATD-LearnRegEx-DataCleaning.ipynb`

**Topics:**

- **RegEx Basics:** Pattern matching fundamentals
- **Common Patterns:** Email, phone number, URL extraction
- **Data Cleaning:** Removing unwanted characters
- **String Parsing:** Extracting structured data from text

**RegEx Essentials:**

```python
import re

# Pattern matching
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(pattern, text)

# Data cleaning
cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', raw_text)
```

---

### 2. Text Data Analysis

**File:** `AnalyzingTextDataNotebook.ipynb`

**Topics:**

- **Text Preprocessing:**

  - Lowercasing
  - Removing punctuation
  - Tokenization
  - Stop word removal

- **Text Statistics:**

  - Word frequency
  - Document length analysis
  - Vocabulary size

- **Basic NLP:**
  - Sentiment indicators
  - Keyword extraction
  - Text summarization basics

---

## 🎯 Skills Developed

✅ **Regular Expressions** - Pattern matching and extraction  
✅ **Text Cleaning** - Preprocessing unstructured data  
✅ **String Manipulation** - Advanced Python string operations  
✅ **Data Extraction** - Mining information from text  
✅ **NLP Foundations** - Basic natural language processing

---

## 📁 Directory Structure

```
W4-AnalyzeTextData/
├── ATD-LearnRegEx-DataCleaning.ipynb
├── AnalyzingTextDataNotebook.ipynb
└── README.md (this file)
```

---

## 🚀 How to Use

### Installation

```bash
pip install pandas numpy jupyter re
# re is built-in with Python
```

### Run Notebooks

```bash
cd W4-AnalyzeTextData
jupyter notebook
```

**Recommended Order:**

1. Start with RegEx & Data Cleaning
2. Then proceed to Text Data Analysis notebook

---

## 💡 Key Techniques

### Regular Expressions

- **`.`** - Any character
- **`\d`** - Digit
- **`\w`** - Word character
- **`+`** - One or more
- **`*`** - Zero or more
- **`[]`** - Character set
- **`()`** - Grouping

### Text Preprocessing Pipeline

```
Raw Text
   ↓
Lowercase
   ↓
Remove Punctuation
   ↓
Tokenization
   ↓
Remove Stop Words
   ↓
Clean Text Ready for Analysis
```

---

## 🔗 Applications

Text analysis skills are used in:

- **Customer Feedback Analysis**
- **Social Media Monitoring**
- **Email Classification**
- **Document Processing**
- **Data Extraction from PDFs/HTMLs**

---

## 🎓 Learning Outcomes

- Master regular expressions for pattern matching
- Clean and preprocess text data efficiently
- Extract structured information from unstructured text
- Foundation for advanced NLP projects
- Practical string manipulation techniques

---

## 🔗 Links

- [Back to Main](../)
- [Previous: EDA](../W3-ExploratoryDataAnalysis)
- [Next: Linear Regression](../W5-LinearRegression)

---

**Module:** W4 | **Type:** Text Analytics | **Key Tool:** Regular Expressions
