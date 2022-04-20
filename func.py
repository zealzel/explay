
# define customed functions here. mainly for extension operation




def exp_gen_year(date_list, score_list, sort=True):
    from collections import Counter
    import json
    import pandas as pd
    if sort:
        date_list = sorted(date_list)
    count = Counter([e[0] for e in date_list])

    def is_this_year_first(each, array):
        more_than_once_this_year = Counter([e[0] for e in array])[each[0]] > 1
        this_year = each[0]
        before_this_year = [e[0] for e in array[:array.index(each)]]
        is_this_year_first = this_year not in before_this_year
        return is_this_year_first

    def format1(y_m_d, score, taiwan=False):
        y_m_d[0] = y_m_d[0] - 1911 if taiwan else y_m_d[0]
        additional = '(共%s件)' % score if score>1 else ''
        return '%d年%d月%d日%s' % tuple(y_m_d + [additional])

    def format2(y_m_d, score):
        additional = '(共%s件)' % score if score>1 else ''
        return '%d月%d日%s' % tuple(y_m_d[1:] + [additional])

    def get_date_score_list(date_list, score_list): # each day
        date_list_ = [json.dumps(l) for l in date_list]
        date_score = list(zip(date_list_, score_list))
        dd = pd.DataFrame(date_score)
        stat = dd.groupby(0, sort=False).agg({1:sum}).reset_index()
        stat.iloc[:,0] = stat.iloc[:,0].map(lambda x: json.loads(x))
        stat = stat.values.tolist()
        return stat

    date_score_list = get_date_score_list(date_list, score_list)
    date_list_stat = [y_m_d for y_m_d, score in date_score_list]
    this_year_first = [is_this_year_first(e, date_list_stat) for e in date_list_stat]
    split_index = [e[0] for e in filter(lambda x: x[1], enumerate(this_year_first))][-1]

    if split_index != 0:
        first_half = date_score_list[:split_index]
        second_half = date_score_list[split_index:]
        str1 = '、'.join([format1(e, score, True) if is_this_year_first(e, date_list) else format2(e, score) for e, score in first_half])
        str2 = '、'.join([format1(e, score, True) if is_this_year_first(e, date_list) else format2(e, score) for e, score in second_half])
        str_final = '%s及%s' % (str1, str2)
    else:
        str_final = '、'.join([format1(e, score, True) if is_this_year_first(e, date_list) else format2(e, score) for e, score in date_score_list])
    return str_final


def exp_each_award(date_minguo, content):
    verb = '發現' if content.startswith('小型動物') else '查核旅客' 
    words = f'{date_minguo}{verb}{content}'
    return words
