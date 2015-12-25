
import numpy as np
import scipy
import matplotlib.pyplot as plt
import moreLinearRegression as lr
import statsmodels.api as sm
import pylab
import scipy.stats as stats


def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''

    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist()


    # Histogram for residuals
    predictedVal = lr.predictions(turnstile_weather);
    (weather_turnstile['ENTRIESn_hourly'] - predictedVal).hist(bins = 100)

    ## line chart for residuals
    plt.plot(weather_turnstile['ENTRIESn_hourly'] - predictedVal);
    plt.ylabel('Residuals')
    plt.show();

    ## qqplot of the residuals to test for normality
    stats.probplot(weather_turnstile['ENTRIESn_hourly'] - predictedVal, dist="norm", plot=pylab)
    pylab.show();

    return plt


# plt.close('all');
# pylab.close('all');



