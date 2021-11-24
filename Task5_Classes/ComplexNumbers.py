class ComplexNumbers:
    real = 0
    imag = 0

    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.imag = imag_part

    def print(self):
        if self.imag >= 0:
            print(str(self.real) + "+" + str(self.imag) + "j")
        else:
            print(str(self.real) + str(self.imag) + "j")

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumbers(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumbers((self.real * other.real) - (self.imag * other.imag), (self.real * other.imag) + (other.real * self.imag))

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def conj(self):
        return ComplexNumbers(self.real, -self.imag)


def main():
    pass


if __name__ == '__main__':
    main()
