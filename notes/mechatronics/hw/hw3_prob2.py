def ADC_12(low, high, value):
    n = 12
    ran = high - low
    res = ran/(2**n)
    values = [low + i * res for i in range(2**n)]

    for i in range(2**n):
        if value < values[i]:
            print("\t{0:12b}".format(i-1), "\t", values[i-1])
            return

    print("\t{0:12b}".format(i), "\t", values[i])


def ADC_16(low, high, value):
    n = 16
    ran = high - low
    res = ran/(2**n)
    values = [low + i * res for i in range(2**n)]

    for i in range(2**n):
        if value < values[i]:
            print("\t{0:16b}".format(i-1), "\t", values[i-1])
            return

    print("\t{0:16b}".format(i), "\t", values[i])

low = -5
high = 5
# 12 bit
print("12-Bit")
ADC_12(low, high, -1.1)
ADC_12(low, high, -0.1)
ADC_12(low, high, 0.1)
ADC_12(low, high, 3.2)
ADC_12(low, high, 6.7)

# 16 bit
print("16-Bit")
ADC_16(low, high, -1.1)
ADC_16(low, high, -0.1)
ADC_16(low, high, 0.1)
ADC_16(low, high, 3.2)
ADC_16(low, high, 6.7)
