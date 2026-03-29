# MachineFailure
> Learning through experiments and data!

## What was the goal?
AutoMobi has recently been encountering a problem with frequent equipment failure in the fuel injector nozzle manufacture unit, leading to disturbance in the manufacturing process. They have reached out to the Data Science team for a solution and shared data for the past three months. As a member of the Data Science team, you are tasked with analyzing the data and developing a Machine Learning model to detect potential machine failures, determine the most influencing factors on machine health, and provide recommendations for cost optimization to the management.

## Why does this matter? (Business Context)
System failure is a common issue across the manufacturing industry, where a variety of machines and equipment are used. In most cases, it becomes important to be able to predict machine failures by analyzing system data and taking preventive measures to be able to tackle them. This is known as predictive maintenance and with the rising availability of data and computational resources, the use of such data-driven, proactive maintenance methods has resulted in several benefits like minimized downtime of the equipment, minimized cost associated with spares and supplies, etc.

## Tech Stack
Matplotlib, NumPy, Pandas, Scikit-learn, Seaborn

## Stuff I used (Libraries)
matplotlib, numpy, pandas, seaborn, sklearn

## What did I notice?
* There are three types of products those are L, M, and H (Low, Medium, and High quality).
* The `UDI` column is containing unique values.
* The dataset has 10000 rows and 8 columns.
* The `Type` column is of *object* type while the rest columns are numeric in nature
* There are no null values in the dataset
* There are no duplicate values in the data.
* The `UDI` column contains only unique values, so we can drop it
**Let's check the statistical summary of the data.**
* The `air temperature` ranges from 300K to 304.5K. Usually, machine shops are maintained in control environment so the temperature range looks usual.
* The `process temperature` is a bit higher than the `air temperature` and that's quite usual because heat is continuously generated during the machining process.
* The `rotational speed` has a max value of 2886rpm while 1612rpm at the 75th percentile. Some of the processes are performed at a higher speed than usual.

## What I Found (Insights)
Placeholder: What did you find out?

## What I Learned
Placeholder: What was the biggest takeaway?

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

