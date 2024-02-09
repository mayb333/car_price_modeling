from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

def calculate_metrics(y_pred, y_true):
    print(f"MSE:  {round(mean_squared_error(y_pred=y_pred, y_true=y_true))}")
    print(f"RMSE: {round(root_mean_squared_error(y_pred=y_pred, y_true=y_true))}")
    print(f"MAE:  {round(mean_absolute_error(y_pred=y_pred, y_true=y_true))}")
    print(f"R^2   {round(r2_score(y_pred=y_pred, y_true=y_true), 2)}")
    print("-" * 80)