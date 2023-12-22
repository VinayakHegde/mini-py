def get_integer(prompt): 
  user_input = input(prompt)
  try:
    # Convert the input to a int
    user_number = int(user_input)
    return user_number

  except ValueError:
    print("Invalid input.")
    return get_integer('Please enter a valid integer: ')
