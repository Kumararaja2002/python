# count = 0
# a = 'cat'
# b = 'act'
# for i in a:
#     if(i in b):
#         count+=1
# if count == (len(a) and len(b)):
#     print('anagram')
# else:
#     print('not an anagram')

        
                
a = 'cat'
b = 'actt'
if(''.join(sorted(a)) == ''.join(sorted(b))):
    print("anagram")
else:
    print("not an anagram")
    

    
   