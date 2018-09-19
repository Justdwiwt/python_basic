# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris = load_iris()
print(iris.DESCR)

iris_data = iris.data
feature_names = iris.feature_names
iris_target = iris.target
