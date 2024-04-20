def my_var():
    var_list = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]
    for item in var_list:
        print(f"{item} est de type {type(item)}")


if __name__ == "__main__":
    my_var()
