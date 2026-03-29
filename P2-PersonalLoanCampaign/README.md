# Appendix
> Learning through experiments and data!

## What was the goal?
To predict whether a liability customer will buy personal loans, to understand which customer attributes are most significant in driving purchases, and identify which segment of customers to target more.

## Why does this matter? (Business Context)
Placeholder: Why does this analysis matter for a business?

## Tech Stack
### Packages Needed For This Module:
- `VKPyKit`
- `matplotlib`
- `numpy`
- `pandas`
- `seaborn`
- `sklearn`
- `uszipcode`

## Stuff I used (Libraries)
VKPyKit, matplotlib, numpy, pandas, seaborn, sklearn, uszipcode

## What did I notice?
- Using uszipcode library to reduce number of values in ZipCode field
Observation
- State does not make much difference, all these are in CA. 
- Also, there are some zipcodes are not mapped to State, which is perticularly an issue. So might as well drop it. 
- Lets favor to the first three digits in Zipcode.
Observation
- State can't be found for some zipcode values, some zip codes are invalid
- So lets use first 3 digits of Zip code.
Observation 
- We reduced the number of unique zip codes from 467 to 57 by taking first 3 digits of zip code.
- It would be interesting to see if we can take first 2 characters? and reduce it further?
Observation
If less than a few unique values, it is worth changing to category columns.

## What I Found (Insights)
* What recommedations would you suggest to the bank?
    - Income, Family size and Higher education are really the main drivers.
    - People with higher income may take personal loan has 30% higher chance than all others 
    - People with "Average spending on credit cards per month" have high disposition 
    - People with "Large family size" are more likely to take a personal loan. 
    - People with "Higher Education" can take personal loan easily.

## What I Learned
- Building classification models for business problems
- Dealing with imbalanced datasets
- Feature engineering for financial data
- Using custom Python packages in ML workflows
- Translating model outputs to business strategies
- Decision Tree interpretation and tuning

---

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

