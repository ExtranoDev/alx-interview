def pascal_triangle(n):
    DEF_V = 1
    if n <= 0:
        return []
    pas_tri = []
    for i in range(n):
        pas_tri.append([DEF_V])
        if len(pas_tri[i]) - DEF_V < i:
            if i == DEF_V:
                pas_tri[DEF_V].append(DEF_V)
            else:
                temp_tri = pas_tri[i - DEF_V][:]
                val = len(temp_tri) - DEF_V
                for x in range(val):
                    temp = temp_tri[x] + temp_tri[x + DEF_V]
                    pas_tri[i].append(temp)
                pas_tri[i].append(DEF_V)
    return pas_tri
