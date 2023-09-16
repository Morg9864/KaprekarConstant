# reverse
# eligibility => hundreds > tens > units

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

# 521 
def prove1089(number):
    
    if not eligibility(number):
        return -1
    
    reversed_number = reverse(number)
    result = number - reversed_number
    proof = result + reverse(result)
    
    if proof != 1089:
        return -2
    
    return 1

# For every 3-digits number eligible
def finalProof():
    
    for num in range (100, 999):
        if prove1089(num) == -2:
            print("Sorry guys, the video was incorrect because of the exception : " + str(num))
            break
        
    print("Every eligible number has passed the algorithm")
        
finalProof()
