#حدس اعداد بین1تا20
#معبن عسکرپور پروژه پایانی
import random

mlist = []

def start():
    attempts = 0
    randoma = random.randint(1, 20)
    print('سلام در این بازی باید عددی که من انتخاب کردم بین1تا20حدس بزنی!!!')
    player = input('نام بازیکن? ')
    ifplay = input(
        f' {player}, آیا مایل به بازی کردن هستی ? (بله/خیر): ')
#شرط شروع بازی انتخاب بله توسط کاربر

    if ifplay.lower() != 'بله':

        exit()


    while ifplay.lower() == 'بله':
        try:
#وارد کردن عدد بین1تا20توسط کاربر
            ply = int(input('یک عدد بین 1تا20انتخاب کنید: '))
            if ply < 1 or ply > 20:
#وارد کردن عدد خارج از محدوده
                raise ValueError(
                    'عددی بین1تا20انتخاب کنید!!')

            attempts += 1
            mlist.append(attempts)
#شرط برنده شدن
            if ply == randoma:
                print('درست حدس زدی!آفرین')
                print(f' تعداد تلاش های شما{attempts} تلاش ')
                ifplay = input(
                     f' {player}, آیا مایل به ادامه بازی  هستی ? (بله/خیر): ' )
                if ifplay.lower() != 'بله':

                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 20)

                    continue
            else:
#کوچکتر یا بزرگتر بودن عدد

                if ply > randoma:
                    print('عدد کوچکتر است')
                elif ply < randoma:
                    print('عدد بزرگتر است')
        except ValueError as err:
            print(err)

if __name__ == '__main__':
    start()