import yfinance as yf

STOCKS_LIST = ['EUCA4', 'CPLE3', 'CPLE6', 'PCAR3', 'DOHL4', 'SAPR3', 'SAPR11', 'SAPR4', 'MTSA4', 'TRPL4', 'CLSC4',
               'EALT4', 'CSMG3', 'ENBR3', 'TRPL3', 'CMIG4', 'EUCA3', 'CMIN3', 'JHSF3', 'AURA33', 'CRPG6', 'SULA4',
               'USIM5', 'VALE3', 'GGBR3', 'USIM3', 'SULA11', 'PETR4', 'CMIG3', 'PETR3', 'CAML3', 'CESP6', 'CRPG5',
               'TAEE11', 'TAEE3', 'TAEE4', 'NEOE3', 'ALUP3', 'ALUP11', 'ALUP4', 'GOAU3', 'SULA3', 'GGBR4', 'SBSP3',
               'GOAU4', 'TIMS3', 'TEND3', 'JBSS3', 'UNIP3', 'LIGT3', 'TRIS3', 'CESP3', 'SEER3', 'UNIP5', 'AGRO3',
               'CYRE3', 'WHRL3', 'UNIP6', 'BRDT3', 'CPFE3', 'RAPT3', 'LEVE3', 'PLPL3', 'CRFB3', 'MRFG3', 'EVEN3',
               'FRAS3', 'EQTL3', 'RAPT4', 'VIVT3', 'GPCP3', 'GPIV33', 'PSSA3', 'DIRR3', 'WHRL4', 'CURY3', 'SLCE3',
               'ENGI4', 'MRVE3', 'RSUL4', 'FESA4', 'LAVV3', 'PARD3', 'ELET6', 'ELET3', 'EQPA3', 'CSNA3', 'BEEF3',
               'POSI3', 'KEPL3', 'RANI3', 'ENGI11', 'ALLD3', 'COCE5', 'ROMI3', 'UCAS3', 'WSON33', 'MDIA3', 'QUAL3',
               'CCPR3', 'TGMA3', 'CARD3', 'HGTX3', 'PFRM3', 'EGIE3', 'GRND3', 'CGRA4', 'SHUL4', 'SMTO3', 'WIZS3',
               'POWE3', 'ETER3', 'POMO3', 'PTNT4', 'OFSA3', 'MTRE3', 'POMO4', 'DTEX3', 'REDE3', 'SCAR3', 'ENAT3',
               'HYPE3', 'ITSA4', 'ABEV3', 'MILS3', 'ITSA3', 'MOVI3', 'PTBL3', 'CIEL3', 'AMBP3', 'PNVL4', 'PNVL3',
               'JSLG3', 'TOTS3', 'LCAM3', 'B3SA3', 'ENGI3', 'HBOR3', 'JPSA3', 'SIMH3', 'NGRD3', 'ALSO3', 'BOAS3',
               'ODPV3', 'CCRO3', 'MELK3', 'VIVA3', 'UGPA3', 'FLRY3', 'ARZZ3', 'LJQQ3', 'RADL3', 'BTTL3', 'SMLS3',
               'HAPV3', 'GNDI3', 'LOGG3', 'ASAI3', 'BRPR3', 'MULT3', 'LAME3', 'ATOM3', 'LAME4', 'WEGE3', 'LREN3',
               'TUPY3', 'PGMN3', 'ESPA3', 'IGTA3', 'MGLU3', 'VVAR3', 'GMAT3', 'TASA3', 'TASA4', 'EMAE4', 'CAMB3',
               'PTNT3', 'VULC3', 'SQIA3', 'BRFS3', 'RENT3', 'EZTC3', 'CSAN3', 'CGAS5', 'ANIM3', 'INTB3', 'CBEE3',
               'STBP3', 'PETZ3', 'RDOR3', 'ALPA3', 'PRIO3', 'LWSA3', 'RAIL3', 'ALPA4', 'ENEV3', 'PDTC3', 'KLBN4',
               'LPSB3', 'KLBN11', 'LOGN3', 'OMGE3', 'KLBN3', 'TFCO4', 'TPIS3', 'MGEL4', 'DMVF3', 'CTKA4', 'CTSA3',
               'CTSA4', 'VAMO3', 'MNPR3', 'TECN3', 'BMOB3', 'MDNE3', 'MOSI3', 'CSED3', 'HAGA4', 'SOJA3', 'MATD3',
               'SGPS3', 'CEDO4', 'HAGA3', 'LUPA3', 'RDNI3', 'CTNM4', 'YDUQ3', 'TESA3', 'NTCO3', 'VLID3', 'MNDL3',
               'CEBR6', 'CEBR3', 'BLAU3', 'CASH3', 'BSEV3', 'MYPK3', 'FHER3', 'AALR3', 'GFSA3', 'DASA3', 'BOBR4',
               'BTOW3', 'OPCT3', 'LINX3', 'BRML3', 'EMBR3', 'AMAR3', 'ORVR3', 'BRKM3', 'BRKM5', 'ALPK3', 'HBRE3',
               'ECOR3', 'SEQL3', 'BBSE3', 'SUZB3', 'HBSA3', 'BBAS3', 'BRAP3', 'BEES3', 'BRSR6', 'BRSR3', 'BMGB4',
               'BRAP4', 'GUAR3', 'ABCB4', 'BBDC3', 'SANB3', 'SOMA3', 'ITUB3', 'SANB11', 'SANB4', 'ITUB4', 'BBDC4',
               'BPAC5', 'MWET4', 'IRBR3', 'RCSL4', 'PRNR3', 'BPAC11', 'RSID3', 'MBLY3', 'MMXM3', 'BPAN4', 'WEST3',
               'DMMO3', 'CEAB3', 'MEAL3', 'BSLI3', 'BKBR3', 'AZEV3', 'BPAC3', 'AZEV4', 'COGN3', 'TELB4', 'TCSA3',
               'FRTA3', 'RNEW4', 'SBFG3', 'JBDU3', 'JBDU4', 'PLAS3', 'PMAM3', 'RPMG3', 'SNSY5', 'BDLL4', 'SLED3',
               'PDGR3', 'SLED4', 'TEKA4', 'BDLL3', 'LLIS3', 'CXSE3', 'ATMP3', 'ELMD3', 'GOLL4', 'OSXB3', 'OIBR3',
               'BBRK3', 'AVLL3', 'AESB3', 'AZUL4', 'OIBR4', 'VIVR3', 'RRRP3', 'SHOW3', 'BIDI11', 'BIDI3', 'BIDI4',
               'BIOM3', 'APER3', 'RECV3', 'JFEN3', 'AERI3', 'PINE4', 'INEP4', 'INEP3', 'ENJU3', 'JALL3', 'CVCB3',
               'MODL4', 'MODL11', 'GGPS3', 'MODL3', 'IFCM3', 'TCNO3', 'TCNO4', 'DOTZ3', 'IGBR3', 'NINJ3']

FIXED_SYMBOLS_STOCKS_LIST = [f'{symbol}.SA' for symbol in STOCKS_LIST]


def get_tickers_info_by_period(tickers: yf.Tickers, period: str) -> list:
    tickers_period_info = []

    for ticker in tickers.tickers:
        ticker_data_frame_for_current_day = tickers.tickers[ticker].history(period)

        # Some Errors occurs when the Symbol is not Found in Yahoo. This Occurred 3 times during test phase.
        # In all the times the reason was that the stock has changed recently it's symbol.
        try:
            tickers_period_info.append({
                'symbol': ticker,
                'today_data': {
                    'open': ticker_data_frame_for_current_day.Open.values[0],
                    'close': ticker_data_frame_for_current_day.Close.values[0],
                    'high': ticker_data_frame_for_current_day.High.values[0],
                    'low': ticker_data_frame_for_current_day.Low.values[0]
                }
            })
        except IndexError as e:
            print(f'Index Error Occured on {ticker}')

    return tickers_period_info


if __name__ == "__main__":
    tickers = yf.Tickers(FIXED_SYMBOLS_STOCKS_LIST)

    tickers_daily_info = get_tickers_info_by_period(tickers, '1d')

    print(len(tickers_daily_info))
    print(tickers_daily_info)
