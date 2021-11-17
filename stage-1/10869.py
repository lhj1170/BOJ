class Solve:
    @classmethod
    def run(cls):
        a, b = cls._get_input()
        cls._get_sum(a, b)
        cls._get_minus(a, b)
        cls._get_multiplication(a, b)
        cls._get_division(a, b)
        cls._get_remainder(a, b)

    @classmethod
    def _get_input(cls):
        data = input()
        refined = data.split(' ')
        return int(refined[0]), int(refined[1])

    @classmethod
    def _get_sum(cls, a, b):
        print(a + b)

    @classmethod
    def _get_minus(cls, a, b):
        print(a - b)

    @classmethod
    def _get_multiplication(cls, a, b):
        print(a * b)

    @classmethod
    def _get_division(cls, a, b):
        print(a // b)

    @classmethod
    def _get_remainder(cls, a, b):
        print(a % b)


if __name__ == '__main__':
    Solve.run()
