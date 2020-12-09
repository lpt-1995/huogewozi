import gift

'''from gift import have_gift
   展示礼物'''


def show():
    have_gift = gift.have_gift
    if have_gift == True:
        print("收到礼物")
    else:
        print("没有收到礼物")
