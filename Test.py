baza_dannych = {
    'LOL': 'odpowiedź na coś zabawnego',
    'CRINGE': 'coś dziwnego lub wstydliwego',
    'ROFL': 'odpowiedź na żart',
    'SHEESH': 'lekka dezaprobata',
    'CREEPY': 'straszny, złowieszczy',
    'AGGRO': 'stać się agresywnym/zły'
}
print('Wsztkie slowa', baza_dannych)

slowo = input('Napisz slowo ktore zmeiniemy')

if slowo in baza_dannych:
    new_value = input('Podaj nowe slowo:')
    baza_dannych [slowo] = new_value
    print('zaktualizowana baza dannych: ', baza_dannych)
