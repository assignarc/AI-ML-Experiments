# Problem Statement
> Learning through experiments and data!

## What was the goal?
Develop an image classification model using CNN to accurately categorize endangered monkey species, enabling the wildlife sanctuary to nhance conservation efforts.

## Why does this matter? (Business Context)
In recent years, habitat destruction, climate change, and poaching have driven several monkey species to extinction, with many more classified as endangered. Conservation efforts worldwide increasingly rely on data-driven approaches to monitor and protect these species. A U.S.-based wildlife sanctuary has taken a proactive step by collecting extensive image datasets of endangered monkey species from different continents to aid in conservation and research efforts.

## Tech Stack
Keras, Matplotlib, NumPy, OpenCV, Pandas, Scikit-learn, Seaborn, TensorFlow

## Stuff I used (Libraries)
cv2, keras, matplotlib, numpy, pandas, seaborn, sklearn, tensorflow

## What did I notice?
-  Due to the large volume of data, the images were converted to the images.npy file and the labels are also placed in Labels.csv, allowing you to work on the data without being concerned about the large data volume.
- The dataset comprises of 10 monkey species.

## What I Found (Insights)
- Adding a feed-forward neural network on top of the VGG-16 model significantly improved performance. This suggests that while the pre-trained features were beneficial, further refining them with an additional neural network tailored to our dataset enhanced the results.

## What I Learned
Placeholder: What was the biggest takeaway?

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

