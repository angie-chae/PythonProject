# @author Dabin Chae

# @precondition temperature <= 50, windspeed >= 4 MPH
# @param temperature The temperature in degrees Fahrenheit
temperature = float(input("Enter a temperature of at most 50 degrees Fahrenheit: "))

# @param windspeed The windspeed in MPH
windSpeed = float(input("Enter a windspeed of at least 4 MPH: "))

#getWindchill computes the windchill given a temperature and windspeed
def getWindchill(temperature, windSpeed):

    # @return The computed windchill
    return (35.74 + 0.6215 * temperature - 35.75 * windSpeed**0.16 +
    0.4275 * temperature * windSpeed**0.16)

print(f'Temperature (including wind chill): {getWindchill(temperature, windSpeed):.1f} degrees')
