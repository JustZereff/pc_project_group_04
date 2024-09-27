def narcissistic( value ):
    if value<10:
        return True
    else:
        a=list(str(value))
        value_a=[int(b) for b in a]
        love=sum(c**len(a) for c in value_a )
        return love==value
    return False


print(narcissistic(372))