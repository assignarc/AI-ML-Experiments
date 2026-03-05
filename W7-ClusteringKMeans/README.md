# 🎯 W7: K-Means Clustering

> **Unsupervised Learning Module:** Partitioning-based clustering for customer segmentation

---

## 📋 Module Overview

**Focus:** K-Means Clustering Algorithm 
**Content:** 4 notebooks across 2 case studies 
**Difficulty:** Intermediate 
**Prerequisites:** W1-W6 (Python, EDA, ML basics)

---

## 📚 Case Studies

### 1. Credit Card Customer Segmentation

**Directory:** `CreditCardSegmentation/` 
**Objective:** Identify customer groups for targeted marketing 
**Features:** Spending patterns, credit utilization, payment behavior

### 2. Retail Customer Segmentation

**Directory:** `RetailSegmentation/` 
**File:** `KMeansClustering.ipynb` 
**Objective:** Customer behavior clustering for business insights

---

## 🎯 Key Concepts

### K-Means Algorithm

1. Choose K (number of clusters)
2. Initialize K centroids randomly
3. Assign each point to nearest centroid
4. Update centroids (mean of assigned points)
5. Repeat steps 3-4 until convergence

### Optimal K Selection

- **Elbow Method:** Plot SSE vs. K, find "elbow"
- **Silhouette Score:** Measure cluster quality (-1 to 1)
- **Domain Knowledge:** Business requirements

---

## 💡 Skills Developed

✅ K-Means implementation and optimization 
✅ Elbow Method for K selection 
✅ Silhouette analysis 
✅ Feature scaling importance 
✅ Cluster profiling and interpretation 
✅ Customer segmentation strategies

---

## 📁 Structure

```
W7-ClusteringKMeans/
├── CreditCardSegmentation/
│ └── CustomerSegmentationNotebook.ipynb
├── RetailSegmentation/
│ └── KMeansClustering.ipynb
└── README.md
```

---

## 🚀 Usage

```bash
cd W7-ClusteringKMeans
jupyter notebook
```

---

## 🔗 Links

- [Back to Main](../)
- [Previous: Decision Trees](../W6-DecisionTree)
- [Next: Hierarchical Clustering](../W8-ClusteringHierarchical)

---

**Module:** W7 | **Type:** Unsupervised Learning | **Focus:** K-Means


---

## Tech Stack
### Packages Needed For This Module:
- `matplotlib`
- `numpy`
- `pandas`
- `plotly`
- `seaborn`
- `sklearn`
