import pandas as pd

def analyze_data(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing": int(df.isnull().sum().sum()),
        "duplicates": int(df.duplicated().sum())
    }

def structure_dataset(df):
    structured = df.copy()

    structured.columns = (
        structured.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    structured.dropna(how="all", inplace=True)
    structured.dropna(axis=1, how="all", inplace=True)
    structured.drop_duplicates(inplace=True)

    for col in structured.columns:
        try:
            structured[col] = pd.to_numeric(structured[col])
        except:
            pass

    for col in structured.select_dtypes(include="number"):
        structured[col].fillna(structured[col].median(), inplace=True)

    for col in structured.select_dtypes(include="object"):
        structured[col].fillna("Unknown", inplace=True)

    return structured
