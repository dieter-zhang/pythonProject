import pandas as pd


def test_pandas_series():
    """test pandas series
    ----
    pandas.Series looks like columns in Excel.
    """
    a = [1, 2, 3]
    # 1. the most easy way to create a series
    myvar = pd.Series(a)
    print(myvar)
    # 2. we can access data by using index
    for i in range(3):
        print(myvar[i])
    # 3. we can also assign index to the series
    #    in this way, series acts like a dict in python.
    a = ["Google", "Runoob", "Wiki"]
    myvar = pd.Series(a, index=['x', 'y', 'z'])
    print(myvar)


def test_pandas_dataframe():
    """ test pandas dataframe
    pandas dataframe is a table like data structure.
    each column is with different type. As the same as the
    table, dataframe has row and column indices.

    :return:
    """
    # 1. the first way to create the pandas dataframe
    data = [['Google', 10],
            ['Runoob', 12],
            ['Wiki', 13]]
    df = pd.DataFrame(data, index=['x', 'y', 'z'], columns=['Site', 'Age'])
    print(df)
    # 2. the second way to create the pandas dataframe
    data = {'Site': ['Google', 'Runoob', 'Wiki'],
            'Age': [10, 12, 13]}
    df = pd.DataFrame(data)
    print(df)
    # 3. the third way (key/value)
    data = [{'Site': 'Google', 'Age': 10}, {'Site': 'Runoob', 'Age': 12}, {'Site': 'Wiki', 'Age': 13}]
    df = pd.DataFrame(data)
    print(df)
    # ----
    # use loc to obtain row
    print('------')
    print(df.loc[0])
    print(df.loc[[0, 2]])
    print(df['Site'])


def test_pandas_csv():
    """ test pandas csv file
    ----
    the most common use of pandas is to read and write csv file.

    """
    df = pd.read_csv('nba.csv')
    #print(df)
    print(df[df['Name'] == 'Jae Crowder'].Team)

    # you can write pandas data to csv file

# if __name__ == "__main__":
# test_pandas_series()
# test_pandas_dataframe()
test_pandas_csv()
