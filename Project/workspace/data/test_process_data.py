from process_data import load_data
from process_data import clean_data

def test_load_data():
    assert(load_data('disaster_messages.csv', 'disaster_categories.csv').shape == (26386, 5))


def test_clean_data():
    df1 = load_data('disaster_messages.csv', 'disaster_categories.csv')
    df2 = clean_data(df1)

    assert (df2.shape == (26216, 40))
