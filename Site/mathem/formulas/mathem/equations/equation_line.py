import sympy as sp
from sympy.abc import *



def equation(ex: str, root: str, nums_comma: int) -> list[dict]:
    global result
    try:
        expr = sp.sympify(ex.replace('=', '-').replace('^', '**'))
        _x = sp.Symbol(root)
        result = sp.solve(expr, _x, dict=True)
        nums_comma = int(nums_comma)
        result = [dict(zip(i.keys(), [round(int(el), nums_comma) for el in i.values()])) for i in result]
    except EnvironmentError:
        result = [{'Результат': "Ошибка в написании уравнения!"}]
    return result


def unequation(ex: str, root: str, nums_comma: str) -> list[dict]:
    nums_comma = int(nums_comma)
    try:
        expression = ex.replace("^", '**')
        _x = sp.Symbol(root)
        result = sp.solve(expression, _x)

    except EnvironmentError:
        result = [{'Результат': "Ошибка в написании уравнения!"}]
    return result
