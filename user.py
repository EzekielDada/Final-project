class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.utilities = expenses.get("utilities", 0)
        self.entertainment = expenses.get("entertainment", 0)
        self.school_fees = expenses.get("school_fees", 0)
        self.shopping = expenses.get("shopping", 0)
        self.healthcare = expenses.get("healthcare", 0)

    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
            "utilities": self.utilities,
            "entertainment": self.entertainment,
            "school_fees": self.school_fees,
            "shopping": self.shopping,
            "healthcare": self.healthcare,
        }

    def to_csv_row(self):
        return [
            self.age,
            self.gender,
            self.total_income,
            self.utilities,
            self.entertainment,
            self.school_fees,
            self.shopping,
            self.healthcare,
        ]

    @staticmethod
    def csv_headers():
        return ["age", "gender", "total_income", "utilities", "entertainment", "school_fees", "shopping", "healthcare"]
