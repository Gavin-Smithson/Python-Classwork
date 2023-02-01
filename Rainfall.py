def main():
    total_rainfall_Mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    rainfall_Nums = [0.0] * 12
    total_rainfall = 0.0
    #Loop to get inputs
    for index in range(len(rainfall_Nums)):
        while True:
            try:
                rainfall_Nums[index] = float(input("Enter the rainllfall for month {:.0f}:  ".format(index + 1)))
                break
            except:
                 print("Invalid rainfall")
        #Get total Rainfall
    total_rainfall += rainfall_Nums[index]
    #Get the average
    average_rainfall = total_rainfall/12
    #Get max and min
    max_rainfall = max(rainfall_Nums)
    min_rainfall = min(rainfall_Nums)
    #Print the outputs

    print('{}\n\n{}\n\nThe total rainfall was {}. The average rainfall was {}. The maxium rainfall was {}. The mimimum rainfall was {}'
          .format(total_rainfall_Mon, rainfall_Nums, total_rainfall, average_rainfall, max_rainfall, min_rainfall))











if __name__ == "__main__":
    main()