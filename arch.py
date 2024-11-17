import json

txt_arch = "arch.txt"
json_arch = "arch.json"

def obtain_soup_info(txt_arch):
    """
    Obtain information that is in the txt file
    """

    with open(txt_arch) as t:
        soup_info = t.read().split("---")
    return soup_info

def obtain_letters():
    """
    Function that gets the letters from letters soup in txt file
    by splitting them from each row and culumn into a list
    """

    info = obtain_soup_info(txt_arch)
    splitted_letters = []
    all_letters = info[0].splitlines()
    for lines in all_letters:
        splitted_letters.append(lines.split(" "))
    return splitted_letters

def obtain_correct_words():
    """
    Function that gets the words that the algoritm is 
    going to check is they are or not in the letter soup
    """

    soup_info = obtain_soup_info(txt_arch)
    words_to_check = soup_info[1].strip().splitlines()
    return words_to_check



def horizontal_lines(all_letters):
    """
    Function that splits the grid by rows
    (left to right and rigth to left) and
    puts them in a list that holds the 
    posible horizontal words
    """

    posible_horizontal = [] 
    for letters in all_letters:
        posible_horizontal.append("".join(letters))  #normal options
        letters.reverse()
        posible_horizontal.append("".join(letters))  #reversed options
    return posible_horizontal



def vertical_lines(all_letters, num_all_letters): #num_all_letters is the number of rows in the grid        
    """
    function that forms words with each column of the grid
    and holds it in a list
    """
    vertical_options = []
    for column in range(num_all_letters):
        vertical_word = ""
        reversed_word = ""
        for row in all_letters:
            vertical_word += row[column]  #up to down options
            reversed_word = row[column] + reversed_word #down to up options
        vertical_options.append(vertical_word)
        vertical_options.append(reversed_word)
    return vertical_options



def possible_lines():
    """
    function that convines all posible 
    horizontal and verticall words in a variable
    """
    all_letters = obtain_letters()
    num_all_letters = len(all_letters[0])
 
    horizontal_words = horizontal_lines(all_letters)
    vertical_words = vertical_lines(all_letters, num_all_letters)


    total_to_check = horizontal_words + vertical_words
    return total_to_check



def check_word(total_to_check, words_to_check):
    """
    function that checks if the correct words 
    are in all the possible words list
    """

    results = {}
    for word in words_to_check:
        flag = False
        for p_word in total_to_check:
            if word in p_word:
                flag = True
                results[word] = flag
        if not flag:
            results[word] = flag
    return results



def write_in_json_file():
    """
    funtion that writes in the json file  if the
    words form the txt are in the letters soup or not
    """
    results = check_word(possible_lines(), obtain_correct_words())
    with open(json_arch, "w") as f:
        json.dump(results, f, indent=4)

write_in_json_file()