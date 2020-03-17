import datetime


def earliest_possible(date):
    lst_date = [int(date_string) for date_string in date.split('/')]

    for year in lst_date:
        if len(str(year)) == 4:
            lst_date.remove(year)
            day, month = lst_date
            if month > 12:
                day, month = month, day
            try:
                date_result = datetime.datetime(year, month, day)
            except ValueError:
                return f'{year}/{month}/{day} illegal'
            else:
                return date_result.strftime('%Y-%m-%d')

        elif year == 0:
            lst_date.remove(year)
            year = 2000
            day, month = lst_date
            if month > 12:
                day, month = month, day
            try:
                date_result = datetime.datetime(year, month, day)
            except ValueError:
                return f'{year}/{month}/{day} illegal'
            else:
                return date_result.strftime('%Y-%m-%d')

    dates = []
    for x in range(3):
        new_date = lst_date[x:] + lst_date[:x]
        year = int('2' + (str(new_date[0]).rjust(3, '0')))
        day, month = new_date[1:]
        try:
            datetime.datetime(year, month, day)
        except ValueError:
            pass
        else:
            date1 = datetime.datetime(year, month, day)
            dates.append(date1)

        day, month = new_date[1:][::-1]
        try:
            datetime.datetime(year, month, day)
        except ValueError:
            pass
        else:
            date2 = datetime.datetime(year, month, day)
            dates.append(date2)

    return min(dates).strftime('%Y-%m-%d') if dates else f'{date} illegal'


def main():
    with open('input.txt') as f:
        for line in f:
            print(earliest_possible(line.rstrip()))


if __name__ == "__main__":
    main()
