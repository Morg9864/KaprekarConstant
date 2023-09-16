# reverse => 521 -> 125
# eligibility => hundreds > tens > units
# prove1089 
# finalProof 

def reverse(number):
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return reversed_number

def eligibility(number):
    hundreds = number // 100
    tens = (number % 100) // 10
    units = number % 10
    
    if not hundreds > tens > units:
        return False
    
    return True

def prove1089(number):
    if not eligibility(number):
        return -1
    
    reversed_number = reverse(number)
    result = number - reversed_number
    proof = result + reverse(result)
    
    if proof != 1089:
        return -2
    
    return 1

def finalProof():
    
    for number in range(100, 999):
        if prove1089(number) == -2:
            print("The video was incorrect")
            return False
        
    print("Every eligible number has passed the algorithm")
    return True

finalProof()