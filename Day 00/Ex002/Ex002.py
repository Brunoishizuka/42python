# var.py

def my_var():
    var_int = 42
    var_str_int = "42"
    var_str = "Quarenta-e-Dois"
    var_float = 42.0
    var_bool = True
    var_list = [42]
    var_dict = {42: 42}
    var_tuple = (42,)
    var_set = set()

    print(f"{var_int} has a type {type(var_int)}")
    print(f"{var_str_int} has a type {type(var_str_int)}")
    print(f"{var_str} has a type {type(var_str)}")
    print(f"{var_float} has a type {type(var_float)}")
    print(f"{var_bool} has a type {type(var_bool)}")
    print(f"{var_list} has a type {type(var_list)}")
    print(f"{var_dict} has a type {type(var_dict)}")
    print(f"{var_tuple} has a type {type(var_tuple)}")
    print(f"{var_set} has a type {type(var_set)}")

if __name__ == "__main__":
    my_var()
