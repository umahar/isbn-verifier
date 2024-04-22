def is_valid(isbn):
    if len(str(isbn)) == 13 or len(str(isbn)) == 10:
        clean_isbn=str(isbn)
        if isbn[-1].isalpha():
            if isbn[-1]!='X':
                return False
            temp = isbn.replace("X","10")
            clean_isbn = temp.replace("-","")
            if not clean_isbn.isdigit():
                return False
            sum = 0
            count = 10
            for char in clean_isbn:
                if count ==1:                    
                    sum = sum + 10
                    break
                else:
                    sum = sum + (int(char)*count)
                    count-=1
            if (sum%11) == 0:
                return True
        sum = 0
        count = 10
        clean_isbn = clean_isbn.replace("-","")
        if not clean_isbn.isdigit():
            return False
        for char in clean_isbn:
            sum = sum + (int(char)*count)
            count-=1
        if (sum%11) == 0:
            return True
    return False



print(is_valid("3-598-21508-8"))