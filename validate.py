def validate_interger(prompt, error):
    while True:
        try:
            reponse = int(input(prompt))
            return response
            break
        except:
            print(error)
def validate_pos_int(prompt,error):
    while True:
        try:
            response = int(input(prompt))
            if response > 0:
                return response
                break
            else:
                print(error)
        except:
            print(error)
def validate_floating_point(prompt, error):
    while True:
        try:
            reponse = float(input(prompt))
            return response
            break
        except:
            print(error)
def validate_pos_float(prompt,error):
    while True:
        try:
            response = float(input(prompt))
            if response > 0:
                return response
                break
            else:
                print(error)
        except:
            print(error)