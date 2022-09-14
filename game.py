alpha = 'a,b,c,d,e,f,g,h,i'
a,b,c,d,e,f,g,h,i = alpha.split(',')
board = f'{a}|{b}|{c}\n{d}|{e}|{f}\n{g}|{h}|{i}'
used_lst = []


def tictac(board,alpha,a,b,c,d,e,f,g,h,i):
    print(board)
    for turn in range(1,11):
        if turn == 10:
            print("It's a TIE! Restart the game!")
            break
        else:
            turn = turn % 2
            player = ''
            if turn == 1:
                player = 'X'
            else:
                player = 'O'
            req_met = False
            while req_met != True:
                p = input(f'Player {player} select a letter which has not been used to replace with an "{player}": ')
                p = p.lower()
                if p.isalpha() and p in alpha and p not in used_lst:
                    if p == a:
                        used_lst.append(a)
                        a = f'{player}'
                    elif p == b:
                        used_lst.append(b)
                        b = f'{player}'
                    elif p == c:
                        used_lst.append(c)
                        c = f'{player}'
                    elif p == d:
                        used_lst.append(d)
                        d = f'{player}'
                    elif p == e:
                        used_lst.append(e)
                        e = f'{player}'
                    elif p == f:
                        used_lst.append(f)
                        f = f'{player}'
                    elif p == g:
                        used_lst.append(g)
                        g = f'{player}'
                    elif p == h:
                        used_lst.append(h)
                        h = f'{player}'
                    elif p == i:
                        used_lst.append(i)
                        i = f'{player}'
                    req_met = True
                    new_board = f'{a}|{b}|{c}\n{d}|{e}|{f}\n{g}|{h}|{i}'
                    print(new_board)
        if a == b and b == c:
            win_combo(a)
            break
        elif a == d and d == g:
            win_combo(a)
            break
        elif a == e and e == i:
            win_combo(a)
            break
        elif e == d and e == f:
            win_combo(e)
            break
        elif e == g and e == c:
            win_combo(e)
            break
        elif e == h and e == b:
            win_combo(e)
            break
        elif i == h and i == g:
            win_combo(i)
            break
        elif i == f and i == c:
            win_combo(i)
            break


def win_combo(z):
    print('Player', z.upper(), 'Won!')


tictac(board,alpha,a,b,c,d,e,f,g,h,i)
