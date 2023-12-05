values = {} # name: value
nodes = {} # name: (leftName, operation, rightName)


with open("21.txt", "r") as file:


    for l in file:
        name, shout = l.strip().split(": ")
        if " " in shout:
            nodes[name] = shout.split(" ")
        else:
            values[name] = int(shout)


def get_value(name):
    val_res = values.get(name)
    if val_res is not None:
        return val_res
    else:
        left, op, right = nodes[name]
        return eval(str(get_value(left))+op+str(get_value(right)))


# print(get_value("root"))

def contains_me(name):
    if name == "humn":
        return True
    if values.get(name) is not None:
        return False
    left, _, right = nodes[name]
    return contains_me(left) or contains_me(right)

opps = {"+": "-",
        "-": "+",
        "/": "*",
        "*": "/"}

def make_equal(name, value):
    if name == "humn":
        print(value)
        return value
    left, op, right = nodes[name]
    if contains_me(left):
        new_value = eval(str(value) + opps[op] + str(get_value(right)))
        return make_equal(left, new_value)
    elif contains_me(right):
        #new_value = eval(str(value) + opps[op] + str(get_value(left)))
        left_value = get_value(left)
        if op in "+*":
            new_value = eval(str(value) + opps[op] + str(left_value))
        else:
            new_value = eval(str(left_value) + op + str(value))

        return make_equal(right, new_value)


root_left, _ , root_right = nodes["root"]


if contains_me(root_left):
    val = make_equal(root_left, get_value(root_right))
else:
    val = make_equal(root_right, get_value(root_left))

values["humn"] = val
