txt='abcabcdabcdeabcdefabcdefg'
vowels='ioaeu'
i=0
count=0
new_str=''
while i<len(txt):
    ch = txt[i]
    new_str+=ch
    count+=1

    if count ==3  and i!=len(txt)-1:
        if ch in vowels and i+1<len(txt):
                i+=1
                new_str+=txt[i+1]+"_"

        else:
            new_str+='_'
        count=0

    i+=1  
        
print(new_str)      