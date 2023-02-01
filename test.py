daily_sales = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

days_of_week = ['Sunday', 'Monday', 'Tuesday',

                    'Wednesday', 'Thursday', 'Friday',

                    'Saturday']

for i in range(7):

        daily_sales[i] = float(input('Enter the sales for ' + day_of_week[i] + ': '))

print(daily_sales)
print(days_of_week)