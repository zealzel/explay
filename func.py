
# define customed functions here. mainly for extension operation



def exp_concat_days(*days):
    try:
        pass
        #  days_str = ','.join(days)
        #  print(days_str)
    except Exception as ex:
        import pdb; pdb.set_trace()
        print("ERROR!")
        print(days)

    #  return days_str
    return list(days)


#  def exp_cal_night(night):
    #  import pdb; pdb.set_trace()
    #  print(night)



#  is_night = lambda schedules_of_this_code: len(list(filter(lambda e: '夜' in e, schedules_of_this_code)))
#  is_morning = lambda schedules_of_this_code: len(list(filter(lambda e: '早' in e, schedules_of_this_code)))
#  is_day = lambda schedules_of_this_code: len(list(filter(lambda e: '日' in e, schedules_of_this_code)))
#  is_small = lambda schedules_of_this_code: len(list(filter(lambda e: '小' in e, schedules_of_this_code)))

#  is_night = lambda schedules_of_this_code: all(['夜' in e for e in schedules_of_this_code])
#  is_small = lambda schedules_of_this_code: all(['小' in e for e in schedules_of_this_code])
#  is_morning = lambda schedules_of_this_code: all(['早' in e for e in schedules_of_this_code])
#  is_day = lambda schedules_of_this_code: all(['日' in e for e in schedules_of_this_code])

is_night = lambda schedules_of_this_code: any(['夜' in e for e in schedules_of_this_code[1]])
is_small = lambda schedules_of_this_code: any(['小' in e for e in schedules_of_this_code[1]])
is_morning = lambda schedules_of_this_code: any(['早' in e for e in schedules_of_this_code[1]])
is_day = lambda schedules_of_this_code: any(['日' in e for e in schedules_of_this_code[1]])


def exp_night_num(schedule_list):
    num_of_night = sum([is_night(n) for n in schedule_list])
    return num_of_night


def exp_morning_num(schedule_list):
    num_of_morning = sum([is_morning(n) for n in schedule_list])
    return num_of_morning


def exp_day_num(number, schedule_list):
    #  if number==986:
        #  sss = schedule_list
        #  import pdb; pdb.set_trace()
    num_of_day = sum([is_day(n) for n in schedule_list])
    return num_of_day


def exp_small_num(schedule_list):
    num_of_small = sum([is_small(n) for n in schedule_list])
    return num_of_small


def exp_sum_all(x, y, z, w):
    return sum([x, y, z, w])


def exp_trim_unit(unit):
    return unit[unit.find('中心')+2:]
