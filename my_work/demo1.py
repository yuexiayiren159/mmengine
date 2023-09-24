def foo(var: int) -> float:
    return float(var)


# a: str = foo('2.0')
# b: int = foo('3.0')  # type: ignore
c: float = foo(3)
