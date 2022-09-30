def notass(*n,sit=False):
    menor=(min(n))
    maior=(max(n))
    media = (sum(n)/len(n))
    dic = {}
    dic['maior']=maior
    dic['menor']=menor
    dic['media']=media
    if sit:
        if media >= 6:
            dic['sit'] = "Boa"
        if media < 6:
            dic['sit'] = 'Ruim'
    return dic






resp = notass(6,6,6,sit=True)
print(resp)