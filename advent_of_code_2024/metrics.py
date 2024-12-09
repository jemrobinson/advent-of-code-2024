import pandas as pd


def distance(series_a: "pd.Series[int]", series_b: "pd.Series[int]") -> int:
    series_a = series_a.sort_values().reset_index(drop=True)
    series_b = series_b.sort_values().reset_index(drop=True)
    return sum(abs(series_a - series_b))


def distance_df(df: pd.DataFrame) -> int:
    loc_ids_0 = df.iloc[:, 0]
    loc_ids_1 = df.iloc[:, 1]
    return distance(loc_ids_0, loc_ids_1)


def similarity(series_a: "pd.Series[int]", series_b: "pd.Series[int]") -> int:
    series_b_counts = series_b.value_counts()
    total = 0
    for item in series_a:
        try:
            total += series_b_counts.loc[item] * item
        except KeyError:
            pass
    return total


def similarity_df(df: pd.DataFrame) -> int:
    loc_ids_0 = df.iloc[:, 0]
    loc_ids_1 = df.iloc[:, 1]
    return similarity(loc_ids_0, loc_ids_1)
