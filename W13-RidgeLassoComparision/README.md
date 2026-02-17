# W13: Ridge vs Lasso - Which One Actually Works?

> Trying to figure out if Ridge or Lasso is better (spoiler: depends on what you're doing)

## What's this about?

Comparing **Ridge** and **Lasso** regression to see how different regularization techniques actually work. Both stop overfitting, but they do it differently - Ridge just shrinks coefficients, Lasso can kill them entirely.

Took me a while to understand why you'd want one over the other.

## The Data

**Car MPG Dataset** - 398 cars with stuff like:

- `mpg` - Miles per gallon (what we're trying to predict)
- `cyl` - Cylinders
- `disp` - Displacement
- `hp` - Horsepower
- `wt` - Weight
- `acc` - Acceleration
- `yr` - Year
- `origin` - Where it's from
- `car_type` - Type

Goal: predict fuel efficiency based on car specs

## What I compared

1. **Linear Regression** - baseline, no regularization
2. **Ridge Regression** - L2 regularization
3. **Lasso Regression** - L1 regularization

## Stuff I used

- **Feature Scaling** - StandardScaler (turns out this matters a LOT for regularization)
- **Cross-Validation** - finding the right amount of regularization (GridSearch took forever but worth it)
- **Regularization** - Ridge (L2) vs Lasso (L1)
- **Metrics** - R² score, MSE, RMSE

## What I found out

- **Feature scaling is really important** - without it, regularization barely works
- Ridge is better when you think all features actually matter
- Lasso just zeros out coefficients it doesn't like (automatic feature selection - pretty cool)
- Both prevent overfitting way better than plain linear regression
- Finding the right regularization strength takes some trial and error (cross-validation helps)

## What I learned

- Regularization isn't just theory - it actually works
- Scaling your features before regularizing makes a huge difference (learned this the hard way)
- Use Lasso when you suspect some features are useless
- Use Ridge when you want all features but need to control their impact
- Cross-validation is worth the extra time (even though it's slow)

## Files

- `RidgeLasso.ipynb` - all the comparisons
- `car-mpg.csv` - car data

---

**TL;DR:** Ridge shrinks everything a bit, Lasso picks winners and kills the rest. Both beat regular regression.

[🔙 Back to Main Repository](../README.md)
