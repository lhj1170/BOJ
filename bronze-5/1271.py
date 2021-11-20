class Solve:
    @classmethod
    def run(cls):
        money, number_of_aliens = cls._get_inputs()
        shared = money // number_of_aliens
        remainder = money % number_of_aliens
        print(shared)
        print(remainder)

    @classmethod
    def _get_inputs(cls):
        input_num = input()
        temp_inputs = input_num.split(' ')
        return int(temp_inputs[0]), int(temp_inputs[1])


if __name__ == '__main__':
    Solve.run()