def run():
    menu = """
    -----------------------------------------------
    WELCOME TO WORLD CAPITALS IDENTIFICATOR

    Please choose an option (only the number): 

    1 - America (North and South)
    2 - Europe
    3 - Asia 
    4 - Oceania
    -----------------------------------------------
    """
    menu1 = """
    -----------------------------------------------
        YOU CHOOSE AMERICA, CHOOSE A COUNTRY PLEASE
    1 - Brasil
    2 - Argentina 
    3 - Perú 
    4 - Colombia
    5 - Chile
    6 - Venezuela
    7 - Ecuador 
    8 - Curazao
    9 - Aruba 
    10 - Uruguay 
    11 - Bolivia
    12 - Paraguay
    13 - United States
    -----------------------------------------------
    """
    menu2 = """
    -----------------------------------------------
        YOU CHOOSE EUROPE, CHOOSE A COUNTRY PLEASE
    1 - Germany
    2 - Italy 
    3 - France
    4 - United kingdom
    5 - Netherlands
    6 - Belgium
    7 - Greece
    8 - Ireland
    -----------------------------------------------
    """
    menu3 = """
    -----------------------------------------------
        YOU CHOOSE ASIA, CHOOSE A COUNTRY PLEASE
    1 - Japan
    2 - India
    3 - Indonesia
    4 - China
    5 - Thailand
    6 - South Korea
    7 - Philipines
    8 - Singapore
    -----------------------------------------------
    """
    menu4 = """
    -----------------------------------------------
        YOU CHOOSE OCEANIA, CHOOSE A COUNTRY PLEASE
    1 - New Zealand
    2 - Australia
    3 - FiJi
    4 - Samoa
    -----------------------------------------------
    """
    option = int(input(menu))
    def capital(country,capital):
            print('The capital of '+country+' is '+capital)

    if option == 1:
        option1 = int(input(menu1))
        if option1 == 1:
            capital('Brasil','Brasilia')
        elif option1 == 2:
            capital('Argentina','Buenos Aires')
        elif option1 == 3:
            capital('Perú','Lima')
        elif option1 == 4:
            capital('Colombia','Bogotá')
        elif option1 == 5:
            capital('Chile','Venezuela')
        elif option1 == 6:
            capital('Venezuela','Caracas')
        elif option1 == 7:
            capital('Ecuador','Quito')
        elif option1 == 8:
            capital('Curazao','Willemstad')
        elif option1 == 9:
            capital('Aruba','Oranjestad')
        elif option1 == 10:
            capital('Uruguay','Montevideo')
        elif option1 == 11:
            capital('Bolivia','Sucre')
        elif option1 == 12:
            capital('Paraguay','Asunción')
        elif option1 == 13:
            capital('united States','Washington')
        else:
            print('Choose a correct option please. ')
    if option == 2:
        option2 = int(input(menu2))
        if option2 == 1:
            capital('Germany','Berlín')
        elif option2 == 2:
            capital('Italy','Roma')
        elif option2 == 3:
            capital('France','París')
        elif option2 == 4:
            capital('United Kingdom','London')
        elif option2 == 5:
            capital('Netherlands','Amsterdam')
        elif option2 == 6:
            capital('Belgium','Bruselas')
        elif option2 == 7:
            capital('Greece','Athenas')
        elif option2 == 8:
            capital('Ireland','Dublin')
        else:
            print('Choose a correct answer please.')
    if option == 3:
        option3 = int(input(menu3))
        if option3 == 1:
            capital('Japan','Tokyo')
        elif option3 == 2:
            capital('India','New Dehli')
        elif option3 == 3:
            capital('Indonesia','Yakarta')
        elif option3 == 4:
            capital('China','Pekin')
        elif option3 == 5:
            capital('thailand','Bangkok')
        elif option3 == 6:
            capital('South Korea','Seul')
        elif option3 == 7:
            capital('Philipines','Manila')
        elif option3 == 8:
            capital('Singapore','Singapore')
        else:
            print('Choose a correct answer please.')    
    if option == 4:
        option4 = int(input(menu4))
        if option4 == 1:
            capital('New Zealand','Wellington')
        elif option4 ==  2:
            capital('Australia','Sidney')
        elif option4 ==  3:
            capital('Fiji','Suva')
        elif option4 ==  4:
            capital('Samoa','Apia')
        else:
            print('Choose a correct answer please.') 
    # else:
    #     print("""Please, Choose a correct option:
    #         1 - America (South and North)
    #         2 - Europe
    #         3 - Asia 
    #         4 - Oceania
    #         """)

if __name__=='__main__':
    run()