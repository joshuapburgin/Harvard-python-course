class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError("Wrong capacity")
        self._capacity=capacity
        self._size= 0


    def __str__(self):
            return self._size*"🍪"


    def deposit(self, amount_deposited):
        if (self._size+ amount_deposited )>self.capacity:
            raise ValueError("Exceeded capacity")
        self._size +=amount_deposited

    def withdraw(self, amount_withdrawn):
       if amount_withdrawn> self._size:
           raise ValueError("Too much withdrawn")
       self._size -= amount_withdrawn

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    capacity= int(input("Capacity: "))
    jar = Jar(capacity)

    deposit= int(input("Deposit: "))
    withdraw= int(input("Withdraw: "))

    jar.deposit(deposit)
    jar.withdraw(withdraw)

    print(jar)

if __name__ == "__main__":
    main()
