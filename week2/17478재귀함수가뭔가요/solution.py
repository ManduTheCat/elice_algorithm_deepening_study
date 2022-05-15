def chatbot(num):
    global text1, text2, text3, text4, text5, text6, marks

    if num == 0:
        print(marks + text1 + '\n' + marks + text5 + '\n' + marks + text6)
        return

    # print("#### marks:", marks, "####")
    print(marks + text1 + '\n' + marks + text2
     + '\n' + marks + text3 + '\n' + marks + text4)

    marks += '____'
    # print("after plus marks:", marks)
    
    chatbot(num - 1)
    marks = marks[4:]
    # print("after minus marks:", marks)
    print(marks + text6)


n = int(input())

marks = ''

text1 = '"재귀함수가 뭔가요?"'
text2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
text3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
text4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

text5 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
text6 = '라고 답변하였지.'


print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
chatbot(n)