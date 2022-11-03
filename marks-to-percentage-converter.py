print("welcome to marks to percentage converter\n")

Subjects = int(input("enter your no. of subjects: "))

totalOfEachPaper = int(input("enter the total mark of one single paper: "))

total = totalOfEachPaper * Subjects

marklst = []

for i in range(Subjects):
    i+=1
    mark = int(input(f"Enter your mark of subject {i}: "))
    marklst.append(mark)

yourTotal = sum(marklst)
print(f"your total mark is {yourTotal}")

percentage= yourTotal / total * 100
print(f"your percentage is {percentage}")