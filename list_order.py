
data_set_fruit = [
    'banana',
    'morango',
    'manga',
    'sapoti',
    'acelora',
    'caju'
]


if __name__ == '__main__' :
    items = [
        ['banana', 2, 1.58],
        ['morango', 2, 6.87],
        ['manga', 8, 1.50],
        ['sapoti', 1, 2.50],
        ['acelora', 2, 3.98],
        ['caju', 5, 0.60]
    ]

    imposto = 0
    result_total = 0
    print('-' * 36)
    print('%10s %4s %8s %10s' % ('Descricao', 'QTD', 'Preco', 'Total'))
    for e in items :
        result = e[1] * e[2]
        result_total += result
        print('%-10s %4d %8.2f %10.2f' % (e[0], e[1], e[2], result))
    
    imposto = result_total * 0.12
    
    print('-' * 36)
    print()
    print('-' * 36)
    print('%-24s %10.2f' % ('Imposto', imposto))
    print('%-24s %10.2f' % ('Total sem Imposto', result_total))
    print('%-24s %10.2f' % ('Total com imposto', result_total + imposto))
    print('-' * 36)

