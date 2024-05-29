intrebari={
    'cum te cheama?':'A',
    'o intrabare utila?':'C',
    'te descurci la dormit?':'D',
    'nu mai am inspiratie':'B',
}
optiuni=[
    ['A. pe nume','B. nu ma cheama','C. drq stie','D. da'],
    ['A. poate', 'B. eu nu stie sa cisteste', 'C. da,foarte!', 'D. depinde de zodie'],
    ['A. doar dorm', 'B. nush, nu tin minte', 'C. ce e ala dormit?', 'D. fara tine, forte greu'],
    ['A. bine', 'B. se vede', 'C. ma omor', 'D. nu va omorati, copii']
]
i=0
a=[]
for key in intrebari:
    print(key)
    for x in optiuni[i]:
        print(x,end=' ')
    a.append(input(':'))
    i+=1
    print('\n ------------------ \n')
corecte=0
i=0
for x in intrebari:
    if intrebari[x]==a[i]:
        corecte+=1
    i+=1
print(corecte/4)