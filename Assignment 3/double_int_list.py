def main():
  
  #set this to any double
  doubleValue = 3.8
  
  #set this to any int
  intValue = 5
  
  #print out addition, subtraction, multiplication, and division of these two values
  
  Print(doubleValue + intValue)
  Print(doubleValue - intValue)
  Print(doubleValue * intValue)
  Print(doubleValue / intValue)

  #populate this list
  myFriends = ["Sam","Ariel","Zoey","Keith"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])
  
  
  #populate this list with five numbers
  fiveNumbers = [1,2,4,6,8]
  
  Print(fiveNumbers[4] - fiveNumbers[8])
  Print(fiveNumbers[1] + fiveNumbers[6])
  Print(fiveNumbers[2] * fiveNumbers[2])
  Print(fiveNumbers[1] / fiveNumbers[4])
  #do each of the four equations with different numbers each time.

  fiveNumbers[4] = 7
  fiveNumbers[0] = 3
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  
  #print out the list
  print(fiveNumbers)
  #ask the user for their pet's name
  #create a list of the pets you have (if you have no pets, use a friend's) and append the user's response to the list of pets
  response=input("yo whats ur pets name dawg")

  Pets = ["Romano"]
  Pets.append(response)
main()
