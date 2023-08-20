import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def main():
    N = int(input("Enter N: "))
    k = int(input("Enter k"))
    
    if k > N:
        print("Error: k <= N")
        return
    
    data = []
    for _ in range(N):
        x = float(input("Enter x"))
        y = float(input("Enter y"))
        data.append((x, y))
    
    X_train = np.array([point[0] for point in data]).reshape(-1, 1)
    y_train = np.array([point[1] for point in data])
    X_pred = float(input("Enter X for new prediction: "))
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, y_train)
    y_pred = knn_regressor.predict([[X_pred]])
    
    r_squared = r2_score(y_train, knn_regressor.predict(X_train))
    
    print(f"Predictions: {y_pred[0]}")
    print(f"r2 score: {r_squared}")

if __name__ == "__main__":
    main()
