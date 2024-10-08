# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y5oUHFZM6TtrkgHfqrZB5JTCW04u_lrN
"""

import pandas as pd

data = pd.read_csv('diabetes.csv')

x = data.drop(columns = ["Outcome"])

y = data["Outcome"]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test, = train_test_split(x,y, test_size = .2)



import tensorflow as tf

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(256, input_shape = (8,), activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  # For binary classification

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs = 1000)

model.evaluate(x_test, y_test)