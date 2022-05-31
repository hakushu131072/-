import sys, datetime

def 入力を取得(msg):
    while 1:
        try:
            x = int(input(msg))
        except Exception as e:
            print(e)
            print('半角数字で入力してください')
            continue
        break
    return x

#def ミス():
#    if x = "m":

if __name__ == '__main__':
    date = datetime.date.today()
    回線数 = 入力を取得('何回線?') #1
    期間 = 入力を取得('何ヶ月?') #2
    月額 = 入力を取得('月額料金は？') * 期間 * 回線数 #3
    端末 = 入力を取得('端末価格は？') * 回線数 #4
    mnp = 入力を取得('mnp弾の費用はいくら？') * 回線数 #5
    事務 = 入力を取得('事務手数料は？') * 回線数 #6
    給料 = 入力を取得('給料はいくら渡しますか？') #7
    諸費 = 入力を取得('諸費用はありますか？') #8
    print(f'月額合算= {月額},端末合算= {端末},給料= {給料},mnp= {mnp},諸費= {諸費}, 事務手数料= {事務}') 
    維持 = mnp + 事務 + 月額
    費用 = 月額 + 端末 + 給料 + mnp + 事務

    print(f'費用は{費用},維持費用は{維持}')
    f_output = open('ttt.txt', 'a') 
    print(date, 維持, 費用, file=f_output)
    f_output.close ()
