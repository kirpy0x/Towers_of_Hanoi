from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with? : "))
while num_disks < 3:
  num_disks = int(input("\nEnter a number greater than or equal to 3\n"))
#ADD DISCS
#for num in range(num_disks):
  #left_stack.push("Disk {}".format(num))
for num in range(num_disks, 0 , -1):
  #slant_num += "|"
  left_stack.push("|"*num)
  
num_optimal_moves = 2 ** num_disks - 1
print("The fastest you can solve this game is in {} moves.".format(num_optimal_moves))
#Get User Input

def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while True:
    #PRINT OPTIONS
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {letter} for {name}".format(letter=letter,name=name))
    #CHOOSE OPTION  
    user_input = input("").upper()
    if user_input in choices:
        for i in range(len(stacks)):
          if user_input == choices[i]:
            return stacks[i]

#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  #PRINT THE STACKS
  print("\n\n\n")
  for stack in stacks:
    stack.print_items()
  #MAKE YOUR MOVE
  while True:
    print("\nStack to move from? : ")
    from_stack = get_input()
    print("\nStack to move to? : ")
    to_stack = get_input()
    #CHECK IF MOVE IS VALID
    if from_stack.is_empty() == True:
      print("\n\n{} is empty!".format(from_stack.name))
    elif to_stack.is_empty() == True or from_stack.peek() < to_stack.peek():
      #MOVE THE DISK
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try again.")
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}.".format(num_user_moves, num_optimal_moves))