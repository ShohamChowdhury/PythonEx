list3 = [1,2,[3,4,"hello"]]
list3[2][2] = "goodbye"
print(list3)

d1 = {'simple_key':'hello1'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello2'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello3']]}]}
print(d3['k1'][0]['nest_key'][1][0])

d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello4']]}]}]}
print(d4['k1'][2]['k2'][1]['tough'][2][0])

list5 =[1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))