class BigNumber:
    def __init__(self, num):
        self.sign = num[0:1]
        num = num[1:]
        self.digits = [int(d) for d in num]


    def convert_to_digits(self, num):
        return [int(d) for d in str(num)]

    def summation(self, bigNumber ):

        digits1 = self.digits
        digits2 = bigNumber.digits
        result = self.adding(digits1, digits2)
        return result

    def the_bigger_value(self, bigNumber):
        if ''.join(map(str, self.digits)) > ''.join(map(str, bigNumber.digits)):
            return self.digits
        elif ''.join(map(str, self.digits)) < ''.join(map(str, bigNumber.digits)):
            return bigNumber.digits
        else:
            return 0

    def adding(self, bigNumber):
        if self.sign == bigNumber.sign:

            max_num = max(len(self.digits), len(bigNumber.digits))
            self_digits1 = [0] * (max_num - len(self.digits)) + self.digits
            self_digits2 = [0] * (max_num - len(bigNumber.digits)) + bigNumber.digits

            result = []
            carry = 0
            for i in range(max_num - 1, -1, -1):
                a = self_digits1[i]
                b = self_digits2[i]
                total = a + b + carry
                result.insert(0, total %10)
                carry = total // 10

            if carry > 0:
                result.insert(0, carry)

            result = ''.join(map(str, result))
            result = self.sign + result

            return result

        if self.sign != bigNumber.sign:
            return self.subtract(bigNumber)

    def minus(self, bigNumber):
        if self.sign == bigNumber.sign:
            if self.the_bigger_value(bigNumber) == self.digits:
                result = self.subtract(bigNumber)

            else:
                result = bigNumber.subtract(self)
                result.sign = bigNumber.sign

        else:
            if bigNumber.sign == '+':
                bigNumber.sign = '-'
                result = self.adding(bigNumber)
            else:
                bigNumber.sign = '+'
                result = self.adding(bigNumber)
        return result


    def subtract(self, bigNumber):

        if self.sign != bigNumber.sign:
            if self.the_bigger_value(bigNumber) == self.digits:
                absolute_sign = self.sign
                max_num = max(len(self.digits), len(bigNumber.digits))
                self_digits1 = [0] * (max_num - len(self.digits)) + self.digits
                self_digits2 = [0] * (max_num - len(bigNumber.digits)) + bigNumber.digits

                result = []
                borrow = 0
                for i in range(max_num - 1, -1, -1):
                    diff = self_digits1[i] - self_digits2[i] - borrow
                    if diff < 0:
                        diff += 10
                        borrow = 1
                    else:
                        borrow = 0
                    result.insert(0, diff)

                result = ''.join(map(str, result))
                result = absolute_sign + result
                return result
            elif  self.the_bigger_value(bigNumber) == bigNumber.digits:
                absolute_sign = bigNumber.digits
                max_num = max(len(self.digits), len(bigNumber.digits))
                self_digits1 = [0] * (max_num - len(self.digits)) + self.digits
                self_digits2 = [0] * (max_num - len(bigNumber.digits)) + bigNumber.digits

                result = []
                borrow = 0
                for i in range(max_num - 1, -1, -1):
                    diff = self_digits1[i] - self_digits2[i] - borrow
                    if diff < 0:
                        diff += 10
                        borrow = 1
                    else:
                        borrow = 0
                    result.insert(0, diff)

                result = ''.join(map(str, result))
                result = absolute_sign + result
                return result

        if self.sign == bigNumber.sign:
            if self.the_bigger_value(bigNumber) == self.digits:
                max_num = max(len(self.digits), len(bigNumber.digits))
                self_digits1 = [0] * (max_num - len(self.digits)) + self.digits
                self_digits2 = [0] * (max_num - len(bigNumber.digits)) + bigNumber.digits

                result = []
                borrow = 0
                for i in range(max_num - 1, -1, -1):
                    diff = self_digits1[i] - self_digits2[i] - borrow
                    if diff < 0:
                        diff += 10
                        borrow = 1
                    else:
                        borrow = 0
                    result.insert(0, diff)

                result = ''.join(map(str, result))
                result = self.sign + result
                return result
            elif self.the_bigger_value(bigNumber) == bigNumber.digits:
                max_num = max(len(self.digits), len(bigNumber.digits))
                self_digits1 = [0] * (max_num - len(self.digits)) + self.digits
                self_digits2 = [0] * (max_num - len(bigNumber.digits)) + bigNumber.digits

                result = []
                borrow = 0
                for i in range(max_num - 1, -1, -1):
                    diff = self_digits1[i] - self_digits2[i] - borrow
                    if diff < 0:
                        diff += 10
                        borrow = 1
                    else:
                        borrow = 0
                    result.insert(0, diff)

                result = ''.join(map(str, result))
                result = bigNumber.sign + result
                return result

    def left_shift(self):
        self.digits.append(0)

    def right_shift(self):
        self.digits.insert(0, 0)
        self.digits.pop()

    def __str__(self):
        return ''.join(map(str, self.digits))




num1 = BigNumber('-224')
num2 = BigNumber('+126')
result = num1.adding(num2)
print("Sum:", result)

