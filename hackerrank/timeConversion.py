import re
# Input examples string of hh:mm:ssAM or hh:mm:ssPM
def timeConversion(s):
    # Write your code here
    try:
        hour, minute, _ = s.split(":")
        second = re.findall(r'[0-9]+', _)[0]
        format = _[-2:]
        if format.lower() == "pm":
            if int(hour) == 12:
                return f'{int(hour)}:{minute}:{second}'
            return f'{int(hour)+12}:{minute}:{second}'
        if int(hour)==12 and format.lower()=="am":
            return f'0{int(hour)-12}:{minute}:{second}'

        return f'{hour}:{minute}:{second}'
    except:
        return print("Invalid time format, should be hh:mm:ssAM or hh:mm:ssPM")

print(timeConversion("12:05:45AM"))
print(timeConversion("04:59:59AM"))