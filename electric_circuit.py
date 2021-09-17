max_t=25*230
izzó=5*30
klima=1500
mosógép=1200
össz_f=izzó+klima+mosógép
if össz_f+2000>max_t:
    print('lekapcsol a megszakitó')
else:
    print('elbirja')