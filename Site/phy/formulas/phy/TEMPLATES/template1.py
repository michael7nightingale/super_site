from ..COUNTER import formula_constructor
from .history import *
from ..DATAMANAGER import jsonGetParams
from django.utils.datastructures import MultiValueDictKeyError


# блок переменных
history = []
literals: dict

# составления словаря контекста
def template1(request, linedb):
    global history
    print('ZZZZZZ вызов template 1 ZZZZZZZZZZZZ ')
    args = ('x', 'y', 'z')
    formula_params_xyz, names = jsonGetParams.get_params(linedb.name, args)
    x_name, y_name, z_name = names
    # print(formula_params_xyz)
    # если есть константы в формуле, то формируем их данные
    constants = formula_params_xyz['constants'] if "constants" in formula_params_xyz else []
    try:
        # print('123')
        match request.POST['find_mark']:
            case 'x':
                result = formula_constructor.template1(params=formula_params_xyz, num1=request.POST[y_name],
                                                       num2=request.POST[z_name],
                                                       ed1=request.POST[f"{y_name}_si"],
                                                       ed2=request.POST[f"{z_name}_si"],
                                                       find_mark='x', nums_comma=request.POST["nums_comma"],
                                                       degree1=formula_params_xyz['y']['degree'],
                                                       degree2=formula_params_xyz['z']['degree'],
                                                       lined_type=formula_params_xyz['type'])
            case 'y':
                result = formula_constructor.template1(params=formula_params_xyz, num1=request.POST[x_name],
                                                       num2=request.POST[z_name],
                                                       ed1=request.POST[f"{x_name}_si"],
                                                       ed2=request.POST[f"{z_name}_si"],
                                                       find_mark='y', nums_comma=request.POST["nums_comma"],
                                                       degree1=formula_params_xyz['x']['degree'],
                                                       degree2=formula_params_xyz['z']['degree'],
                                                       lined_type=formula_params_xyz['type'])
            case 'z':
                result = formula_constructor.template1(params=formula_params_xyz, num1=request.POST[x_name],
                                                       num2=request.POST[y_name],
                                                       ed1=request.POST[f"{x_name}_si"],
                                                       ed2=request.POST[f"{y_name}_si"],
                                                       find_mark='z', nums_comma=request.POST["nums_comma"],
                                                       degree1=formula_params_xyz['x']['degree'],
                                                       degree2=formula_params_xyz['y']['degree'],
                                                       lined_type=formula_params_xyz['type'])
            case 'unknown':
                result = "Ошибка входных данных"
        if result != "Ошибка входных данных":
            history = form_history(result, formula_params_xyz[request.POST['find_mark']]['INFO']['literal'], history)
        # constants = {x: y['value'] for x, y in constants} if constants is not None else None
        constants = formula_params_xyz['constants'] if 'constants' in formula_params_xyz else None
        context = {'history': history, "params": formula_params_xyz, 'db': linedb,
                   f"result_{request.POST['find_mark']}": result, "constants": constants}
    except MultiValueDictKeyError:
        context = {'db': linedb,
                   "params": formula_params_xyz, "result_x": 0, "constants": constants}
    return context


def template2(request, linedb):
    global history
    args = ('x', 'y', 'z', 'w')
    formula_params_xyzw, names_for_request = jsonGetParams.get_params(name=linedb.name, args=args)

    x_name, y_name, z_name, w_name = names_for_request
    constants = formula_params_xyzw['constants'] if 'constants' in formula_params_xyzw else []
    nums_comma = request.POST['nums_comma']
    lined_type = formula_params_xyzw['type']
    degreex, degreey, degreez, degreew = formula_params_xyzw["x"]["degree"], formula_params_xyzw["y"]["degree"], formula_params_xyzw["z"]["degree"], formula_params_xyzw["w"]["degree"],
    try:
        find_mark = request.POST['find_mark']
        match find_mark:
            case "x":
                # 123 = yzw
                result = formula_constructor.template2(params=formula_params_xyzw, num1=request.POST[y_name], num2=request.POST[z_name], num3=request.POST[w_name],
                                                       ed1=request.POST[f'{y_name}_si'], ed2=request.POST[f'{z_name}_si'], ed3=request.POST[f'{w_name}_si'],
                                                       degree1=degreey, degree2=degreez, degree3=degreew, degree_find=degreex,
                                                       nums_comma=nums_comma, lined_type=type, find_mark=find_mark)
            case "y":
                # 123 = xzw
                result = formula_constructor.template2(params=formula_params_xyzw, num1=request.POST[x_name], num2=request.POST[z_name], num3=request.POST[w_name],
                                                       ed1=request.POST[f'{x_name}_si'], ed2=request.POST[f'{z_name}_si'], ed3=request.POST[f'{w_name}_si'],
                                                       degree1=degreex, degree2=degreez, degree3=degreew, degree_find=degreey,
                                                       nums_comma=nums_comma, lined_type=type, find_mark=find_mark)
            case "z":
                # 123 = xyw
                result = formula_constructor.template2(params=formula_params_xyzw, num1=request.POST[x_name], num2=request.POST[y_name], num3=request.POST[w_name],
                                                       ed1=request.POST[f'{x_name}_si'], ed2=request.POST[f'{y_name}_si'], ed3=request.POST[f'{w_name}_si'],
                                                       degree1=degreex, degree2=degreey, degree3=degreew, degree_find=degreez,
                                                       nums_comma=nums_comma, lined_type=type, find_mark=find_mark)
            case "w":
                # 123 = xyz
                result = formula_constructor.template2(params=formula_params_xyzw, num1=request.POST[x_name], num2=request.POST[y_name], num3=request.POST[z_name],
                                                       ed1=request.POST[f'{x_name}_si'], ed2=request.POST[f'{y_name}_si'], ed3=request.POST[f'{z_name}_si'],
                                                       degree1=degreex, degree2=degreey, degree3=degreez, degree_find=degreew,
                                                       nums_comma=nums_comma, lined_type=type, find_mark=find_mark)
            case _:
                result = "Ошибка входных данных"
        # forming history if success
        if result != 'Ошибка входных данных':
            form_history(result, formula_params_xyzw[find_mark]['INFO']['literal'], history)
        # forming context after all

        context = {'params': formula_params_xyzw, f"result_{find_mark}": result,
                   'history': history, "constants": constants, "db": linedb}
    except MultiValueDictKeyError:
        context = {'params': formula_params_xyzw, "db": linedb,
                   'constants': constants}
    return context

