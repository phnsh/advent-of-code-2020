# def empty_array(arr):
# 	if 

def process_data(data):
    # required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    if data.count(':') == 8:
        # print("valid")
        return 1
    elif data.count(':') == 7:
        if 'cid' in data:
            # print("invalid")
            return 0
        else:
            # print("valid")
            return 1
    else:
        # print("invalid")
        return 0


valid_pw = 0
with open('../inputs/day-4.txt') as f:
    data = ''
    counter = 0
    for line in f:
        # print(line.strip().split('\n'))
        if line.strip().split('\n')[0] == '':
            valid_pw += process_data(data)
            data = ''
            continue
        data += line.strip().split('\n')[0] + '\n'
        
print(valid_pw)