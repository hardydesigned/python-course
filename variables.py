str = "String"
int_number = 10
float_number = 10.5
bool = True

print(str)
print(int_number)
print(float_number)
print(bool)

str2 = "String2"
concat = str + str2
print(concat)

#Operations

sum = int_number + float_number
print(sum)

sub = int_number - float_number
print(sub)

mul = int_number * float_number
print(mul)

div = int_number / float_number
print(div)

#Comparisons

greater = int_number > float_number
print(greater)

less = int_number < float_number
print(less)

equal = int_number == float_number
print(equal)

not_equal = int_number != float_number
print(not_equal)

greater_equal = int_number >= float_number
print(greater_equal)

less_equal = int_number <= float_number
print(less_equal)

#Logical

and_op = True and False
print(and_op)

or_op = True or False
print(or_op)

not_op = not True
print(not_op)

#Identity

is_op = str is str2
print(is_op)

is_not_op = str is not str2

#Membership

in_op = "S" in str
print(in_op)

not_in_op = "S" not in str
print(not_in_op)

#Bitwise

bitwise_and = 2 & 3
bitwise_or = 2 | 3
bitwise_xor = 2 ^ 3
bitwise_not = ~2
bitwise_shift_left = 2 << 1
bitwise_shift_right = 2 >> 1

print(bitwise_and)
print(bitwise_or)
print(bitwise_xor)
print(bitwise_not)
print(bitwise_shift_left)
print(bitwise_shift_right)

#Math functions
import math

abs_number = abs(-10)
print(abs_number)

round_number = round(10.5)
print(round_number)

pow_number = pow(2, 3)
print(pow_number)

sqrt_number = math.sqrt(16)
print(sqrt_number)

floor_number = math.floor(10.5)
print(floor_number)

ceil_number = math.ceil(10.5)
print(ceil_number)