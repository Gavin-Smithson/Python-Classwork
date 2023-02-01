import validate
def prop_calculations(prop_value):
    assessment_value = prop_value * .6
    tax = (assessment_value/100) * .72
    return assessment_value , tax

def main():
    prop_value = validate.validate_pos_float('Enter the value of your property.: ', 'Error')
    assessment_value,tax = prop_calculations(prop_value)
    print('Your property value is {:.2f}\nYour propertry assessment value is {:.2f}\nYour property tax is {:.2f}'.format(prop_value,assessment_value,tax))






if __name__ == "__main__":
    main()