#Hide the card number and show the last 4 digits 
def card_hide(numbers):
    last_four=numbers[-4:]
    hidden_part="*" *((len(numbers)-4))
    return hidden_part+last_four
   

    
card_number=input("Enter card number:")
result=card_hide(card_number)
print(result)