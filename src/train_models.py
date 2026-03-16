from catboost import CatBoostRegressor


def train_catboost(X_train, y_train):

    model = CatBoostRegressor(
        iterations=300,
        depth=6,
        learning_rate=0.05,
        verbose=False
    )

    model.fit(X_train, y_train)

    return model
