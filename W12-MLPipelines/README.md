# W12: ML Pipelines

> Trying to figure out how to stop copy-pasting the same preprocessing code everywhere (there had to be a better way)

## What's this?

Learned about **ML Pipelines** - basically a way to chain all your ML steps together so you don't have to manually run scaling, encoding, and modeling separately. Sounds simple but it actually prevents some sneaky bugs (like accidentally fitting your scaler on test data - oops, did that once).

## What's in here

### SimplePipeline

Hands-on example of building basic pipelines with scikit-learn. Check out the [SimplePipeline folder](./SimplePipeline) to see how it works.

## Why bother with pipelines?

- **Prevents data leakage** - Learned this the hard way. Pipelines make sure you only fit transformations on training data
- **Way cleaner code** - No more juggling 5 different variables to track transformations
- **Actually reproducible** - Same pipeline works on new data without manual steps (finally!)
- **Cross-validation friendly** - Makes CV way less painful

## What I figured out

- Pipelines make everything so much more maintainable (wish I knew this earlier)
- `Pipeline` and `ColumnTransformer` together are pretty powerful
- Stops you from making dumb mistakes like fitting scalers on test data
- Makes deployment easier - just pickle the whole pipeline, not every step

---

**What I learned:** Stop manually running every preprocessing step. Use pipelines.

[🔙 Back to Main Repository](../README.md)


---

## Tech Stack
### Packages Needed For This Module:
- `numpy`
- `pandas`
- `sklearn`
