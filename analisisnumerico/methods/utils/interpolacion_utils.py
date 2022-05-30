def is_valid(X):
    for x in X:
        if X.count(x) >= 2:
            return False
    return True