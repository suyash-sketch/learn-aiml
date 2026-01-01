class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [items.strip() for items in text.split(",")]
    

raw = " water, milk, ginger , honey "

# obj = ChaiUtils()
# cleaned =  obj.clean_ingredients(raw)

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)