def foo(uppercase = False) -> str:
    if uppercase:  # pragma: no cover
        return "FOO"
    return "foo"