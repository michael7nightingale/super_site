import json
# открытие бд с формулами
with open(r"D:\Progs\PycharmProjects\super_site\Site\phy\formulas\phy\DATA\params.json") as datafile:
    data = json.load(datafile)

# блок переменных-словарей
formulas = data['formulas']
literals = data['literals']
constants = data['constants']


# получить данные о формуле из json по слагу формулы
def get_params(name: str) -> tuple[dict, list]:
    # print('#W$%#$%#$% вызов jsonGetParams 34$%W$%W$% ')
    if name in formulas:
        # получаем общие данные имен и тип формулы
        params_common = formulas[name]
        # lined_type = formulas[name]["type"]
        # получаем данные по аргументам
        names_for_request = []
        args = [i for i in params_common.keys() if len(i) == 1]
        # params = data['formulas'][name]
        params = dict(zip(args, (dict() for _ in args)))
        # print(args)
        # params = params_common
        # print('params = ', params)
        for arg in args:
            # print(arg)
            # print(data['formulas'][name][arg]['INFO'])
            if params_common[arg]['INFO'] in literals:
                # print(literals[params_common[arg]['INFO']])
                # print(params[arg]['INFO'])
                params[arg]['INFO'] = literals[params_common[arg]["INFO"]]
                params[arg]['degree'] = params_common[arg]['degree']
                names_for_request.append(params[arg]['INFO']['name'])
            elif params_common[arg]['INFO'] in constants:
                params[arg]['degree'] = params_common[arg]['degree']
                params[arg]['INFO'] = constants[params_common[arg]["INFO"]]
                names_for_request.append(params[arg]['INFO']['name'])
        # print(names_for_request)
        # params = dict(zip(args, args_data))
        # print(params)
        # print(params_common)
        if "constants" in params_common:
            params["constants"] = params_common['constants']
        else:
            pass
        params["type"] = formulas[name]["type"]
        return params, names_for_request
    else:
        return "Ошибка имени!"


def get_constants(params: dict) -> list:
    return params['constants'] if "constants" in params else []


