import numpy as np
import pandas
from sklearn import linear_model
from math import ceil


def predictions_line_regression():
    date = [[2024], [2025], [2026], [2027], [2028], [2029], [2030]]

    almaty = pandas.read_csv('date/prediction_almaty.csv')
    astana = pandas.read_csv('date/prediction_astana.csv')
    shymkent = pandas.read_csv('date/prediction_shymkent.csv')

    price_almaty = np.array(almaty.price).reshape(-1, 1)
    date_almaty = np.array(almaty.date).reshape(-1, 1)
    reg_almaty = linear_model.LinearRegression()
    reg_almaty.fit(date_almaty, price_almaty)

    price_astana = np.array(astana.price).reshape(-1, 1)
    date_astana = np.array(astana.date).reshape(-1, 1)
    reg_astana = linear_model.LinearRegression()
    reg_astana.fit(date_astana, price_astana)

    price_shymkent = np.array(shymkent.price).reshape(-1, 1)
    date_shymkent = np.array(shymkent.date).reshape(-1, 1)
    reg_shymkent = linear_model.LinearRegression()
    reg_shymkent.fit(date_shymkent, price_shymkent)

    alm_pred = reg_almaty.predict(date)
    ast_pred = reg_astana.predict(date)
    shm_pred = reg_shymkent.predict(date)

    alm = []
    ast = []
    shm = []

    for i in range(len(alm_pred)):
        for j in range(len(alm_pred[i])):
            alm.append(ceil(alm_pred[i][j]))

    for i in range(len(ast_pred)):
        for j in range(len(ast_pred[i])):
            ast.append(ceil(ast_pred[i][j]))

    for i in range(len(shm_pred)):
        for j in range(len(shm_pred[i])):
            shm.append(ceil(shm_pred[i][j]))

    date_res = [2024, 2025, 2026, 2027, 2028, 2029, 2030]

    alm_res = 'Almaty: \n'
    for j in range(len(alm)):
        mid = f'{" ":<7}{date_res[j]} : {alm[j]} тг/м² \n'
        alm_res += mid

    ast_res = 'Astana: \n'
    for j in range(len(ast)):
        mid = f'{" ":<7}{date_res[j]} : {ast[j]} тг/м² \n'
        ast_res += mid

    shm_res = 'Shymkent: \n'
    for j in range(len(shm)):
        mid = f'{" ":<7}{date_res[j]} : {shm[j]} тг/м² \n'
        shm_res += mid

    return (f'{alm_res}'
            f'{ast_res}'
            f'{shm_res}')
