card_stock, move_turn = map(int, input().split())

point_stock = 0
for i in range(move_turn):
    fee = int(input())
    if point_stock >= fee:
        point_stock -= fee
    else:
        card_stock -= fee
        point_stock += int(fee/10)
    print(card_stock, point_stock)
