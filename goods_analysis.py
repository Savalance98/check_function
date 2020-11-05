def goods_analysis(*l, in_sale=None):
    p = []
    for i in l:
        if in_sale is not None:
            if in_sale(i):
                p.append(i)
        elif 'молоко' in i['название'].lower():
            p.append(i)
    p.sort(key=lambda i: i['цена'])
    return p[2], p[1], p[0]
