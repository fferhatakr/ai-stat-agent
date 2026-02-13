def simple_analysis(df):
    results = {}

    results["stroke_rate"] = df["stroke"].mean()

    glucose_means = df.groupby("stroke")["avg_glucose_level"].mean()
    results["glucose_means"] = glucose_means.to_dict()

    bmi_means = df.groupby("stroke")["bmi"].mean()
    results["bmi_means"] = bmi_means.to_dict()

    hypertension_stroke = df.groupby("hypertension")["stroke"].mean()
    results["hypertension_stroke_rate"] = hypertension_stroke.to_dict()

    heart_stroke = df.groupby("heart_disease")["stroke"].mean()
    results["heart_disease_stroke_rate"] = heart_stroke.to_dict()

    return results
