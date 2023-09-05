# House Price Prediction - Tehran

## Overview
This project aims to predict house prices in Tehran using various machine learning algorithms. It involves data preprocessing, model building, sensitivity analysis, and visualization. The project uses Python and several libraries such as Pandas, scikit-learn, XGBoost, LightGBM, and SALib.

## Project Structure
The project is organized into several main parts:

1. **Data**: The data used for this project is stored in Excel files. The dataset contains information about houses, including features like area, floor, meterage, age, room count, parking availability, storeroom availability, and elevator availability.

2. **Machine Learning Models**: Multiple machine learning algorithms are employed to build predictive models for house prices. These algorithms include:
   - Bayesian Ridge
   - Elastic Net
   - Gradient Boosting Regressor
   - Kernel Ridge
   - Lasso
   - LightGBM Regressor
   - Linear Regression
   - Stochastic Gradient Descent Regressor
   - Support Vector Regressor
   - XGBoost Regressor

3. **Sensitivity Analysis**: Sensitivity analysis is performed using the Morris method from the SALib library. This analysis assesses how changes in input features impact house price predictions. Sensitivity results are calculated for each algorithm.

4. **Sensitivity Plots**: After sensitivity analysis, bar plots are generated to visualize the sensitivity of each feature for each algorithm. These plots help understand which features have the most influence on predictions.

5. **File Paths**: The project includes file paths to specify where input data is located, where results are saved, and where sensitivity plots are stored.

## Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.x
- Required libraries (install using `pip install library_name`):
  - Pandas
  - scikit-learn
  - XGBoost
  - LightGBM
  - SALib
  - Seaborn
  - Matplotlib

## Running the Project
1. Clone or download this repository to your local machine.

2. Ensure that your dataset is in the correct Excel format and specify the file path in the code.

3. Run the `main.py` script to execute the entire pipeline.

## Results
- The project will generate Excel files containing sensitivity analysis results for each algorithm.
- Sensitivity plots (bar charts) for each algorithm will be saved in the specified directory.

## Contributing
If you'd like to contribute to this project, please follow these guidelines:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit with descriptive messages.
4. Push your branch to your forked repository.
5. Create a pull request, explaining your changes.


## Acknowledgments
- Thanks to the developers of the Pandas, scikit-learn, XGBoost, LightGBM, and SALib libraries.
- Special thanks to the open-source community for providing valuable resources and tools.
