import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def train_and_test_knn_classifier(train_data, k, test_data):
    X_train, y_train = zip(*train_data)
    X_train = np.array(X_train).reshape(-1, 1)
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    X_test, y_test = zip(*test_data)
    X_test = np.array(X_test).reshape(-1, 1)
    y_pred = knn_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
  
def read_pairs(num_pairs):
    pairs = []
    for _ in range(num_pairs):
        x = float(input("Enter x: "))
        y = int(input("Enter y: "))
        pairs.append((x, y))
    return pairs

# Main program
def main():
  N = int(input("Enter (N): "))
  train_data = read_pairs(N)
  
  M = int(input("Enter (M): "))
  test_data = read_pairs(M)
  
  best_k = 0
  best_accuracy = 0
  
  for k in range(10):
      accuracy = train_and_test_knn_classifier(train_data, k+1, test_data)  
      if accuracy >= best_accuracy:
          best_k = k
          best_accuracy = accuracy
  
  print(f"The best k is {best_k}")
  print(f"The best accuracy is {best_accuracy}")

if __name__ == "__main__":
    main()
