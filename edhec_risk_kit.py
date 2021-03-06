import pandas as pd

def drawdown(return_series: pd.Series):
    """
    Takes time series of asset returns
    Computes and returns a DataFrame containing:
    wealth index
    previous peaks
    percent drawdowns
    """
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    return pd.DataFrame({
        "Wealth": wealth_index,
        "Peaks": previous_peaks,
        "Drawdown": drawdowns})

def get_ffme_returns():
    """
    Load Fama_french Dataset for the returns of the Top and Bottom Deciles by MarketCap    
    """
    file = pd.read_csv("Portfolios_Formed_on_ME_monthly_EW.csv",
                  header=0, index_col=0, parse_dates=True, na_values=-99.99)

    rets = file[['Lo 10', 'Hi 10']]
    rets.columns = ['SmallCap', 'LargeCap']
    rets = rets/100
    rets.index = pd.to_datetime(rets.index, format="%Y%m").to_period('M')
    return rets
