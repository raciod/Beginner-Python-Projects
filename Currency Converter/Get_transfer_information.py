def Get_transfer_information():
    # the currency to convert from
    print("Choose the currency to convert from:")
    print(
        '''
    1. USD: US dollar
    2. JPY: Japanese yen
    3. BGN: Bulgarian lev
    4. CZK: Czech koruna
    5. DKK: Danish krone
    6. GBP: Pound sterling
    7. HUF: Hungarian forint
    8. PLN: Polish zloty
    9. RON: Romanian leu
    10. SEK: Swedish krona
    11. CHF: Swiss franc
    12. ISK: Icelandic krona
    13. NOK: Norwegian krone
    14. TRY: Turkish lira
    15. AUD: Australian dollar
    16. BRL: Brazilian real
    17. CAD: Canadian dollar
    18. CNY: Chinese yuan renminbi
    19. HKD: Hong Kong dollar
    20. IDR: Indonesian rupiah
    21. INR: Indian rupee
    22. KRW: South Korean won
    23. MXN: Mexican peso
    24. MYR: Malaysian ringgit
    25. NZD: New Zealand dollar
    26. PHP: Philippine peso
    27. SGD: Singapore dollar
    28. THB: Thai baht
    29. ZAR: South African rand
    '''
    )
    convert_from = input("Enter (USD, JPY, BGN...) to select your choice: ").upper()

    # the currency to convert to
    print("Choose the currency to convert to")
    print(
        '''
    1. USD: US dollar
    2. JPY: Japanese yen
    3. BGN: Bulgarian lev
    4. CZK: Czech koruna
    5. DKK: Danish krone
    6. GBP: Pound sterling
    7. HUF: Hungarian forint
    8. PLN: Polish zloty
    9. RON: Romanian leu
    10. SEK: Swedish krona
    11. CHF: Swiss franc
    12. ISK: Icelandic krona
    13. NOK: Norwegian krone
    14. TRY: Turkish lira
    15. AUD: Australian dollar
    16. BRL: Brazilian real
    17. CAD: Canadian dollar
    18. CNY: Chinese yuan renminbi
    19. HKD: Hong Kong dollar
    20. IDR: Indonesian rupiah
    21. INR: Indian rupee
    22. KRW: South Korean won
    23. MXN: Mexican peso
    24. MYR: Malaysian ringgit
    25. NZD: New Zealand dollar
    26. PHP: Philippine peso
    27. SGD: Singapore dollar
    28. THB: Thai baht
    29. ZAR: South African rand
    '''
    )
    convert_to = input("Enter (USD, JPY, BGN...) to select your choice: ").upper()

    # value
    value = int(input("How much do you want to convert? "))

    return convert_from , convert_to , value
