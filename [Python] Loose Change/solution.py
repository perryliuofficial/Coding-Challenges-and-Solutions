def main(change_required: float):
    try:
        if change_required < 0:
            print("Error! Change is negative. Please ask your customer to code their own code instead.")
            return False
    except TypeError:
        print("Error! Not a number!")
        return False
    coins = [2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    coins_output = []
    changeCalculation(change_required,coins,coins_output)

def changeCalculation(change_required: float, coins, coins_output):
    remaining_change = change_required

    for i in coins:
        count = remaining_change // i
        if count >= 1:
            coins_output.append(coinsFormatting(i) + " x " + str(int(count)))
            remaining_change -= (i*count)
            remaining_change = round(remaining_change,2)
    print (coins_output)

def coinsFormatting(input):
    if input >=1:
        return ("£"+str(int(input)))
    if input <1:
        input = input*100
        return (str(int(input)) + "p")

main(0.98)