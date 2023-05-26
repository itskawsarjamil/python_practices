# class A:
#     def one(self):
#         return self.two()
#     def two(self):
#         return 'A'

# class B:
#     def two(self):
#         return 'B'

# obj=B()

# print(obj.two())


# class A:
#     def test(self):
#         print("Test of A is called ",end="")
# class B(A):
#     def test(self):
#         print("Test of B is called ",end="")
#         super().test()
# class C(A):
#     def test(self):
#         print("Test of C is called ",end="")
#         super().test()
# class D(B,C):
#     def test2(self):
#         print("Test of D is called ",end="")
# obj=D()
# obj.test()

# apple = mango


# class A:
#     def __init__(self) -> None:
#         self.multiply(15)
#         print(self.i)
#     def multiply(self,i):
#         self.i=4*i
# class B(A):
#     def __init__(self) -> None:
#         super().__init__()
#     def multiply(self, i):
#         self.i=2*i
# obj=B()

