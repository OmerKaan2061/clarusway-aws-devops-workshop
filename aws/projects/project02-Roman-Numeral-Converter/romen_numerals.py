numbers = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
           90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV",  1: "I"}



def convert(given_number):
    try:
            given_number = int(given_number)
            romen_number = ""
            if given_number < 1 or given_number > 3999:
                return False

            for i in numbers:
                while i <= given_number:
                    romen_number += numbers[i]
                    given_number -= i
            return romen_number
    
    except:
        return False


