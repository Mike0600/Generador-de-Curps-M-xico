
import random
import re


apellido = 'Acosta,Acuña,Aguilar,Becerril,Cervantes,Céspedes,Cevallos,Gaitán,Galán,Galeano,Jaramillo,Jerano,Manzano,Marcías,Marrero,Quesada,Quevedo,Quijada,Tablada,Talavera,Tames,Valdés,Valdiva,Valencia'

nombres_m = 'Alicia,Ana,Beatriz,Carmen,Elenea,Cristina,Francisca,Isabel,Irene,Laura,Juana,Patricia,Paula,Pilar,Rosa,Fernanda,Maria'

nombres_h = 'Aaron,Abel,Bartolo,Bernardo,Bruno,Cesar,Claudio,Constantino,Daniel,Dante,Edgar,Eric,Federico,Jose,Luis,Marco,Octavio,Pablo'

states = 'AS,BS,CL,CS,DF,GT,HG,MC,MS,NL,PL,QR,SL,TC,TL,YN,NE,BC,CC,CM,CH,DG,GR,JC,MN,NT,OC,QT,SP,SR,TS,VZ,ZS'

thirty_days_months = [4,6,8,11]


def random_date():
    random_month = random.randint(1,12)

    if(random_month in thirty_days_months):
        random_day = random.randint(1,30)
    elif(random_month == 2):
        random_day = random.randint(1,28)
    else:
        random_day = random.randint(1,31)

    random_year = random.randint(1950,2020)

    return random_year, random_month, random_day

def get_random_name():
    random_sex = random.randint(0,1)
    nombres_h_list = list(nombres_h.split(','))
    nombres_m_list = list(nombres_m.split(','))
    apellidos_list = list(apellido.split(','))
    if(random_sex == 0):
        gender = 'H'
        _n = random.randint(0,len(nombres_h_list)-1)
        name = nombres_h_list[_n]
        second_name = _get_random_value_subnames(apellidos_list)
        third_name = _get_random_value_subnames(apellidos_list)
        while(third_name == second_name):
            third_name = _get_random_value_subnames(apellidos_list)        
    else:
        gender = 'M'
        _n = random.randint(0,len(nombres_m_list)-1)
        name = nombres_m_list[_n]
        second_name = _get_random_value_subnames(apellidos_list)
        third_name = _get_random_value_subnames(apellidos_list)
        while(third_name == second_name):
            third_name = _get_random_value_subnames(apellidos_list)

    return gender, name, second_name, third_name

def _get_random_value_subnames(apellidos_list):
    _a = random.randint(0,len(apellidos_list)-1)
    second_name = apellidos_list[_a]
    return second_name

def random_state():
    states_list = list(states.split(','))
    rand_number = random.randint(0,len(states_list)-1)
    state = states_list[rand_number]
    return state

def get_data():
    gender, name, second_name, third_name = get_random_name()
    year, month, day = random_date()
    state = random_state()

    return gender, name, second_name, third_name, year, month, day, state


def make_curp():
    gender, name, second_name, third_name, year, month, day, state  = get_data()  

    print('{} D A T O S {}'.format(('-*'*5),('-*'*5)))
    print(gender, name, second_name, third_name)
    print(year, month, day)
    print(state)
    print('{}'.format('-*'*16))


    c_first = second_name[:1]
    c_second = _get_vowel(second_name)
    c_third = third_name[:1]
    c_fourth = name[:1]
    if(month<10 and day < 10):
        c_fift = str(year)[2:] + str(0) + str(month) + str(0) + str(day)  
    elif(month<10 and day>10):
        c_fift = str(year)[2:] + str(0) + str(month) + str(day) 
    elif(month>10 and day<10):
        c_fift = str(year)[2:] + str(month) + str(0) + str(day) 
    else: 
        c_fift = str(year)[2:] + str(month) + str(0) + str(day) 
    c_sixth = gender
    c_seventh = state
    c_eighth = _get_next_consonant(second_name,1,'a')
    c_ninth = _get_next_consonant(third_name,1,'a')
    c_tenth = _get_next_consonant(second_name,2, c_eighth)
    homo = _get_homo()
    curp = c_first + c_second.upper() + c_third.upper() + c_fourth.upper() + c_fift + c_sixth.upper() + c_seventh.upper() + c_eighth.upper() + c_ninth.upper() + c_tenth.upper() + homo
    print('El curp es: \n {}'.format(curp))

def _get_homo():
    rand_num = random.randint(0,99)
    if(rand_num<10):
        num = str(0) + str(rand_num)
        return num
    else:
        num = str(rand_num)
        return num

def _get_next_consonant(x_name,start,letter_before):
    for letter in x_name[start:]:
        if letter not in ('a', 'e', 'i', 'o', 'u'):
            if letter is not letter_before:
                return letter


def _get_vowel(second_name):
    for letter in second_name:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            return letter




def _obtener():
    cadena = str(input('Ingresa la cadena: '))
    return cadena

def comparar():
    cadena = _obtener()
    c = True
    for elem in cadena:
        m = re.match(r'\d',elem)
        if(m):
            c = False
            break
    if(c):
        n = re.match(r'\w*a+\w*e+\w*\wi+\w*o+\w*u+\w*',cadena)
        if(n):
            print('Cadena Valida')
        else:
            print('Cadena Invalida')
        
    else:
        print('Cadena invalida')
    

if __name__ == '__main__':
    comparar()