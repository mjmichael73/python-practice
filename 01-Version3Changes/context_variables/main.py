import contextvars

number = contextvars.ContextVar("number", default="-1")
contexts = list()

def print_number():
    print(f"number: {number.get()}")


if __name__ == "__main__":
    print_number() # number: -1
    for n in [1, 2, 3]:
        ctx = contextvars.copy_context()
        ctx.run(number.set, n)
        contexts.append(ctx)
    
    for ctx in reversed(contexts):
        ctx.run(print_number)

