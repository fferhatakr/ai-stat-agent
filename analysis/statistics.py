import pandas as pd

def load_data(path):
    return pd.read_excel(path)

def analyze_data(df):
    analysis = {}
    analysis["shape"] = df.shape
    analysis["missing"] = df.isnull().sum().to_dict()
    analysis["stroke_dist"] = df["stroke"].value_counts().to_dict()
    analysis["correlations"] = (
        df.corr(numeric_only=True)["stroke"]
        .sort_values(ascending=False)
        .to_dict()
    )
    return analysis
