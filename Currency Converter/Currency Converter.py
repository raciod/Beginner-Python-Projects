from currency_converter import CurrencyConverter
from Get_transfer_information import Get_transfer_information


def currency_converter() :
    # Your existing function code here...

    if __name__ == "__main__":
        c = CurrencyConverter()
        # get the values from the other function
        convert_from, convert_to, value = Get_transfer_information()

        The_value_after_conversion = c.convert(value, convert_from, convert_to)

        print("Original Value:", value, convert_from)
        print("Converted Value:", The_value_after_conversion, convert_to)


currency_converter()