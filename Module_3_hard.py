def the_total_amount(var):
    total = 0
    if isinstance(var, int):
        return var
    elif isinstance(var, str):
        return len(var)
    elif isinstance(var, dict):
        var = list(var.items())
    for i in var:
        total += the_total_amount(i)
    return total

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = the_total_amount(data_structure)
print(result)