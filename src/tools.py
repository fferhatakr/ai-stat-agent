import pandas as pd


def load_data(path):
    try:
        df = pd.read_excel(path, engine="openpyxl")
        return df
    except Exception as e:
        raise Exception(f"Excel yüklenirken hata oluştu: {e}")


def basic_analysis(df):
    try:
        result = {
            "columns": list(df.columns),
            "shape": df.shape,
            "missing_values": df.isnull().sum().to_dict(),
            "summary": df.describe(include="all").to_string()
        }
        return result
    except Exception as e:
        raise Exception(f"Temel analiz sırasında hata oluştu: {e}")


def correlation_analysis(df):
    try:
        corr = df.corr(numeric_only=True)
        return corr.to_string()
    except Exception as e:
        raise Exception(f"Korelasyon analizi sırasında hata oluştu: {e}")


def detect_outliers(df):
    try:
        numeric_df = df.select_dtypes(include="number")
        outliers = {}

        for col in numeric_df.columns:
            q1 = numeric_df[col].quantile(0.25)
            q3 = numeric_df[col].quantile(0.75)
            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            count = numeric_df[(numeric_df[col] < lower) | (numeric_df[col] > upper)]
            outliers[col] = len(count)

        return outliers
    except Exception as e:
        raise Exception(f"Aykırı değer analizi sırasında hata oluştu: {e}")
