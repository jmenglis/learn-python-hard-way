def send_numbers(num):
    i = 0
    numbers = []
    """This is function that takes the variable num"""
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num


send_numbers(15000)