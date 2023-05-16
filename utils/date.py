from utils import jalali

def date2jalali(inp):
    date = f"{inp.year},{inp.month},{inp.day}"
    time = f"{inp.hour}:{inp.minute}"
    persian = jalali.Gregorian(date).persian_tuple()
    output = f"{persian[0]}/{persian[1]}/{persian[2]}، ساعت {time}"
    return output