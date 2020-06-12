class Percentage():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def increase_function(cls, x, y): # 1. Find the percentage increase / decrease
        result = round(((y - x) / x * 100), 2)
        if result > 0:
            return("\nIncreased by %s%%\n" %result)
        elif result < 0:
            return("\nDecreased by %s%%\n" %(result * -1))
        else:
            return("\nThere was no change.\n")

    @classmethod
    def one_of_the_other_function(cls, x, y): # 2. Find out what percentage one number is of the other
        result = round((x / y * 100), 2)
        return ("\nIt is %s%%\n" %result)

    @classmethod
    def gst_sub_function(cls, x, y): # 3. Find out the net value
        result = round((x / (100 + y) * 100), 2)
        return ("\nThe amount before added percentage is %s\n" %result)

    @classmethod
    def add_function(cls, x, y): # 4. Add percentage to a number
        result = round((x * (y / 100 + 1)), 2)
        return ("\nThe final amount is %s\n" %result)

    @classmethod
    def substract_function(self): # 5. Substract percentage from a number
        result = round((x * ((100 - y) / 100)), 2)
        return ("\nThe final amount is %s\n" %result)

    @classmethod
    def perc_number_function(self): # 6. Find percentage of a number
        result = round((x * y /100), 2)
        return("\n%s%% of %s is %s\n" % (y, x, result))

    #def json(self):
        #return {
        #"x": self.x,
        #"y": self.y
        #}

#r = Percentage(45, 50)
#print(r.increase())

#x = float(input())
#y = float(input())
#r = Percentage(x, y)
#print(r.increase())
