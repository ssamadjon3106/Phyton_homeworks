import string

def word_frequency():
    file_name = 'sample.txt'
    
    # Try to open and read the file
    try:
        with open(file_name, mode='r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f'{file_name} not found.')
        text = input("Enter a paragraph to create the file: ")
        with open(file_name, mode='w') as file:
            file.write(text)
    
    # Clean up the text
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation

    words = text.split()
    words_count = {}

    # Count the frequency of each word
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1

    total_words = len(words)
    
    # Sort words by frequency (descending)
    sorted_word_count = sorted(words_count.items(), key=lambda x: x[1], reverse=True)

    # Print the results to the console
    print(f"Total words: {total_words}")
    print('Top 5 most common words:')
    
    for i in range(min(5, len(sorted_word_count))):  # Avoid going out of bounds
        word, count = sorted_word_count[i]
        print(f'{word} - {count} times')

    # Writing the results to a report file
    with open("word_count_report.txt", mode='w') as report_file:
        report_file.write("Word count report\n")
        report_file.write(f"Total words: {total_words}\n")
        report_file.write('Top 5 most common words:\n')
        
        for i in range(min(5, len(sorted_word_count))):  # Avoid going out of bounds
            word, count = sorted_word_count[i]
            report_file.write(f'{word} - {count} times\n')  # Ensure proper formatting
            report_file.flush()  # Ensure everything is written out

# Call the function to run the word frequency analysis
word_frequency()

