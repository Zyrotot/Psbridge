from timeit import default_timer as timer

def achaNumero(numero):
    start = timer()
    count = 2
    while True:
        result = str(numero*count)
        verification = set()
        for digito in result:
            if digito.isnumeric():
                verification.add(digito)
        if len(verification) < 3:
            break
        else:
            count = count +1
    end = timer()
    elapsed = end - start

    response = {}
    response['result'] = result
    response['elapsed'] = elapsed

    return response