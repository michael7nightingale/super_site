def check_template_data(func):
    """Проверка дынных запроса"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RecursionError:
            return "Ошибка выходных данных"
    return wrapper


# x = y*z, x = y/z -> y = x*z
@check_template_data
def template1(params: dict, nums_comma: str, find_mark: str, num1: str, num2: str, ed1: str, ed2: str,
              degree1: str, degree2: str, lined_type) -> int | str:
    # print('1123 123 прием до меня дошло')
    # print('_____ вызов formula_constructor ___')

    num1, num2, nums_comma, degree1, degree2, degree_find =\
    float(num1), float(num2), int(nums_comma), float(degree1), float(degree2), float(params[find_mark]['degree'])
    # print(123, params['y']['degree'])
    # print(degree1, degree2)
    match find_mark:
        case 'x':
            if lined_type == "line_xyz":
                    # print(eval(params['y']['INFO']['si'][ed1]))
                result = (((num1 * eval(params['y']['INFO']['si'][ed1]))**degree1) *
                        ((num2 * eval(params['z']['INFO']['si'][ed2]))**degree2))**(1/degree_find)

                    # response = "$${" + f"{params[find_mark]['literal']}"+"} = {"+f"{num1} {ed1} * {num2} {ed2}" + '} = {' + f"{result}" +'}$$'
            elif lined_type == 'divide_xyz':
                result = (((num1 * eval(params['y']['INFO']['si'][ed1])) ** degree1) /
                        ((num2 * eval(params['z']['INFO']['si'][ed2])) ** degree2))**(1/degree_find)
        case 'y':
            if lined_type == "line_xyz":
                result = (((num1 * eval(params['x']['INFO']['si'][ed1])) ** degree1) /
                        ((num2 * eval(params['z']['INFO']['si'][ed2])) ** degree2))**(1/degree_find)
            elif lined_type == 'divide_xyz':
                result = (((num1 * eval(params['x']['INFO']['si'][ed1])) ** degree1) *
                        ((num2 * eval(params['z']['INFO']['si'][ed2])) ** degree2))**(1/degree_find)
        case 'z':
            if lined_type == "line_xyz":
                result = (((num1 * eval(params['x']['INFO']['si'][ed1])) ** degree1) /
                        ((num2 * eval(params['y']['INFO']['si'][ed2])) ** degree2))**(1/degree_find)
            elif lined_type == 'divide_xyz':
                result = (((num1 * eval(params['x']['INFO']['si'][ed1])) ** degree1) /
                        ((num2 * eval(params['y']['INFO']['si'][ed2])) ** degree2))**(1/degree_find)
        case _: raise AssertionError('unsupported find_mark for x = y*x')
    return round(result, nums_comma)


@check_template_data
def template2(params: dict, num1, num2, num3, ed1, ed2, ed3, degree1, degree2, degree3, degree_find, find_mark, nums_comma, lined_type) -> int | str:
    num1, num2, num3, nums_comma = float(num1), float(num2), float(num3), int(nums_comma)
    degree1, degree2, degree3, degree_find = float(degree1), float(degree2), float(degree3), float(params[find_mark]['degree'])
    match find_mark:
        case "x":
            ed1, ed2, ed3 = params['y']['INFO']['si'][ed1], params['z']['INFO']['si'][ed2], params['w']['INFO']['si'][ed3]
            match lined_type:
                case "line":
                    result = (
                              ((num1 * eval(ed1))**degree1) *
                              ((num2 * eval(ed2))**degree2) *
                              ((num3 * eval(ed3))**degree3)
                            ) ** (1/degree_find)
        case "y":
            ed1, ed2, ed3 = params['x']['INFO']['si'][ed1], params['z']["INFO"]['si'][ed2], params["w"]["INFO"]["si"][ed3]
            match lined_type:
                case "line":
                    result = (
                        ((num1 * eval(ed1)) ** degree1) /
                            (
                                ((num2 * eval(ed2)) ** degree2) *
                                ((num3 * eval(ed3)) ** degree3)
                            )
                    ) ** (1/degree_find)
        case "z":
            ed1, ed2, ed3 = params['x']['INFO']['si'][ed1], params['y']["INFO"]['si'][ed2], params["w"]["INFO"]["si"][
                ed3]
            match lined_type:
                case "line":
                    result = (
                                     ((num1 * eval(ed1)) ** degree1) /
                                     (
                                             ((num2 * eval(ed2)) ** degree2) *
                                             ((num3 * eval(ed3)) ** degree3)
                                     )
                             ) ** (1 / degree_find)
        case "w":
            ed1, ed2, ed3 = params['x']['INFO']['si'][ed1], params['y']["INFO"]['si'][ed2], params["z"]["INFO"]["si"][
                ed3]
            match lined_type:
                case "line":
                    result = (
                                     ((num1 * eval(ed1)) ** degree1) /
                                     (
                                             ((num2 * eval(ed2)) ** degree2) *
                                             ((num3 * eval(ed3)) ** degree3)
                                     )
                             ) ** (1 / degree_find)
    return round(result, nums_comma)



