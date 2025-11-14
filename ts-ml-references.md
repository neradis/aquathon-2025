## Scope
This document summarizes exploration of scientific literature and tech options that might
might be adequate and useful for modeling, forecasting and data synthesis of the time series
data that has been and will be captured in the context of ROSEAU.
Even though some preliminary experiments could be executed during the hackathon, its limited
time frame of the hackathon did not allow in-depth study and evaluation of options
presented.

## Scientific Literature

### Time Series Forecasting
[Deep Learning for Time Series Forecasting: A Survey](https://arxiv.org/pdf/2503.10198)

[Chronos-2: From Univariate to Universal Forecasting](https://arxiv.org/pdf/2510.15821):
State-of-the-art autoregressive deep learning model for forecasting, able to integrate known and unknown exogenous features

[KAIROS: Unified Training for Universal Non-Autoregressive
Time Series Forecasting](https://arxiv.org/pdf/2510.02084v2)
State-of-the-art non-autoregressive model with additional potential for causal inference by examination of routing and expert effects of the mixture-of-experts

### Time Series Generation
[Time-series Generative Adversarial Networks (TimeGAN)](https://papers.nips.cc/paper_files/paper/2019/file/c9efe5f26cd17ba6216bbe2a7d26d490-Paper.pdf)

[SeriesGAN: Time Series Generation via Adversarial and Autoregressive Learning](https://arxiv.org/pdf/2410.21203)

[TIMEVAE: A Variational Auto-Encoder for Multivariate Time Series Generation](https://arxiv.org/pdf/2111.08095)

## Tools / Implementations

[AutoTS: Automated Forecasting](https://winedarksea.github.io/AutoTS/build/html/source/intro.html): Meta-learning framework over a learning space of both various models and respective hyper-parameters

[Time Series Generative Modeling](https://tsgm.readthedocs.io/en/latest/)

[`tsa` module of `statmodels`](https://www.statsmodels.org/stable/tsa.html): Offers various common parametric forecasting models (e.g. (Seasonal) ARIMA) and implementations of common forecasting metrics and cross-validation for time series