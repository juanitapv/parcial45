import json
file_path="input.txt"
path_results="results.json"
def get_f_info(file_path):
    with open(file_path) as f:
        info=f.read().split("---") 
    return info

def get_words():
    global file_path
    info=get_f_info(file_path)

    words=info[1].strip().splitlines()
    return words

def get_letters():
    global file_path
    info=get_f_info(file_path)

    new_letters=[]
    letters=info[0].strip().splitlines()
    for row in letters:
        new_letters.append(row.split(" "))
    return new_letters

def vertical_lines(letters, m):  
        possible_v=[]
        for x in range(0, m):
            y_total=[]
            for y in letters:
                y_total.append(y[x])

            possible_v.append("".join(y_total))
            y_total.reverse()
            possible_v.append("".join(y_total))
        return possible_v
                    
def horizontal_lines(letters):
    posible_h=[]
    for y in letters:
        posible_h.append("".join(y))
        y.reverse()
        posible_h.append("".join(y))
    return posible_h


def possible_lines():
    letters=get_letters()
    m=len(letters[0])
    n=len(letters)
    total=[]

    h=horizontal_lines(letters)
    v=vertical_lines(letters, m)

    
    total=h+v
    return total

def check_word(total,words):
    results={}
    for word in words:
        flag=False
        for p_word in total:
            word=str(word)

            if word in p_word:
                flag=True
                results[word]=flag
                
        if  flag == False:
            results[word]=flag
    return results

def write_json():
    global path_results
    results=check_word(possible_lines(),get_words())
    with open(path_results, "w") as f:
        json.dump(results, f, indent=4)
   
write_json()