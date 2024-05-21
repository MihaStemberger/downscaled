class ScaleResponse:
    def __init__(self):
        self._weight = None
        self._bmi = None
        self._height = None
        self._year = None
        self._month = None
        self._day = None
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._body_fat_percentage = None
        self._basal_metabolism = None
        self._muscle_percentage = None
        self._soft_lean_mass = None
        self._body_water_mass = None
        self._impedance = None

    @property
    def weight(self):
        return self._weight

    @property
    def bmi(self):
        return self._bmi

    @property
    def height(self):
        return self._height

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @property
    def seconds(self):
        return self._seconds

    @property
    def body_fat_percentage(self):
        return self._body_fat_percentage

    @property
    def basal_metabolism(self):
        return self._basal_metabolism

    @property
    def muscle_percentage(self):
        return self._muscle_percentage

    @property
    def soft_lean_mass(self):
        return self._soft_lean_mass

    @property
    def body_water_mass(self):
        return self._body_water_mass

    @property
    def impedance(self):
        return self._impedance

    @weight.setter
    def weight(self, value):
        # You can add validation logic here if needed
        self._weight = value

    @bmi.setter
    def bmi(self, value):
        # You can add validation logic here if needed
        self._bmi = value

    @height.setter
    def height(self, value):
        # You can add validation logic here if needed
        self._height = value

    @year.setter
    def year(self, value):
        # You can add validation logic here if needed
        self._year = value

    @month.setter
    def month(self, value):
        # You can add validation logic here if needed
        self._month = value

    @day.setter
    def day(self, value):
        # You can add validation logic here if needed
        self._day = value

    @hours.setter
    def hours(self, value):
        # You can add validation logic here if needed
        self._hours = value

    @minutes.setter
    def minutes(self, value):
        # You can add validation logic here if needed
        self._minutes = value

    @seconds.setter
    def seconds(self, value):
        # You can add validation logic here if needed
        self._seconds = value

    @body_fat_percentage.setter
    def body_fat_percentage(self, value):
        # You can add validation logic here if needed
        self._body_fat_percentage = value

    @basal_metabolism.setter
    def basal_metabolism(self, value):
        # You can add validation logic here if needed
        self._basal_metabolism = value

    @muscle_percentage.setter
    def muscle_percentage(self, value):
        # You can add validation logic here if needed
        self._muscle_percentage = value

    @soft_lean_mass.setter
    def soft_lean_mass(self, value):
        # You can add validation logic here if needed
        self._soft_lean_mass = value

    @body_water_mass.setter
    def body_water_mass(self, value):
        # You can add validation logic here if needed
        self._body_water_mass = value

    @impedance.setter
    def impedance(self, value):
        # You can add validation logic here if needed
        self._impedance = value
