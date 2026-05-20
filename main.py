from dataloader import load_data
from GridSearch import GridSearch
if __name__ == "__main__":
    X, Y = load_data(file_path="bienetre.csv", target_col="target")
    print("Data loaded successfully")
    print("-"*20)
    k_values = [1, 3, 5, 7]
    grid_search = GridSearch(k_values)
    best_k, best_score = grid_search.fit_best_k(X_train=X[:80], y_train=Y[:80], X_test=X[80:], y_test=Y[80:])
    print(f"Best k: {best_k} with an accuracy of {best_score*100}%")