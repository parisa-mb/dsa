class BigNumber:
    def __init__(self, num1=0, num2=0):
        self.digits1 = [int(d) for d in str(num1)]
        self.digits2 = [int(d) for d in str(num2)]
        self.digits = []

    def summation(self):

        max_num = max(len(self.digits1), len(self.digits2))
        self_digits1 = [0] * (max_num - len(self.digits1)) + self.digits1
        self_digits2 = [0] * (max_num - len(self.digits2)) + self.digits2
        # for i in range((max_num - len(self.digits1))):
        #     self_digits.insert(0, 0)
        # for i in range((max_num - len(self.digits2))):
        #     num2_digits.insert(0,0)

        result = []
        carry = 0
        for i in range(max_num - 1, -1, -1):
            a = self.digits1[i]
            b = self.digits2[i]
            total = a + b + carry
            result.insert(0, total %10)
            carry = total //10

        if carry > 0:
            result.insert(0, carry)

        self.digits = result
        return BigNumber(''.join(map(str, result)))

    def minus(self):
        if len(self.digits1) < len(self.digits2) or (len(self.digits1) == len(self.digits2) and self.digits1 < self.digits2):
            raise ValueError("first number is smaller than the second number.")
        max_num = max(len(self.digits1), len(self.digits2))
        self_digits1 = [0] * (max_num - len(self.digits1)) + self.digits1
        self_digits2 = [0] * (max_num - len(self.digits2)) + self.digits2

        # for i in range((max_num - len(self.digits1))):
        #     self_digits.insert(0, 0)
        # for i in range((max_num - len(self.digits2))):
        #     num2_digits.insert(0, 0)

        result = []
        extra = 0
        for i in range(max_num - 1, -1, -1):
            a = self.digits[i]
            b = self.digits2[i]
            total = a - b - extra
            if total < 0:
                total += 10
                extra = 1
            else:
                extra = 0
            result.insert(0, total)

        self.digits = result
        return BigNumber(''.join(map(str, result)))

    def left_shift(self):
        self.digits.append(0)

    def right_shift(self):
        self.digits.insert(0, 0)
        self.digits.pop()

    def __str__(self):
        return ''.join(map(str, self.digits1))


num = BigNumber(224, 126)
result = num.summation()
print("Sum:", result)

result_minus = num.minus()
print("minus:", result_minus)
num.left_shift()
print("Left Shift:", num) 

num.right_shift()
print("Right Shift:", num)