def count_bottle(count):
    remainder = count % 10
    if remainder == 1 and not count == 11:
        return f'{count} бутылка'
    elif remainder >= 2 and remainder <= 4 and not (count >= 12 and count <= 14):
        return f'{count} бутылки'
    else:
        return f'{count} бутылок'


def base():
    print(f'{count_bottle(N)} пива на стене')
    print(f'{count_bottle(N)} пива!')
    print('Возьми одну, пусти по кругу')
    if N == 1:
        final()
    else:
        print(f'{count_bottle(N - 1)} пива на стене!\n')


def final():
    print('Нет больше бутылок пива на стене!\n')
    print('Нет бутылок пива на стене!')
    print('Нет бутылок пива!')
    print('Пойди в магазин и купи ещё')
    print('99 бутылок пива на стене!')


for N in reversed(range(1, 100)):
    base()