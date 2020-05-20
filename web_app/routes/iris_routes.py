import numpy as np
from sklearn.linear_model import LogisticRegression
from flask import Blueprint, jsonify, request, render_template #, flash, redirect

iris_routes = Blueprint("iris_routes", __name__)

@iris_routes.route('/iris')
def iris():    
 
 X, y = load_iris(return_X_y=True)
 clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)

 return str(clf.predict(X[:2, :]))

if __name__ == "__main__":
    print(str(clf.predict(X[:2, :])))