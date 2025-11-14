## Conceptual Brainstorming

```mermaid
mindmap
  root(ROSEAU data processing & analytics)
    analytics
      forecasting
        models
          parametric models
          deep-learning models
      causal inference
        regression analysis
        mixture-of-experts models
      trend-seasonal-residual split
      time series generation
    dashboards/UI
      data augmentaion for prototyping/demos
    data preprocessing
      transformation to equidistant time series
      search for and mitigation of data gaps
    data acquisition
      historical weather/climate data
      short term & long term weather forecasts
      demographic and econometric data
    data pipelines & MLOps
      workflow engines/DAG execution tools
      integration of existing code for processing and analytics
      GitOps-style automated deployment

```


## data preprocessing
### transformation to equidistant time series
Many models for time series analysis/forecasting work with the assumption that data points in examined series refert to regular, equidistant points in time (e.g. exactly each 10 seconds), which is not a property given in the current data captured by the prototype.
Many data processing libraries/packages offer however helper functions to re-sample time series into equidistant ones by various heuristings (interpolation, min, max, ...).

## analytics
### causal inference
Causal inference methods on fitted models can give insights that can be translated into in-domain hypotheses like 'water source X is especially influenced by intensity of sunlight'.
### trend-seasonal-residual split
Time series can often be decomposed in trend, seasonality and residuals, which can often help to create more clearly interpretable visualisations, especially trend lines.
