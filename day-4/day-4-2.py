from functools import partial
import re

def height_rule(height):
    if 'cm' in height:
        val = int(height.split('cm')[0])
        if val >= 150 and val <= 193:
            return 1
        else:
            return 0
    elif 'in' in height:
        val = int(height.split('in')[0])
        if val >= 59 and val <= 76:
            return 1
        else:
            return 0
    else:
        return 0

eye_colors_valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

rules = {
    'byr': (lambda a: 1 if len(a) == 4 and int(a) >= 1920 and int(a) <= 2002 else 0),
    'iyr': (lambda a: 1 if len(a) == 4 and int(a) >= 2010 and int(a) <= 2020 else 0),
    'eyr': (lambda a: 1 if len(a) == 4 and int(a) >= 2020 and int(a) <= 2030 else 0),
    'hgt': partial(height_rule),
    'hcl': (lambda a: 1 if a[0] == '#' and re.match("^[a-f0-9]*$", a.split('#')[1]) else 0),
    'ecl': (lambda a: 1 if a in eye_colors_valid else 0),
    'pid': (lambda a: 1 if len(a) == 9 else 0)
}

def field_validator(fields):
    for f in fields.split(' '):
        if len(f) > 0:
            key = f.split(':')[0]
            value = f.split(':')[1]
            
            if key == 'cid':
                continue
            if rules[key](value) == 1:
                continue
            else:
                return 0
    return 1


def process_data(data):
    metrics = data.split(' ')
    if data.count(':') == 8:
        return field_validator(data)
    elif data.count(':') == 7:
        if 'cid' in data:
            return 0
        else:
            return field_validator(data)
    else:
        return 0


valid_pw = 0

with open('../inputs/day-4.txt') as f:
    data = ''
    counter = 0
    for line in f:
        if line.strip().split('\n')[0] == '':
            valid_pw += process_data(data)
            data = ''
            continue
        data += line.replace('\n', ' ')
        
print(valid_pw)