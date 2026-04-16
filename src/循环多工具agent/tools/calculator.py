def calculator(expression: str):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"计算错误: {e}"