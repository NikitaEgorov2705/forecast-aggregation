# Testing Forecast Aggregation Methods

## Overview
This project evaluates various forecast aggregation methods by comparing their performance using the **Brier score**, a metric that assesses the accuracy of probabilistic predictions.
I also propose a new aggregation method which outperforms ones tested previously on these datasets.  

## Data
The project utilizes datasets from the Hybrid Forecasting Competition (HFC), an initiative by IARPA designed to explore and develop predictive models that integrate human and machine forecasting capabilities. The competition aimed to leverage the complementary strengths of human intuition and automated predictive systems for complex geopolitical event forecasting.

### About the Competition
The HFC challenged participants to forecast the likelihood of various geopolitical events, such as military conflicts, shifts in economic indicators, and political developments. The competition's focus was on enhancing forecast accuracy by combining traditional and machine-based approaches.

### Data Source and Scope
The original datasets are available publicly on Harvard Dataverse (https://dataverse.harvard.edu/dataverse/hfc). For this project, only the RCTA datasets, which cover the first year of the HFC, were selected for analysis. These datasets include detailed records of human and machine forecasts, providing a rich data for testing aggregation methods.
The RCTA datasets can be found in the project repository as feather files.

## Methodology
1. **EDA**: Exploration and description of 3 datasets.
3. **Tranformation & Aggregation**: The datasets are merged, transformed and aggregated using common forecast aggregation methods:
    Raw Mean: Simple average of all forecasts.
    Median: The middle value of the sorted forecasts, reducing the effect of outliers.
    Geometric Mean: The nth root of the product of forecasts, offering a multiplicative aggregation perspective.
    Trimmed Mean: Calculated by trimming the top and bottom 10% of forecasts to minimize the influence of extreme values.
    Geometric Mean of Odds: An adaptation that uses the odds of the forecasts instead of probabilities.
5. **Brier score evaluation**: Assessed the performance of each aggregation method using the Brier score, a metric that evaluates the accuracy of probabilistic forecasts by measuring the mean squared difference between predicted probabilities and actual outcomes.
6. **Weighted probabilities**: Introduced and tested a new aggregation method based on weighted probabilities, in which weights are assigned to forecasts based on the variance of each forecast every day.
This method demonstrated improved performance compared to traditional aggregation techniques, yielding a lower Brier score on the tested datasets.

## Results
### Ranking of Aggregation Methods by Brier Score
1. Weighted Forecast: 0.1267
   This method demonstrated the best overall accuracy, leveraging a mean of weighted probabilities derived from the variance of forecast probabilities across days. By assigning lower weights to forecasts with higher variance, this method effectively reduces the influence of uncertain predictions, leading to a more reliable aggregated forecast.
2. Trimmed Mean: 0.1285
   The trimmed mean ranked second, effectively mitigating the impact of extreme values by excluding the top and bottom 10% of forecasts. This aggregation method provides a better reflection of the central tendency of the data, leading to improved accuracy.
3. Raw Mean: 0.1286
   The raw mean achieved a Brier score very close to the trimmed mean, indicating solid performance as a straightforward averaging method. However, it does not address outliers, which can skew results.
4. Median: 0.1296
   The median performed slightly less accurately than both the raw and trimmed means. While it effectively reduces the influence of outliers, its failure to consider the full distribution of predictions results in a marginally lower accuracy.
5. Geometric Mean of Odds: 0.1341
   This method exhibited performance similar to the geometric mean, highlighting its limitations. The presence of many zero and low-value probabilities led to skewed results, making it less effective for this dataset.
6. Geometric Mean: 0.1344
    The geometric mean ranked lowest, affected by the skewing effect of small values and zeros. Since the geometric mean multiplies all values and takes the root, any zero probability in the set results in an aggregated value of zero, leading to less accurate forecasts.

The results of this project highlight the importance of effectively aggregating forecasts to improve accuracy in predicting complex geopolitical events. Among the methods tested, the weighted forecast method proved to be the most effective, achieving the lowest Brier score. By leveraging the variance of forecast probabilities as a proxy for certainty, this method successfully reduced the influence of less reliable predictions. Overall, while reducing the influence of outliers is beneficial in addressing forecasting overconfidence, incorporating controls for other factors, such as forecasting variability over time, could enhance the robustness of prediction methods.  

## How to Run
1. Clone the repo: `git clone https://github.com/NikitaEgorov2705/forecast-aggregation.git`
2. Navigate to the project directory: `cd forecast-aggregation`
3. Run the notebook: `jupyter notebook NFC_nb.ipynb`
Note: Python dependencies will be checked and installed automatically through the notebook code if needed.


## Contact
naegorov2705@gmail.com
