import yfinance as yf

STOCKS_LIST = ['EUCA4', 'CPLE3']

FIXED_SYMBOLS_STOCKS_LIST = [f'{symbol}.SA' for symbol in STOCKS_LIST]


def get_tickers_info_by_period(tickers: yf.Tickers, period: str) -> list:
    tickers_period_info = []

    for ticker in tickers.tickers:
        ticker_data_frame_for_current_day = tickers.tickers[ticker].history(period)

        tickers_period_info.append({
            'symbol': ticker,
            'today_data': {
                'open': ticker_data_frame_for_current_day.Open.values[0],
                'close': ticker_data_frame_for_current_day.Close.values[0],
                'high': ticker_data_frame_for_current_day.High.values[0],
                'low': ticker_data_frame_for_current_day.Low.values[0]
            }
        })

    return tickers_period_info


if __name__ == "__main__":
    tickers = yf.Tickers(FIXED_SYMBOLS_STOCKS_LIST)

    tickers_daily_info = get_tickers_info_by_period(tickers, '1d')

    print(len(tickers_daily_info))
    print(tickers_daily_info)
