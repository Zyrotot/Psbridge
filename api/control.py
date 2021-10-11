def achaNumero(numero):
    count = 2
    while True:
        result = str(numero*count)
        verification = set()
        for digito in result:
            verification.add(digito)
        if len(verification) < 3:
            break
        else:
            count = count +1

    return result