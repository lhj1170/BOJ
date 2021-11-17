class Solve:
    @classmethod
    def run(cls):
        input_a = cls._get_input()
        input_b = cls._get_input()
        cls._solve(input_a, input_b)

    @classmethod
    def _get_input(cls):
        data = input()
        return data

    @classmethod
    def _solve(cls, input_a, input_b):
        input_a = int(input_a)
        reverse_input_b = input_b[::-1]
        for idx, each_char in enumerate(reverse_input_b):
            res = input_a * int(each_char)
            print(res)
        print(input_a * int(input_b))


if __name__ == '__main__':
    Solve.run()
