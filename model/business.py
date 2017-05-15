class Business:

    TYPES = ["Taxis","Laundry","Barbers","Shipping","Bonds","Delivery","Pizza Parlor","Taco Shack","Real Estate","Printing Company","Tourist Trap","Ice Cream Plaza"]

    def __init__(self, type, name, income):
        self.__type = type
        self.__income = income
        self.__name = name

    def getIncome(self):
        return self.__income

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type
