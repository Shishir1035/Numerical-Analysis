hile True:
        check = f(deriE,a)
        while check == 0.0:
            a = float(input('Enter another initial value = '))
            check = f(deriE,a)

        newa = a - (f(E,a)/check)

        error = ((abs(newa-a)/newa)*100) 
        val = f(E,newa)
        table.add_row(["%.8"%newa, "%.8"%error, "%.8f"%val])
        cnt = cnt + 1

        if error < acerror:
            break