class Item:
    # attribute

    #constructor

    def __init__(self, name, category, price, count=1):
        self.name = name
        self.count = count
        self.category = category
        self.price = price
    
    # properties
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value:
            if isinstance(value, str):
                if value.isalpha():
                    self.__name = value
                else:
                    raise ValueError("name must be alphabet.")
            else:
                raise TypeError("name must be str data type.")
        else:
            raise ValueError("name cannot be empty.")

    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, value):
        raise BaseException("setter is not implemented in Item class.")
        pass

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value:
            if isinstance(value, str):
                if value.isalpha():
                    self.__category = value.upper()
                else:
                    raise ValueError("category must be alphabet.")
            else:
                raise TypeError("category must be str data type.")
        else:
            raise ValueError("category cannot be empty.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value:
            if isinstance(value, int) or isinstance(value, float):
                self.__price = value * self.count
            else:
                raise TypeError("price must be int or float data type.")
        else:
            raise ValueError("price cannot be empty.")
    # method

    # casting
    def __str__(self):
        return '{{name= {}, count= {}, price={} }}'.format(self.name, self.count,  self.price)
    
    def __int__(self):
        return int(self._count)
    
    def __float__(self):
        return float(self._count)

    # representation of an object
    def __repr__(self):
        return '{{name= {}, count= {}, price={}}}'.format(self.name, self.count,  self.price)


class ContinuousItem(Item):

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if count:
            if isinstance(count, float):
                self._count = count
            else:
                raise ValueError("count must be float data type. ")
        else:
            raise ValueError("count cannot be empty.")

    # magic method
    def __add__(self, other):
        if isinstance(other, float):
            total = self._count + other
            self._count = total
            return total
        else:
            raise TypeError("in ContinuousItem class count should be float type.")

    def __iadd__(self, other):
        if isinstance(other, float):
            self._count = self._count + other
            return self
        else:
            raise TypeError("in ContinuousItem class count should be float type.")


class DiscreteItem(Item):
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if count:
            if isinstance(count, int):
                self._count = count
            else:
                raise ValueError("count must be int data type.")
        else:
            raise ValueError("count cannot be empty.")

    def __add__(self, other):
        if isinstance(other, int):
            total = self._count + other
            self._count = total
            return total
        else:
            raise TypeError("in DiscreteItem class count should be int type.")

    def __iadd__(self, other):
        if isinstance(other, int):
            self._count = self._count + other
            return self
        else:
            raise TypeError("in DiscreteItem class count should be int type.")


class Items:
    def __init__(self, parent):
        if isinstance(parent, User):
            self.__parent = parent
        else:
            raise TypeError("only User class is accepted as parent.")
        self.__items = dict()

    def add(self, item):
        if item:
            if isinstance(item, ContinuousItem) or isinstance(item, DiscreteItem):
                category = item.category
                temp_items = set()
                if self.__items.get(category):
                    temp_items = set(self.__items.get(category))
                temp_items.add(item)
                self.__items[category] = temp_items
                file = File(self.__parent.username)
                file.store(item)
            else:
                raise ValueError("input must be ContinuousItem or DiscreteItem class.")
        else:
            raise ValueError("item cannot be empty.")

    def show(self):
        return self.__items

    def __iter__(self):
        yield from self.__items
    
    def __contains__(self, item):
        temp_items = self.__items.get(item.category)
        for i in temp_items:
            if item.name == i.name and item.count == i.count:
                return True
        return False

    def __add__(self, other):
        self.add(other)
        return self
    
    def __len__(self):
        return len(self.__items)

    def __str__(self):
        string = str()

        for key, value in self.__items.items():
            string += str("Category {}: \n").format(key) + str(value) + "\n"
        return string


class User:
    def __init__(self, username, password, first_name, last_name) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.__items = Items(self)
        self.is_login = False

    @property
    def is_login(self):
        return self.__is_login

    @is_login.setter
    def is_login(self, value):
        if isinstance(value, bool):
            self.__is_login = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value:
            if isinstance(value, str):
                self.__username = value
            else:
                raise TypeError("username must be string")
        else:
            raise ValueError("please correct username")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if value:
            if isinstance(value, str):
                if len(value) > 5:
                    if value.isalnum():
                        self.__password = value
                    else:
                        raise ValueError("password must be contain letter and numbers")
                else:
                    raise ValueError("password length must be greater than 5 characters")
            else:
                raise TypeError("password must be string")
        else:
            raise ValueError("please correct password")

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value:
            if isinstance(value, str):
                self.__first_name = value
            else:
                raise TypeError("__first_name must be string")
        else:
            raise ValueError("please correct __first_name")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value:
            if isinstance(value, str):
                self.__last_name = value
            else:
                raise TypeError("last_name must be string")
        else:
            raise ValueError("please correct last_name")

    @property
    def items(self):
        if not self.__is_login:
            raise AttributeError("user is not login. you cannot see its items")
        return self.__items


class UsersManager:
    def __init__(self) -> None:
        self.__users = dict()

    def add_user(self, user):
        if isinstance(user, User):
            self.__users[user.username] = user
        else:
            raise TypeError("only user objects could be add")

    def login(self, username, password) -> User:
        if username and password:
            if isinstance(username, str):
                if self.__users.get(username):
                    user = self.__users.get(username)
                    if user.password == password:
                        user.is_login = True
                        return user
                    else:
                        raise ValueError("username or password is wrong.")

                else:
                    raise ValueError("username is not exist")
            else:
                raise ValueError("please enter correct username and password")
        else:
            raise ValueError("please enter correct username and password")


class File:
    def __init__(self, file_name) -> None:
        if not file_name:
            raise ValueError("enter correct filename")
        self.__file = open(file_name, "a+")

    def store(self, item):
        # file_content = self.__file.read()
        # if category in file_content:
        #     self.__file.seek(file_content.index(category))
        #     print(self.__file.readline())
        # else:
        #     self.__file.write("")
        self.__file.write(item.category + ";\n" + item.name + ", " + str(item.price) + ", " + str(item.count) + "\n")

    def __del__(self):
        self.__file.close()
