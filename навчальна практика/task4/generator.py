def generator(a=0, b=1, step=1):
    minimum = min(a, b)
    maximum = max(a, b)
    if step > 0:
        yield minimum
        while minimum < maximum:
            minimum += step
            if minimum > maximum:
                return
            yield minimum
    else:
        yield maximum
        while minimum < maximum:
            maximum += step
            if minimum > maximum:
                return
            yield maximum
