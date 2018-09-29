"""""
Determine if a set of brackets are ballanced


input:
7
{x[abc(1)]}
{[(])}
{{[[(())]]}}
{{[([(())])]}}
{[]([])}
))))
((((

output:
YES
NO
YES
YES

Notes:
    - unmatched close bracket == False
    - can start another bracket if others are not balanced
    - 
    
{ [ ( ] ) }
    
    
"""""




def is_matched(expression):
    brackets = {'()': 0, '[]': 0, '{}': 0}
    mystack = []
    for item in expression:
        for key in brackets:
            if item == key[0]:
                # New open item - push to stack
                mystack.append(key)
            if item == key[1]:
                # close bracket here - check last stack entry
                if len(mystack) > 0:
                    if item in mystack[len(mystack)-1]:
                        mystack.pop()
                    else:
                        # trying to close the wrong type of bracket
                        #print item, mystack[len(mystack)-1]
                        return False
                else:
                    # nothing to close
                    #print item, "no match"
                    return False
            pass
        pass
    pass
    #print expression
    if len(mystack) > 0:
        return False
    else:
        return True


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
