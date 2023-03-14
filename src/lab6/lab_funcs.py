import sklearn
import sklearn.datasets
import sklearn.model_selection
import sklearn.neighbors

lfw_pairs_dataset = sklearn.datasets.fetch_lfw_pairs()
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    lfw_pairs_dataset.data, lfw_pairs_dataset.target)

def train(k: int) -> tuple[float, float]:
    knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    
    return knn.score(x_test, y_test), knn.score(x_train, y_train)
