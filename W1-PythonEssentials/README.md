# 📊 W1: Python Essentials for Data Science

> **Foundation Module:** Core Python libraries essential for data science workflows

---

## 📋 Module Overview

**Focus:** NumPy, Pandas, and Python for Data Science 
**Content:** 11 notebooks 
**Difficulty:** Beginner to Intermediate 
**Prerequisites:** Basic Python (W0 recommended)

### What I\'m trying to do

- Master NumPy for numerical computing
- Learn Pandas for data manipulation and analysis
- Understand OOP concepts in Python
- Work with file systems using OS module
- Apply Python to data science problems

---

## 📚 Content Structure

### 1. Introduction to Python for Data Science

**File:** `Python_For_Data_Science_Intro.ipynb`

**Topics:**

- Python in data science ecosystem
- Jupyter notebook workflows
- Data science libraries overview

---

### 2. NumPy - Numerical Python

**File:** `Hands_on_Notebook_NumPy.ipynb`

**Topics Covered:**

- **NumPy Arrays:** Creation, indexing, slicing
- **Array Operations:** Element-wise operations, broadcasting
- **Mathematical Functions:** Statistical operations, linear algebra
- **Array Manipulation:** Reshaping, stacking, splitting
- **Performance:** Why NumPy is faster than pure Python

**Key Concepts:**

```python
import numpy as np

# Array creation
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# Operations
arr * 2 # Broadcasting
np.mean(arr) # Statistics
np.dot(matrix, matrix) # Linear algebra
```

---

### 3. Pandas - Data Analysis Library

**File:** `Hands_on_Notebook_Pandas.ipynb`

**Topics Covered:**

- **Series & DataFrames:** Core pandas data structures
- **Data Loading:** Reading CSV, Excel, SQL databases
- **Data Inspection:** head(), tail(), info(), describe()
- **Indexing:** loc[], iloc[], boolean indexing
- **Data Cleaning:** Handling missing values, duplicates
- **Aggregation:** groupby(), pivot_table()
- **Merging:** concat(), merge(), join()

**Key Operations:**

```python
import pandas as pd

# DataFrame creation
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Data manipulation
df.groupby('column').agg({'value': 'mean'})
df.merge(df2, on='key')
df.fillna(0) # Handle missing values
```

---

### 4. Object-Oriented Programming in Python

**File:** `OOP_in_python.ipynb`

**Topics Covered:**

- **Classes and Objects:** Defining classes, creating instances
- **Attributes:** Instance vs. class attributes
- **Methods:** Instance methods, class methods, static methods
- **Inheritance:** Single and multiple inheritance
- **Encapsulation:** Private and protected members
- **Polymorphism:** Method overriding

**OOP Example:**

```python
class DataProcessor:
 def __init__(self, data):
 self.data = data

 def clean_data(self):
 # Data cleaning logic
 pass

 def analyze(self):
 # Analysis logic
 pass
```

---

### 5. Operating System Module

**File:** `Operating_system_module.ipynb`

**Topics Covered:**

- **File System Navigation:** os.listdir(), os.getcwd()
- **Path Operations:** os.path.join(), os.path.exists()
- **File Operations:** Creating, deleting, renaming
- **Directory Management:** Making and removing directories
- **Environment Variables:** os.environ

---

### 6. Debugging Techniques

**File:** `Debugging.ipynb`

**Topics Covered:**

- Using print statements effectively
- Python debugger (pdb)
- Understanding error messages
- Common errors and solutions
- Best practices for debugging

---

### 7. Case Study: MovieLens

**File:** `Session_Notebook_AIML_Movie_Lens_Notebook.ipynb`

**Application of Skills:**

- Real-world dataset analysis
- Applying NumPy and Pandas
- Data exploration techniques
- Introduction to recommendation systems

---

## 🎯 Skills Developed

✅ **NumPy Proficiency** - Array operations and numerical computing 
✅ **Pandas Mastery** - Data manipulation and analysis 
✅ **OOP Understanding** - Object-oriented design in Python 
✅ **File System Operations** - Working with files and directories 
✅ **Debugging Skills** - Finding and fixing errors efficiently 
✅ **Practical Application** - MovieLens case study

---

## 📁 Directory Structure

```
W1-PythonEssentials/
├── Hands_on_Notebook_NumPy.ipynb
├── Hands_on_Notebook_Pandas.ipynb
├── Hands_on_notebook_introduction_to_Python.ipynb
├── Python_PreWork_Session.ipynb
├── Session_Notebook_AIML_Movie_Lens_Notebook.ipynb
├── Exercise 1/
│ └── Python_For_Data_Science_Intro.ipynb
├── Exercise 2/
│ ├── Debugging.ipynb
│ ├── OOP_in_python.ipynb
│ └── Operating_system_module.ipynb
├── PreReq/
└── README.md (this file)
```

---

## Running This
### Packages Needed For This Module:
- `google`
- `numpy`
- `pandas`


### Installation

```bash
# Install required libraries
pip install numpy pandas jupyter matplotlib

# Or from the repository root
pip install -r requirements.txt
```

### Running Notebooks

```bash
# Navigate to this directory
cd W1-PythonEssentials

# Launch Jupyter
jupyter notebook

# Open any .ipynb file and run cells sequentially
```

---

## 📈 Learning Path

```
1. Introduction to Python for DS
 ↓
2. NumPy Fundamentals
 ↓
3. Pandas Data Analysis
 ↓
4. OOP Concepts
 ↓
5. OS Module & File Operations
 ↓
6. Debugging Techniques
 ↓
7. Case Study Application (MovieLens)
```

---

## 💡 Best Practices Learned

- **NumPy:** Use vectorized operations instead of loops
- **Pandas:** Method chaining for cleaner code
- **OOP:** Design reusable, modular code
- **Debugging:** Systematic approach to error resolution
- **Code Quality:** Write readable, documented code

---

## 🔗 Connections to Projects

These skills are applied in:

- **P1: FoodHub** - Pandas for order analysis
- **P2: Personal Loan** - Data manipulation and cleaning
- **P3: EasyVisa** - Large dataset handling with Pandas
- **All Projects** - NumPy for numerical computations

---

## 🔗 Next Steps

- **[W2: MovieLens Analysis](../W2-MovieLens)** - Deep dive into recommendation data
- **[W3: Exploratory Data Analysis](../W3-ExploratoryDataAnalysis)** - EDA techniques

---

## 📖 Additional Resources

- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python OOP Tutorial](https://docs.python.org/3/tutorial/classes.html)

---

## 🔗 Links

- [Back to Main Repository](../)
- [Previous: Python Training](../W0-PythonTrainings)
- [Next: MovieLens Analysis](../W2-MovieLens)

---

**Module:** W1 
**Type:** Data Science Foundations 
**Notebooks:** 11 
**Key Libraries:** NumPy, Pandas
