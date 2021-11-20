class Solve:
    @classmethod
    def run(cls):
        tmp_hexa_code = cls._get_input()
        decimal = cls._convert_hexa_code_to_decimal(tmp_hexa_code)
        print(decimal)

    @classmethod
    def _get_input(cls):
        input_num = input()
        return input_num

    @classmethod
    def _convert_hexa_code_to_decimal(cls, tmp_hexa_code):
        return int(tmp_hexa_code, 16)


if __name__ == '__main__':
    Solve.run()
