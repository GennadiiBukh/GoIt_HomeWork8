from datetime import datetime, date, timedelta

employees = [{'name':'Іван', 'birthday':'1994-08-01'}, 
             {'name':'Олег', 'birthday':'1995-08-02'},
             {'name':'Ганна', 'birthday':'1996-07-27'},
             {'name':'Андрій', 'birthday':'1999-01-17'},
             {'name':'Олександр', 'birthday':'2000-10-09'},
             {'name':'Сергій', 'birthday':'2003-08-05'},
             {'name':'Аліна', 'birthday':'2004-07-29'},
             {'name':'Людмила', 'birthday':'2001-07-30'}]

def get_birthdays_per_week(users):

    days_name = {
    0: "понеділок",
    1: "вівторок",
    2: "середа",
    3: "четвер",
    4: "п'ятниця",
    5: "субота",
    6: "неділя",
    }

    current_date = date.today()

    if current_date.weekday() == 0:
        current_date = current_date - timedelta(days=2)

    one_week = timedelta(days=6)
    one_week_later = current_date + one_week

    print(f'Поздоровити іменинників від {current_date} до {one_week_later}\n')

    to_congrat = {i:[] for i in range(0,6)}

    for user in users:
          
        birthdate_this_year = date.fromisoformat(user['birthday']).replace(year=current_date.year) # Встановлюємо ДН у поточному році 
        day_of_week = None
           
        if current_date <= birthdate_this_year <= one_week_later: # Перевіряємо чи припадає ДН на сьогодні чи тиждень від сьогодні
           day_of_week = birthdate_this_year.weekday() # Отримуємо день тижня коли буде ДН
           if day_of_week in [5,6]:    # Якщо ДН у вихідний - поздоровляємо у понеділок
               day_of_week = 0
        else:
            continue
        for day, name in to_congrat.items(): # Формуємо списки поздоровлень по днях
            if day == day_of_week:
                to_congrat[day].append(user['name'])

    for day, names in to_congrat.items(): # Друкуємо списки на поздоровлення по наступних днях
        if names:
            names_str = ', '.join(names)
            print(f'{days_name[day]:<10}: {names_str}')

get_birthdays_per_week(employees)
