from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess(df):

    X = df[[
        "spindle_speed",
        "feed_rate",
        "depth_of_cut"
    ]]

    y = df[[
        "cutting_force",
        "surface_roughness",
        "tool_wear_rate",
        "temperature",
        "chip_load_deviation",
        "power"
    ]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, scaler
