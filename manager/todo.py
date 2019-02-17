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

    def __init__(self):
        self.__items = dict()

    def get_item(self, category, name):
        category = self.__items.get(category)
        if category:
            return [x for x in category if x.name == name]

    def add(self, item):
        if item:
            if isinstance(item, ContinuousItem) or isinstance(item, DiscreteItem):
                category = item.category
                temp_items = list()
                if self.__items.get(category):
                    temp_items = self.__items.get(category)
                # temp_item = self.get_item(item.category, item.name)
                # if temp_item:
                #     temp_item.count = temp_item.count + item.count
                # else:
                temp_items.append(item)
                self.__items[category] = temp_items

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
            if item.name == i.name:
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
    def __init__(self, username, password, first_name, last_name, storage_mode="MEMORY") -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.__items = Items()
        self.is_login = False
        self.__storage_manager = StorageManager(self, storage_mode)

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
        return self.__storage_manager.get_items()

    def set_storage(self, storage_mod):
        self.__storage_manager = StorageManager(storage_mod, self.username)

    def add_item(self, item):
        if item:
            if isinstance(item, ContinuousItem) or isinstance(item, DiscreteItem):
                self.__storage_manager.store(item)


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
    MODES = ["r", "w", "a+", "w+"]

    def __init__(self, file_name, mode="r") -> None:
        from pathlib import Path
        if not file_name:
            raise ValueError("enter correct filename")
        if mode not in File.MODES:
            raise ValueError("file mode is incorrect.")
        file = Path("/path/to/file")
        if not file.is_file():
            self.__file = open(file_name, "a+")
            self.__file.close()
        self.__file = open(file_name, mode)

    def store(self, item):
        item_type = "DISCRETE"
        if isinstance(item, ContinuousItem):
            item_type = "CONTINUOUS"

        self.__file.write(item.name + "," + item.category + "," + str(item.price) + ","
                          + str(item.count) + "," + item_type + ";")

    def read_items(self):
        content = self.__file.read()
        return content

    def __del__(self):
        self.__file.close()

    def close_file(self):
        self.__file.close()

    def change_mode(self, mode="r"):
        if mode not in File.MODES:
            raise ValueError("file mode is incorrect.")
        self.__file.mode = mode


class Database:
    def __init__(self):
        import sqlalchemy
        print("SQLALCHEMY VERSION IS: " + sqlalchemy.__version__)


class StorageManager:

    STORAGE_MODES = ["MEMORY", "FILE", "DATABASE"]

    def __init__(self, parent, storage_mode="MEMORY"):
        self.mode = storage_mode
        if self.mode == "MEMORY":
            self.__items = Items()
        else:
            if isinstance(parent, User):
                self.__parent = parent

    def store(self, item):
        if self.__mode == "FILE":
            storage = File(self.__parent.username, "a+")
            storage.store(item)
            storage.close_file()
        elif self.__mode == "DATABASE":
            storage = Database()
            # TODO Implement database class
        else:
            self.__items.add(item)

    def get_items(self):
        if self.__mode == "FILE":
            storage = File(self.__parent.username, "r")
            data = storage.read_items().split(";")
            items = Items()
            for line in data:
                line = line.split(",")
                if len(line) < 4:
                    return items
                    # raise ValueError("the file has wrong format")
                if line[4] == "CONTINUOUS":
                    item = ContinuousItem(str(line[0]), str(line[1]), float(line[2]), float(line[3]))
                    items.add(item)
                else:
                    item = DiscreteItem(str(line[0]), str(line[1]), float(line[2]), int(line[3]))
                    items.add(item)

            storage.close_file()
            return items
        elif self.__mode == "DATABASE":
            storage = Database()
            # TODO Implement database class
        else:
            return self.__items

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        if value in StorageManager.STORAGE_MODES:
            self.__mode = value
        else:
            raise TypeError("storage mode is invalid")

