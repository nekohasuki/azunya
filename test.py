import json
with open('cmds\\data\\test.json','r',encoding='utf8') as TestFile:
    test = json.load(TestFile)
a = 1
while a <10:
    b = 1
    while b <10:
        c = 1
        while c <10:
            d = 1
            while d <10:
                e = 1
                while e <10:
                    f = 1
                    while f <10:
                        g = 1
                        while g <10:
                            h = 1
                            while h <10:
                                i = 1
                                while i <10:
                                    j = 1
                                    while j <10:
                                        k = 1
                                        while k <10:
                                            l = 1
                                            while l <10:
                                                m = 1
                                                while m <10:
                                                    n = 1
                                                    while n <10:
                                                        o = 1
                                                        while o <10:
                                                            p = 1
                                                            while p <10:
                                                                q = 1
                                                                while q <10:
                                                                    r = 1
                                                                    while r <10:
                                                                        s = 1
                                                                        while s <10:
                                                                            t = 1
                                                                            while t <10:
                                                                                print(f'{a}x{b}x{c}x{d}x{e}x{f}x{g}x{h}x{i}x{j}x{k}x{l}x{m}x{n}x{o}x{p}x{q}x{r}x{s}x{t}={a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t}')
                                                                                update={f'{a}x{b}x{c}x{d}x{e}x{f}x{g}x{h}x{i}x{j}x{k}x{l}x{m}x{n}x{o}x{p}x{q}x{r}x{s}x{t}':f'{a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t}'}
                                                                                test.update(update)
                                                                                t += 1
                                                                                if t >10:
                                                                                    break
                                                                            s +=1
                                                                            if s >10:
                                                                                break
                                                                        r += 1
                                                                        if r >10:
                                                                            break
                                                                    q += 1
                                                                    if q >10:
                                                                        break
                                                                p += 1
                                                                if p >10:
                                                                    break
                                                            o += 1
                                                            if o >10:
                                                                break
                                                        n +=1
                                                        if n >10:
                                                            break
                                                    m += 1
                                                    if m >10:
                                                        break
                                                l += 1
                                                if l >10:
                                                    break
                                            k += 1
                                            if k >10:
                                                break
                                        j += 1
                                        if j >10:
                                            break
                                    i +=1
                                    if i >10:
                                        break
                                h += 1
                                if h >10:
                                    break
                            g += 1
                            if g >10:
                                break
                        f += 1
                        if f >10:
                            break
                    e += 1
                    if e >10:
                        break
                d +=1
                if d >10:
                    break
            c += 1
            if c >10:
                break
        b += 1
        if b >10:
            break
    a += 1
    if a >10:
        break
with open('cmds\\data\\test.json','w',encoding='utf8') as TestFile:
test = json.dump(test,TestFile,indent=4)

print("程式已執行完畢")