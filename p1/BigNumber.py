def multiply_lists(a, b):

    max_len = max(len(a), len(b))
    a = [0] * (max_len - len(a)) + a
    b = [0] * (max_len - len(b)) + b

    result = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        carry = 0
        for j in range(len(b) - 1, -1, -1):
            product = a[i] * b[j] + result[i + j + 1] + carry
            result[i + j + 1] = product % 10
            carry = product // 10
        result[i + j] += carry

    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    return result


def subtract_one(number):
    number = number.copy()

    i = len(number) - 1
    while i >= 0 and number[i] == 0:
        number[i] = 9
        i -= 1

    if i >= 0:
        number[i] -= 1
    else:
        number.insert(0, 9)

    return number


class BigNumber:
    def __init__(self, num):
        self.sign = num[0:1]
        num = num[1:]
        self.digits = [int(d) for d in num]


    def the_bigger_value(self, bigNumber):
        if int(''.join(map(str, self.digits))) > int(''.join(map(str, bigNumber.digits))):
            return self.digits
        elif int(''.join(map(str, self.digits))) < int(''.join(map(str, bigNumber.digits))):
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

            return BigNumber(result)

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
                absolute_sign = bigNumber.sign
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


    def multiplication(self, bigNumber):

        if self.digits == [0] or bigNumber.digits == [0]:
            return 0

        result_len = len(self.digits) + len(bigNumber.digits)
        result = [0] * result_len

        for i in range(len(self.digits) - 1, -1, -1):
            carry = 0
            for j in range(len(bigNumber.digits) - 1, -1, -1):
                current_result = self.digits[i] * bigNumber.digits[j] + result[i + j + 1] + carry
                result[i + j + 1] = current_result % 10
                carry = current_result // 10

            result[i + j] += carry

        return result

    def division(self, bigNumber):

        max_num = max(len(self.digits), len(bigNumber.digits))
        self_digits1 = [0] * (max_num - len(self.digits)) + self.digits
        self_digits2 = [0] * (max_num - len(bigNumber.digits)) + bigNumber.digits
        if bigNumber == 0:
            raise ValueError("division by zero")

        dividend_digits = self.digits
        divisor_digits = bigNumber.digits

        result = []
        current_result = 0

        for digit in self_digits1:
            current_result = current_result * 10 + digit
            count = 0
            while current_result >= int(str(bigNumber)):
                current_result -= int(str(bigNumber))
                count += 1

            result.append(count)

        result = ''.join(map(str, result))
        return result

    def factorial(self):

        the_thing = int(''.join(map(str, self.digits)))

        if the_thing > 100:
            raise ValueError("Number is larger than 100")

        current_result = [1]

        current_num = self.digits

        while int(''.join(map(str, current_num))) >1:
            current_result = multiply_lists(current_result, current_num)

            current_num = subtract_one(current_num)

        return ''.join(map(str, current_result))


    def power(self, bigNumber):
        if bigNumber.sign == '-':
            if self.sign == '-':
                if bigNumber.digits.index(len(bigNumber.digits)-1) % 2 == 0:
                    result = self.power_by(bigNumber)
                    result = int(''.join(map(str, result)))
                    return 1/result
                else:
                    result = self.power_by(bigNumber)
                    result = ''.join(map(str, result))
                    return '-' + 1/result
            else:
                result = self.power_by(bigNumber)
                result = ''.join(map(str, result))
                return 1/ result
        else:
            if self.sign == '-' :
                if bigNumber.digits.index(len(bigNumber.digits)-1) % 2 == 0:
                    result = self.power_by(bigNumber)
                    result = '-' +''.join(map(str, result))
                    return result
            else:
                result = self.power_by(bigNumber)
                result = ''.join(map(str, result))
                return result

    def power_by(self, bigNumber):

        exponent_value = int(''.join(map(str, bigNumber.digits)))

        if exponent_value == 0:
            return BigNumber('+1')
        elif exponent_value == 1:
            return self

        result = BigNumber(('+' + ''.join(map(str, self.digits))))
        current_base = self

        while exponent_value > 0:
            result = result.multiply(result)
            if exponent_value % 2 == 1:
                result = result.multiply(current_base)
                exponent_value -= 1
            exponent_value //= 2

        return result

    def divide(self, bigNumber):
        if self.sign != bigNumber.sign:
            result = self.division(bigNumber)
            return '-' + result
        else:
            result = self.division(bigNumber)
            return result

    def multiply(self, bigNumber):
        if self.sign != bigNumber.sign:
            result = self.multiplication(bigNumber)
            return BigNumber('-' + ''.join(map(str, result)))
        else:
            result = self.multiplication(bigNumber)
            return BigNumber(''.join(map(str, result)))

    def left_shift(self, places=1):
        self.digits.extend([0] * places)

    def right_shift(self):
        self.digits.insert(0, 0)
        self.digits.pop()

    def karatsuba_multiply_helper(x, y):

        # x = [int(d) for d in x]
        # y = [int(d) for d in y]

        if len(x.digits) == 1 and len(y.digits) == 1:
            product = x[0] * y[0]
            return product

        max_len = max(len(x), len(y))
        x = [0] * (max_len - len(x)) + x
        y = [0] * (max_len - len(y)) + y

        mid = max_len // 2
        high1 = x[:mid]
        low1 = x[mid:]
        high2 = y[:mid]
        low2 = y[mid:]

        a = karatsuba_multiply_helper(low1, low2)
        b = karatsuba_multiply_helper(low1 + high1, low2 + high2)
        c = karatsuba_multiply_helper(high1, high2)

        result = shift_left(c, 2 * (max_len - mid))
        result = add_lists(result, shift_left(subtract_lists(b, add_lists(a, c)), max_len - mid))
        result = add_lists(result, a)

        return result

    def add_lists(a, b):
        max_len = max(len(a), len(b))
        a = [0] * (max_len - len(a)) + a
        b = [0] * (max_len - len(b)) + b

        result = []
        carry = 0
        for i in range(max_len - 1, -1, -1):
            total = a[i] + b[i] + carry
            result.insert(0, total % 10)
            carry = total // 10

        if carry:
            result.insert(0, carry)

        return result

    def subtract_lists(a, b):
        max_len = max(len(a), len(b))
        a = [0] * (max_len - len(a)) + a
        b = [0] * (max_len - len(b)) + b

        result = []
        borrow = 0
        for i in range(max_len - 1, -1, -1):
            diff = a[i] - b[i] - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.insert(0, diff)

        return result

    def shift_left(digits, count):
        return digits + [0] * count


    def __str__(self):
        return ''.join(map(str, self.digits))




num1 = BigNumber('+2')
num2 = BigNumber('+10')
num3 = BigNumber('+50')
# result1 = num3.factorial()
# result2 = num1.divide(num2)
# result3 = num1.adding(num2)
result4 = num1.multiply(num2)
rrrr = num1.power_by(num2)
# hkjs = num1.karatsuba_multiply_helper(num2)
print('\nmultiply ' + result4, rrrr)

