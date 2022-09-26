from model.dataset.FullDataset import min_max_data, build_target


def get_best():
    df = min_max_data()
    # Keeping columns with the highest coefficients
    df.drop(columns=["Natural Gas Price, Wellhead",
                     "Natural Gas Price, Citygate",
                     "Natural Gas Price, Delivered to Consumers, Residential",
                     "Natural Gas Price, Delivered to Consumers, Commercial",
                     "Natural Gas Price, Delivered to Consumers, Industrial",
                     "Natural Gas Price, Electric Power Sector",
                     "Average Retail Price of Electricity, Residential",
                     "Average Retail Price of Electricity, Commercial",
                     "Average Retail Price of Electricity, Industrial",
                     "Average Retail Price of Electricity, Transportation",
                     "Average Retail Price of Electricity, Total",
                     "Leaded Regular Gasoline, U.S. City Average Retail Price",
                     "Unleaded Regular Gasoline, U.S. City Average Retail Price",
                     "Unleaded Premium Gasoline, U.S. City Average Retail Price",
                     "All Grades of Gasoline, U.S. City Average Retail Price",
                     "Regular Motor Gasoline, Conventional Gasoline Areas, Retail Price",
                     "Regular Motor Gasoline, Reformulated Gasoline Areas, Retail Price",
                     "Regular Motor Gasoline, All Areas, Retail Price",
                     "Homes Average Sales Price",
                     "Apples",
                     "Bananas",
                     "Beef_Ground_Chuck",
                     "Beef_Round_Roast",
                     "Beef_Steak_Round",
                     "Bread_French",
                     "Bread_Whole_Wheat",
                     "Cheese_Cheddar",
                     "Chicken_Legs",
                     "Chicken_Whole",
                     "Cookies",
                     "Eggs",
                     "Flour",
                     "Frankfurters",
                     "Grapes_Seedless",
                     "IceCream",
                     "Lemons",
                     "Lettuce_Iceberg",
                     "Peaches",
                     "Pears",
                     "Peppers_Sweet",
                     "Pork_Chops",
                     "Tomatoes",
                     ],
            inplace=True)
    return df


def complete_df():
    x = get_best()
    y = build_target()
    df = x
    df = df.join(y)
    target = df.pop('USREC')
    df.insert(0, 'USREC', target)
    # Fill remaining NaN using interpolation
    df.interpolate(method='time',
                   inplace=True,
                   axis=0,
                   limit_direction='both')
    return df
