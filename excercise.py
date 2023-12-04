class FoodOrder:
    def __init__(self, food_name, amount_ordered):
        self._food_name = food_name
        self._amount_ordered = amount_ordered
        self._standard_price_per_pound = self._get_standard_price_per_pound()
        self._calculated_price = None

    def _get_standard_price_per_pound(self):
        if self._food_name == "Dry Cured Iberian Ham":
            return 177.80
        elif self._food_name == "Wagyu Steaks":
            return 450.00
        elif self._food_name == "Matsutake Mushrooms":
            return 272.00
        elif self._food_name == "Kopi Luwak Coffee":
            return 306.50
        elif self._food_name == "Moose Cheese":
            return 487.20
        elif self._food_name == "White Truffles":
            return 3600.00
        elif self._food_name == "Blue Fin Tuna":
            return 3603.00
        elif self._food_name == "Le Bonnotte Potatoes":
            return 270.81
        else:
            return 0

    def cost_of_ordered_food(self):
        self._calculated_price = self._amount_ordered * self._standard_price_per_pound
        return self._calculated_price
