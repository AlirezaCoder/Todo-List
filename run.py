from manager.todo import ContinuousItem, DiscreteItem, Items, User, UsersManager

user1 = User("ali", "123abc", "ali", "alavi")
user2 = User("hassan", "abc123", "hassan", "hassani", "FILE")
user_manger = UsersManager()
user_manger.add_user(user1)
user_manger.add_user(user2)



loggined_user = user_manger.login("ali", "123abc")
if isinstance(loggined_user, User):
    items = loggined_user.items
    # items.add(ContinuousItem('apple', "fruit", 100, 2.5))
    # items.add(ContinuousItem('orange', "fruit", 50, 3.5))

print("Here is user1 list: ")
# for item in items:
#     print(item)
print(items)

loggined_user = user_manger.login("hassan", "abc123")
if isinstance(loggined_user, User):
    items = loggined_user.items
    loggined_user.add_item(DiscreteItem('banana', "fruit", 500, 10))
    loggined_user.add_item(DiscreteItem('apple', "fruit", 80, 1))
    loggined_user.add_item(ContinuousItem('milk', "dairy", 80, float(50)))

    # items.add(DiscreteItem('banana', "fruit", 500, 10))
    # items.add(DiscreteItem('apple', "fruit", 80, 1))
    # items.add(ContinuousItem('milk', "dairy", 80, float(50)))
    # items.add(ContinuousItem('butter', "dairy", 200, 7.5))

print("Here is user2 list: ")
# for item in items:
#     print(item)
print(loggined_user.items)

# items = Items(user)
#
# items.add(ContinuousItem('apple', "fruit", 100, 2.5))
# items.add(ContinuousItem('orange', "fruit", 50, 3.5))
# items.add(DiscreteItem('banana', "fruit", 500, 10))
# items.add(DiscreteItem('apple', "fruit", 80, 1))
# items.add(ContinuousItem('milk', "dairy", 80, float(50)))
# items.add(ContinuousItem('butter', "dairy", 200, 7.5))



print("Here is your list: ")
# for item in items:
#     print(item)
print(items)