''' Do:
-- Read from 'mountain.txt'
-- Change 'McKinley' to 'Denali'
-- Write to 'denali.txt'
'''

with open('./Notes/Week07/mountain.txt', 'r') as mtn_in, open('./Notes/Week07/denali.txt', 'w') as mtn_out:
    line = mtn_in.readline()
#   while len(line) > 0:
#   while line != '':
#   while line:
#   while line = line.replace('McKinley', 'Denali')
#       mtn_out.write(line)
#       line = mtn_in.readline()

    for line in mtn_in:
        mtn_out.write(line.replace('McKinley', 'Denali'))
#   text = mtn_in.read()
#   mtn_out.write(text.replace('Mckinley', 'Denali'))