
def is_buildin(func_str):
    try:
        eval(func_str)
        return True
    except NameError as ex:
        return False

#  def replace_str(my_string, span_as_tuple, replaced_word):
    #  string_as_list = list(my_string)
    #  string_as_list[span_as_tuple[0]:span_as_tuple[1]] = replaced_word
    #  replaced_string = ''.join(string_as_list)
    #  return replaced_string


def replace_str(my_string, spans, replaced_words):
    cursor = 0
    new_string = ''
    for span, word in zip(spans, replaced_words):
        prev_str = my_string[cursor:span[0]]
        next_str = my_string[span[0]:span[1]]
        new_string += prev_str + str(word)
        cursor = span[1]
    new_string += my_string[cursor:]
    return new_string


#  import regex
#  s = 'I---{am}={Kevin +=1 }Lee'
#  p = regex.compile('{.*?}')
#  groups = [m for m in p.finditer(s)]
#  spans = [list(g.span()) for g in groups]


#  s = "{200 * score // 4}, {title+' ABC'}"
#  spans = [[0, 18], [20, 34]]
#  values = [200, 'bonus ABC']
