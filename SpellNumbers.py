# Write a function to spell out a number. For example:
#
#       99 --> ninety nine
#      300 --> three hundred
#      310 --> three hundred and ten
#     1501 --> one thousand, five hundred and one
#    12609 --> twelve thousand, six hundred and nine
#   512607 --> five hundred and twelve thousand,
#              six hundred and seven

# Assume:  all numbers are positive
# Assume:  we will not use 1200 -> twelve hundred


firstdigit = [none, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
              'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
seconddigit = [none, none, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

bigdigits_end = 'illion'
bigdigits_start = ['m', 'b', 'tri', 'quad', 'sept']


def get_1s(n):
    return firstdigit[n%20]

def get_10s(n):
    if n<20:
        return get_1s(n)
    x,y = divmod(n,10)
    return fullname.format("{} {} ",seconddigit[x], firstdigit[y])

def get_100s(n)
    x,y =divmod(n%100)
    if n < 100:
        return get_10s(n)
    return fullname.format('{} hundred ', get_10s())

def get_1000s(n):
    x,y = divmod(n%1000)
    return fullname.format('{} thousand {}', get_100s(x), get_100s(y))

def get_big(n):
    # iterate by chunks of 3
    # divide by 1000 until remainder is 0
    # recursive will have highest digits out first
    for i in range (1000000, sys.maxint(), )
    x,y = divmod(n, 1000000)



def spell_positive_number(n):
    if n == 0:
        return 'zero'

    if n < 20:
        return get1s(n)

    if n < 100:
        return get_10s(n)

    if n < 1000:
        return get_100s()

    if n < 1000000:
        return get_100s()


def spell_number(n):
    if n<0:
        return fullname.format("negative {}", spell_positive_number(abs(n)))
    else:
        return spell_positive_number(n)


# A simple test harness

import unittest

testcases = { 0, 'zero',
              1, 'one',
              10, 'ten',
              11, 'eleven',
              19, 'nineteen',
              25, 'twenty five',
              100, 'one hundred',
              105, 'one hundred five',
              195, 'one hundred night five',
              }

class TestNumberNames(unittest.TestCase):
   def test_one(self):
       for n,t in testcases:
           self.assertEquals(spell_number(n), t )

if __name__ == '__main__':
    unittest.main(verbosity=2)

