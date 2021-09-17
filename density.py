ólom= 18
réz=23
ólom_s=11.34
réz_s=8.69
ó_súly=ólom*ólom_s
r_súly=réz*réz_s
if ó_súly>r_súly:
    print('az ólom nehezebb')
elif ó_súly==r_súly:
    print('egyenlők')
else:
    print('a réz nehezebb')