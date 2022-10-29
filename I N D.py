#Пер Об Разн

if __name__ == '__main__':
    b = input('b = ')
    c = input('c = ')
    g = input('g = ')
    I = input('I = ')
    w = input('w = ')
    e = input('e = ')
    h = input('h = ')
    q = input('q = ')
    d = input('d = ')
    k = input('k = ')
    l = input('l = ')
    y = input('y = ')
    a = input('a = ')
    u = input('u = ')
    v = input('v = ')
    z = input('z = ')


    mn_a = {b, c, g, I, w}
    mn_b = {e, g, h, q, w}
    mn_c = {c, d, k, l, y}
    mn_d = {a, g, h, u, v, z}
    mn_u = set("abcdefghijklmnopqrstuvwxyz")
    a = mn_u.difference(mn_a)
    print('Множество A = ', mn_a)
    print('Множество B = ', mn_b)
    print('Множество C = ', mn_c)
    print('Множество D = ', mn_d)

    mn_x = (mn_a.intersection(mn_c)).union(mn_b)
    print('\nМножество X = ', mn_x)

    mn_y =(a.intersection(mn_d)).union(mn_c.difference(mn_b))
    print('Множество Y = ', mn_y)
