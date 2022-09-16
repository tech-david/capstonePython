from helpers.Cleaner import fill_gas_na, fill_electricity_na, fill_oil_na, resample_house, fill_cpi_na


def get_all_features():
    # Getting common columns to drop
    col = ['Year', 'Month', 'Day', 'Date']
    df_ng = fill_gas_na()
    df_ng.drop(columns=col, inplace=True)
    df_elec = fill_electricity_na()
    df_elec.drop(columns=col, inplace=True)
    df_oil = fill_oil_na()
    df_oil.drop(columns=col, inplace=True)
    df_house = resample_house()
    df_house = df_house.rename(columns={'Average Sales Price': 'Homes Average Sales Price',
                                        'Median Sales Price': 'Homes Median Sales Price'})
    df_cpi = fill_cpi_na()
    df_cpi.drop(columns=col[0],
                inplace=True)

    df = df_ng
    # Merging on different columns (outer), sorting to keep chronological order
    df = df.merge(df_elec, how='outer', on='Date', sort=True)
    df = df.merge(df_oil, how='outer', on='Date', sort=True)
    df = df.join(df_house)
    df = df.join(df_cpi)
    return df
