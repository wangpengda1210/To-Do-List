def final_deposit_amount(*interest, amount=1000):
    deposit = amount
    for i in interest:
        deposit += i / 100 * deposit
    return round(deposit, 2)
