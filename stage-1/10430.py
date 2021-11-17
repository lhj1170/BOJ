class Solve:
    @classmethod
    def run(cls):
        a, b, c = cls._get_input()
        cls._solve(a, b, c)

    @classmethod
    def _get_input(cls):
        data = input()
        refined = data.split(' ')
        return int(refined[0]), int(refined[1]), int(refined[2])

    @classmethod
    def _solve(cls, a, b, c):
        print((a + b) % c)
        print(((a % c) + (b % c)) % c)
        print((a * b) % c)
        print(((a % c) * (b % c)) % c)


if __name__ == '__main__':
    Solve.run()
