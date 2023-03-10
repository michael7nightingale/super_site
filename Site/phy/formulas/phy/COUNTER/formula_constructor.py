# x = y*z, x = y/z -> y = x*z
def template1(params: dict, nums_comma: str, find_mark: str, num1: str, num2: str, ed1: str, ed2: str,
              degree1: str, degree2: str, lined_type) -> int | str:
    # print('1123 123 прием до меня дошло')
    # print('_____ вызов formula_constructor ___')
    try:
        num1, num2, nums_comma, degree1, degree2, degree_find =\
           float(num1), float(num2), int(nums_comma), float(degree1), float(degree2), float(params[find_mark]['degree'])
        # print(123, params['y']['degree'])
        # print(degree1, degree2)
        match find_mark:
            case 'x':
                if lined_type == "line_xyz":
                    print(degree2, degree_find, degree1)
                    # print(eval(params['y']['INFO']['si'][ed1]))
                    result = round(
                        (((num1 * eval(params['y']['INFO']['si'][ed1]))**degree1) *
                        ((num2 * eval(params['z']['INFO']['si'][ed2]))**degree2))**(1/degree_find),
                        nums_comma)
                    # response = "$${" + f"{params[find_mark]['literal']}"+"} = {"+f"{num1} {ed1} * {num2} {ed2}" + '} = {' + f"{result}" +'}$$'
                elif lined_type == 'divide_xyz':
                    result = round(
                        (((num1 * eval(params['y']['INFO']['si'][ed1])) ** degree1) /
                        ((num2 * eval(params['z']['INFO']['si'][ed2])) ** degree2))**(1/degree_find),
                        nums_comma)
            case 'y':
                if lined_type == "line_xyz":
                    print(params)
                    result = round(
                        (((num1 * eval(params['x']['INFO']['si'][ed1])) ** degree1) /
                        ((num2 * eval(params['z']['INFO']['si'][ed2])) ** degree2))**(1/degree_find),
                        nums_comma)
                elif lined_type == 'divide_xyz':
                    result = round(
                        (((num1 * eval(params['x']['INFO']['si'][ed1])) ** degree1) *
                        ((num2 * eval(params['z']['INFO']['si'][ed2])) ** degree2))**(1/degree_find),
                        nums_comma)
            case 'z':
                if lined_type == "line_xyz":
                    result = round(
                        (((num1 * eval(params['x']['INFO']['si'][ed1])) ** degree1) /
                        ((num2 * eval(params['y']['INFO']['si'][ed2])) ** degree2))**(1/degree_find),
                        nums_comma)
                elif lined_type == 'divide_xyz':
                    result = round(
                        (((num1 * eval(params['x']['INFO']['si'][ed1])) ** degree1) /
                        ((num2 * eval(params['y']['INFO']['si'][ed2])) ** degree2))**(1/degree_find),
                        nums_comma)
            case _: raise AssertionError('unsupported find_mark for x = y*x')

        return result
    # если передан другой тип данных
    # except EnvironmentError:
    except AssertionError:
        return 'Ошибка входных данных'


# составляем скрипт MathJax
def template1Сonstruсtor(params: dict, nums_comma: str, find_mark: str, num1, num2, ed1, ed2, constants) -> str:
    ...


def template2(params: dict, num1, num2, num3, ed1, ed2, ed3, degree1, degree2, degree3, find_mark, nums_comma, lined_type) -> int | str:
    num1, num2, num3, nums_comma = float(num1), float(num2), float(num3), float(nums_comma)
    degree1, degree2, degree3 = float(degree1), float(degree2), float(degree3)


