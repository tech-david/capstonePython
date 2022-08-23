from model.dataset.FullDataset import min_max_data, build_target


def drop_high_vif():
    df = min_max_data()
    df.drop(columns=["Natural Gas Price, Citygate",
                     "Natural Gas Price, Delivered to Consumers, Commercial",
                     "Natural Gas Price, Delivered to Consumers, Industrial",
                     "Natural Gas Price, Electric Power Sector",
                     "Average Retail Price of Electricity, Commercial",
                     "Average Retail Price of Electricity, Total",
                     "Unleaded Premium Gasoline, U.S. City Average Retail Price",
                     "All Grades of Gasoline, U.S. City Average Retail Price",
                     "Regular Motor Gasoline, Conventional Gasoline Areas, Retail Price",
                     "Regular Motor Gasoline, Reformulated Gasoline Areas, Retail Price",
                     "Regular Motor Gasoline, All Areas, Retail Price",
                     "Homes Median Sales Price",
                     "Gasoline_all",
                     "Unleaded Regular Gasoline, U.S. City Average Retail Price",
                     "Leaded Regular Gasoline, U.S. City Average Retail Price",
                     "Beef_Ground_Chuck"],
            inplace=True)
    return df


def complete_df():
    x = drop_high_vif()
    y = build_target()
    df = x
    df = df.join(y)
    target = df.pop('USREC')
    df.insert(0, 'USREC', target)
    # df.index = pd.to_datetime(df.index)
    # Fill remaining NaN using interpolation
    df.interpolate(method='time',
                   inplace=True,
                   axis=0,
                   limit_direction='both')
    return df
