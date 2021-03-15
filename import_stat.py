import statistics as s

dataValues = []
count = 0

while count < 6:
    data_input = input("Score: ")
    dataValues.append(int(data_input))
    count += 1

meanValue = s.mean(dataValues)
print("Mean:", meanValue)

medianValue = s.median(dataValues)
print("Median:", medianValue)

modeValue = s.mode(dataValues)
print("Mode:", modeValue)

sDeviation = s.stdev(dataValues)
print("Standard Deviation:", sDeviation)
