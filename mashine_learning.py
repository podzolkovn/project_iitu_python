import numpy as np
import pandas
from sklearn import linear_model
from math import ceil

almaty = pandas.read_csv('date/prediction_almaty.csv')
aktau = pandas.read_csv('date/prediction_aktau.csv')
astana = pandas.read_csv('date/prediction_astana.csv')
shymkent = pandas.read_csv('date/prediction_shymkent.csv')


price_almaty = np.array(almaty.price).reshape(-1, 1)
date_almaty = np.array(almaty.date).reshape(-1, 1)
reg_almaty = linear_model.LinearRegression()
reg_almaty.fit(date_almaty, price_almaty)

price_aktau = np.array(aktau.price).reshape(-1, 1)
date_aktau = np.array(aktau.date).reshape(-1, 1)
reg_aktau = linear_model.LinearRegression()
reg_aktau.fit(date_aktau, price_aktau)

price_astana = np.array(astana.price).reshape(-1, 1)
date_astana = np.array(astana.date).reshape(-1, 1)
reg_astana = linear_model.LinearRegression()
reg_astana.fit(date_astana, price_astana)

price_shymkent = np.array(shymkent.price).reshape(-1, 1)
date_shymkent = np.array(shymkent.date).reshape(-1, 1)
reg_shymkent = linear_model.LinearRegression()
reg_shymkent.fit(date_shymkent, price_shymkent)

alm_pred = reg_almaty.predict([[2024], [2025], [2026], [2027], [2028], [2029], [2030]])
ast_pred = reg_astana.predict([[2024], [2025], [2026], [2027], [2028], [2029], [2030]])
akt_pred = reg_aktau.predict([[2024], [2025], [2026], [2027], [2028], [2029], [2030]])
shm_pred = reg_shymkent.predict([[2024], [2025], [2026], [2027], [2028], [2029], [2030]])

alm = []
ast = []
akt = []
shm = []

for i in range(len(alm_pred)):
    for j in range(len(alm_pred[i])):
        alm.append(ceil(alm_pred[i][j]))

for i in range(len(ast_pred)):
    for j in range(len(ast_pred[i])):
        ast.append(ceil(ast_pred[i][j]))

for i in range(len(akt_pred)):
    for j in range(len(akt_pred[i])):
        akt.append(ceil(akt_pred[i][j]))

for i in range(len(shm_pred)):
    for j in range(len(shm_pred[i])):
        shm.append(ceil(shm_pred[i][j]))

print(alm)
print(ast)
print(akt)
print(shm)

