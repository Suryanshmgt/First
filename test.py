file = open("ques.txt", "r")
file2 = open("ans.txt", "r")
ques = file.readlines()
cnt = 0
marks = 0

for i in range(0, len(ques)):
    print(ques[i])
    cnt += 1
    if cnt == 5:
        print('Enter your answer')
        userAns = input()
        userAns = userAns.upper()
        # fetching first char from answers
        correctAns = file2.readline()[0]

        if correctAns == userAns:
            print('\nCorrect answer\n')
            marks += 2
        else:
            print('\nWrong answer\n')

        cnt = 0

file2.seek(0)
answers = file2.readlines()

file.close()
file2.close()

print('Your score is: ', marks)
print('Correct answer as follows:')
for e in answers:
    print(e)