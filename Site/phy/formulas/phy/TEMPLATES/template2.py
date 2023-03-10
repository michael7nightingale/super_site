from ..DATAMANAGER import jsonGetParams
from ..COUNTER import formula_constructor
from .history import *
from django.utils.datastructures import MultiValueDictKeyError


def template2(request, linedb):
    global history
    args = ('x', 'y', 'z', 'w')
    formula_params_xyzw, names_for_request = jsonGetParams.get_params(name=linedb.name, args=args)
    x_name, y_name, z_name, w_name = names_for_request
    constants = formula_params_xyzw['constants'] if 'constants' in formula_params_xyzw else None
    try:
        match request.POST['find_mark']:
            case "x":
                result = formula_constructor.template2()
            case "y":
                result = formula_constructor.template2()
            case "z":
                result = formula_constructor.template2()
            case "w":
                result = formula_constructor.template2()




    except MultiValueDictKeyError:
        context = {'params': formula_params_xyzw, "db": linedb,
                   'constants': constants}

