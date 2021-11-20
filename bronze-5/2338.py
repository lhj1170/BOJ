class Solve:
    @classmethod
    def run(cls):
        a, b = cls._get_inputs()
        print(a + b)
        print(a - b)
        print(a * b)

    @classmethod
    def _get_inputs(cls):
        input_a = int(input())
        input_b = int(input())
        return input_a, input_b


if __name__ == '__main__':
    Solve.run()
