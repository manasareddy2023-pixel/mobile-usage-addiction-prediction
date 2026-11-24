
# Selected features used by the final ML model

BEST_FEATURES = [
    'Daily_Usage_Hours',
    'Sleep_Hours',
    'Intellectual_Performance',
    'Apps_Used_Daily',
    'Phone_Checks_Per_Day',
    'Time_on_Social_Media',
    'Gaming_Usage_Ratio',
    'Social_Media_Usage_Ratio',
    'Non_Educational_Usage_Hours',
    'Education_Usage_Ratio'
]


def select_features(data):
    """
    Select the required 10 features
    in the same order used during training.
    """
    missing_features = [
        feature for feature in BEST_FEATURES
        if feature not in data.columns
    ]

    if missing_features:
        raise ValueError(
            f"Missing features: {missing_features}"
        )

    return data[BEST_FEATURES].copy()
