class A:
    def b(self, data):
        self.b(data, 'hehe')

    def b(self, data, param):
        print data
        print param

if __name__ == "__main__":
    obj = A()
    obj.b("data")
    obj.b("data", "cust")
