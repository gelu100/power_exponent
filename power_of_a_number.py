def returning_power_base_of_a_number(pow, exp):
    if isinstance(exp,float):
        raise TypeError
    if isinstance(pow, str):
        raise TypeError
    elif exp == 0:
        return 1
    elif isinstance(exp, str):
        raise TypeError
    elif pow == 0 and exp < 0:
        raise ZeroDivisionError
    elif pow!=0 and exp <0:
        result = 1
        while exp <0:
            result *=pow
            exp +=1
        new_result = 1/result
        return new_result
    else:
        results = 1
        for n in range(exp):
            results *= pow
        return results
