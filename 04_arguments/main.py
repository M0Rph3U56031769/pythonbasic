class Arguments:

    @staticmethod
    def concatenate(**kwargs):
        result = ""
        # Iterating over the Python kwargs dictionary
        for arg in kwargs.values():
            result += arg
        return result

    @staticmethod
    def my_sum(*args, extra: int = 0):
        result = 0
        print(extra)
        # Iterating over the Python args tuple
        for x in args:
            result += x
        return result


if __name__ == "__main__":
    print(Arguments.my_sum(1, 2, 3))
    print(Arguments.concatenate(a="The", b="Python", c="Is", d="Great", e="!"))
