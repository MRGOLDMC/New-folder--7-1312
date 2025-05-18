def ontime(n):
    iternation = 0
    for i in range(1, n + 1):
        iternation += 1
    print("When n is", n, "the iteration is", iternation)

ontime(10)
ontime(20)
ontime(30)
print("\nWith every 'n' the time taken and iterations will increase.")

