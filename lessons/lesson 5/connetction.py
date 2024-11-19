def check_connection(username, count_tries, priority):
    if priority >= 10:
        finish = 5
        for attemt in range(1, count_tries + 1):
            if attemt == finish:
                print("Connection was sucsessful!")
                break
            print(f"Attemt: {attemt} to connect to {username}")
    elif priority >= 5 and priority < 10:
        finish = 3
        for attemt in range(1, 6):
            if attemt == finish:
                print("Connection was sucsessful!")
            print(f"Attemt: {attemt} to connect to {username}")
    else:
        print("Your username has so low priority")


check_connection(count_tries=10, username="Oleg", priority=2)
