# James Taddei
# Energy Rating Calc
# 5/1/23

def main():
    print(f"The energy rating: {calculateEnergyRating()}")

def calculateEnergyRating() -> str:
    """
    Calculates and returns the energy rating of a lightbulb
    after prompting the user to input the luminous flux and
    power consumption. 
    """
    luminousFlux, powerConsumption = inputData() # User input
    energyRating = luminousFlux / powerConsumption # Calculation

    # Determining rating
    if (energyRating >= 210): # A rating
        raise Exception("The rating is too high")
    elif (energyRating >= 185): # B rating
        return "B"
    elif (energyRating >= 160): # C rating
        return "C"
    elif (energyRating >= 135): # D rating
        return "D"
    elif (energyRating >= 110): # E rating
        return "E"
    elif (energyRating >= 85): # F rating
        return "F"
    else: # G rating
        raise Exception("The rating is too low")

def inputData() -> tuple:
    """
    Returns the inputted luminous flux and power consumption
    as integers in a tuple.
    """
    luminousFlux = float(input("Enter the luminous flux in lumens: "))
    powerConsumption = float(input("Enter the power consumption in kilowatts per 1,000 hours: "))
    return (luminousFlux, powerConsumption)

main()