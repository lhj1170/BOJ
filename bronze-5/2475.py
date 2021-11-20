class Solve:
    @classmethod
    def run(cls):
        split_inputs = cls._get_inputs()
        solve_num = 0
        for input in split_inputs:
            solve_num += (int(input) ** 2)
        print(solve_num % 10)

    @classmethod
    def _get_inputs(cls):
        input_tmp = input()
        split_input = input_tmp.split(' ')
        return split_input


if __name__ == '__main__':
    Solve.run()
