def cal(var_a: int, var_b: int, sym: str) -> int:
    symbols_char = set(["+", "-", "/", "%", "*"])
    if sym not in symbols_char:
        return None
    if sym == "+":
        return var_a + var_b
    if sym == "-":
        return var_a - var_b
    if sym == "/":
        return var_a / var_b
    if sym == "%":
        return var_a % var_b
    if sym == "*":
        return var_a * var_b


def main():
    expression = input("give a expression: ").strip().split()
    var_a, sym, var_b = int(expression[0]), expression[1], int(expression[2])
    res = cal(var_a, var_b, sym)
    print(res)


if __name__ == "__main__":
    main()
