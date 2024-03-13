from models import TaksoPark,UserAccount,DriverAccount,Car

class Menu:

    driver = DriverAccount(
        name='toylep',
        last_name='toylep',
        age=20,
        gender='male',
        rating=4.5,
        age_of_work=2,
    )

    user_list = [
        UserAccount(
            name='toylep',
            last_name='toylep',
            age=20,
            gender='male',
            balance=10000,
            bonuses = 0
        )
    ]
#int,str,dict,list

    park = TaksoPark(
        car_list=[
            Car(
            mark='Renault',
            model='Duster',
            milliage=50000,
            color='white',
            driver=driver
            ),
            Car(
                mark='Mitsubisi',
                model='Lancer',
                milliage=60000,
                color='black',
                driver=driver
            )
        ],
        user_list=user_list
    )

    def start_menu(self):
        print("Выберите машину")
        print(self.park.car_list)

if __name__ == '__main__':
    Menu().start_menu()
    