class Register(int):
    # val - int value of register
    # size - max value of register before overflow
    def __new__(cls, val=0, size=0xFF):
        # Create a new register with max value of "size"
        new_reg = super(Register, cls).__new__(cls, val & size)
        new_reg.did_overflow = val & size < val
        new_reg.size = size
        return new_reg

    # ADD
    def __add__(self, num):
        new_val = int.__add__(self, num)

        return Register(new_val, self.size)

    # OR
    def __or__(self, num):
        new_val = int.__or__(self, num)

        return Register(new_val, self.size)

    # AND
    def __and__(self, num):
        new_val = int.__and__(self, num)

        return Register(new_val, self.size)

    # XOR
    def __xor__(self, num):
        new_val = int.__xor__(self, num)

        return Register(new_val, self.size)


    def __str__(self):
        return "%d" % int(self)
