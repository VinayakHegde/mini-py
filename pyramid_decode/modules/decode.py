def decode(message_file):
    # Read the contents of the file
  with open(message_file, 'r') as file:
      lines = file.readlines()

  # Extract numbers and words from each line
  pairs = [(int(line.split()[0]), line.split()[1]) for line in lines]

  # Sort pairs based on the first element (numbers)
  pairs.sort()

  # Extract words corresponding to the sorted numbers
  selected_words = [pair[1] for pair in pairs]
  # Create a pyramid of numbers
  pyramid = []
  current_row = 1
  current_index = 0

  while current_index < len(selected_words):
      row_words = selected_words[current_index]
      pyramid.append(row_words)
      current_row += 1
      current_index += current_row
  
  # Join the words in each row and concatenate rows into a string
  decoded_message = ' '.join(pyramid)
  return decoded_message