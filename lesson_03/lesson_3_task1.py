class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullName = f"{self.first_name} {self.last_name}"

    def print_first_name(self):
        print(f'Меня зовут: {self.first_name}')

    def print_Last_name(self):
        print(f'Моя фамилия: {self.last_name}')


    def print_fullName(self):
        print(f'Мои имя и фамилия: {self.fullName}')
