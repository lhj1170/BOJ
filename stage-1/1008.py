class Solve:
    @classmethod
    def run(cls):
        a, b = cls._get_input()
        print(a / b)

    @classmethod
    def _get_input(cls):
        data = input()
        refined = data.split(' ')
        return int(refined[0]), int(refined[1])


if __name__ == '__main__':
    Solve.run()
