import cmd
import pickle
import re
import doctest
import matplotlib.pyplot as plt
import numpy as np
import os
import unittest



class MyFileExistsError(Exception):
    def __init__(self):
        Exception.__init__(self, "file alreadys exists, try again with a \
        different name or location")


class Model():
    id_list = list()
    gender_list = list()
    age_list = list()
    sales_list = list()
    bmi_list = list()
    income_list = list()

    def get_data():
        """
        Check correct data has entered list at correct index.
        loadData_Bad.txt scenario.

        >>> Model.id_list[3] is None
        True

        >>> Model.gender_list[3]
        'F'
        """
        filename = input("Enter the destination/filename. \
        Eg: D:/data/load_data.txt")
        try:
            with open(filename, 'r') as f:
                for line in f:
                    raw_line_data = line
                    i = 0
                    for element in raw_line_data.split():
                        if i == 0:
                            element = Model.validate_id(element)
                            Model.id_list.append(element)
                        elif i == 1:
                            element = Model.validate_gender(element)
                            Model.gender_list.append(element)
                        elif i == 2:
                            element = Model.validate_age(element)
                            Model.age_list.append(element)
                        elif i == 3:
                            element = Model.validate_sales(element)
                            Model.sales_list.append(element)
                        elif i == 4:
                            element = Model.validate_bmi(element)
                            Model.bmi_list.append(element)
                        elif i == 5:
                            element = Model.validate_income(element)
                            Model.income_list.append(element)
                        else:
                            print("error in get_data() raw_line_data")
                        i += 1

        except IOError:
            print("IO error, not reading file. Try entering filename again")

    def serialise_data():

        print("called serialise_data()")
        """
        toSerialiseList = ""
        for element in Model.id_list:
            i = Model.id_list.index(element)
            toSerialiseList = toSerialiseList + Model.id_list[i] + " " \
                + Model.gender_list[i] + " " + str(Model.age_list[i]) + " " + \
                str(Model.sales_list[i]) + " " + Model.bmi_list[i] + " " \
                + str(Model.income_list[i]) + os.linesep
        print(toSerialiseList)

        if Model.id_list or Model.gender_list or Model.age_list or \
            Model.sales_list or Model.bmi_list or Model.income_list:
                serialise_location = input('Enter location/filename to save \
                    to: ')
                try:
                    with open(serialise_location + '.pickle', 'wb') as f:
                        pickle.dump(str(toSerialiseList), f)
                except MyFileExistsError:
                    overwrite = input("File already exists. Overwrite it? \
                        Y or N")
                    if overwrite == 'Y' or 'y':
                        with open(serialise_location + '.pickle', 'wb') as f:
                            pickle.dump(str(toSerialiseList), f)
        else:
            print("No data to save")
        """

    def load_serialised_data():
        print("called load serialised_data()")
        """
        load_serial_data = input('Would you like to reload saved data? Y or N')
        if load_serial_data == 'y' or 'Y':
            serialise_location = input('Enter location/filename to save to: ')
            try:
                with open(serialise_location + '.pickle', 'rb') as f:
                    data = pickle.load(f)
                    for line in f:
                        raw_line_data = line
                        i = 0
                        for element in raw_line_data.split():
                            if i == 0:
                                element = Model.validate_id(element)
                                Model.id_list.append(element)
                            elif i == 1:
                                element = Model.validate_gender(element)
                                Model.gender_list.append(element)
                            elif i == 2:
                                element = Model.validate_age(element)
                                Model.age_list.append(element)
                            elif i == 3:
                                element = Model.validate_sales(element)
                                Model.sales_list.append(element)
                            elif i == 4:
                                element = Model.validate_bmi(element)
                                Model.bmi_list.append(element)
                            elif i == 5:
                                element = Model.validate_income(element)
                                Model.income_list.append(element)
                            else:
                                print("error in get_data() raw_line_data")
                            i += 1
            except OSError.FileNotFoundError:
                    print('File not found. Try again')
                    load_serialised_data()
            """

    def validate_id(id):
        """
        test using loadData_Bad.txt.
        #Raw input is "a0111", should return None
        because the input is too long to be valid.

        >>> Model.id_list[1] is None
        True

        #Raw input is "c234", should return None because
        the input has a lower case first char.

        >>> Model.id_list[3] is None
        True

        #Raw input is "E30", should return None because
        the input is not long enough.

        >>> Model.id_list[5] is None
        True

        #Raw input is "F456", should return "F456" because
        the input is in correct format.
        >>> Model.id_list[6]
        'F456'
        """
        match_id = re.match('[A-Z][0-9]{3}', id)
        if match_id is None or len(id) is not 4:
            print('id format incorrect: id entered as None')
            id = None
            print(id)
            return(id)
        else:
            return id

    def validate_gender(gender):
        """
        #Raw input is "?", should return None because not a valid input.
        >>> Model.gender_list[1] is None
        True

        #Raw input is " ", should return 0 because not a valid input.
        >>> Model.gender_list[6] is None
        True

        #Raw input is "F", should return "F" because it is valid input.
        >>> Model.gender_list[3]
        'F'
        """
        match_gender = re.match('(M|F)', gender)
        if match_gender is None:
            print('gender format incorrect:  entered as None')
            gender = None
            return gender
        else:
            return gender

    def validate_age(age):
        """
        #Raw input is "2", should return 0 as input is in
        invalid format.

        >>> Model.age_list[0] is 0
        True

        #Raw input is "1S", should return 0 as input has a
        non-int character in it.

        >>> Model.age_list[7] is 0
        True

        #Raw input is "60", should return "60" as it is valid.

        >>> Model.age_list[9]
        '60'
        """
        match_age = re.match('[0-9]{2}', age)
        if match_age is None or len(age) is not 2:
            print('age format incorrect:  entered as 0')
            age = 0
            return age
        else:
            return int(age)

    def validate_sales(sales):
        """
        #Raw input is "54", should return 0, because input in
        incorrect format.

        >>> Model.sales_list[6] is 0
        True

        #Raw input is "5554", should return 0, because input is in
        incorrect format, too long

        >>> Model.sales_list[7] is 0
        True

        #Raw input is "222", should return "222" as it's correct format

        >>> Model.sales_list[0]
        '222'
        """
        match_sales = re.match('[0-9]{3}', sales)
        if match_sales is None or len(sales) is not 3:
            print('sales format incorrect:  entered as 0')
            sales = 0
            return sales
        else:
            return int(sales)

    def validate_bmi(bmi):
        """
        #Raw input is "underweight", should return None as first char
        is lowercase

        >>> Model.bmi_list[1] is None
        True

        #Raw input is " ", should return None as field is empty

        >>> Model.bmi_list[4] is None
        True

        #Raw input is "Normal", should return "Normal" as is correct format

        >>> Model.bmi_list[0]
        'Overweight'
        """
        match_bmi = re.match('(Normal|Overweight|Obesity|Underweight)', bmi)
        if match_bmi is None:
            print('bmi format incorrect:  entered as None')
            bmi = None
            return bmi
        else:
            return bmi

    def validate_income(income):
        """
        #Raw input is "8", should return 0, incorrect format, only 1 number

        >>> Model.income_list[2] is 0
        True

        #Raw input is " ", should return 0 as it is an empty field

        >>> Model.income_list[3] is 0
        True

        #Raw input is "999", should return "999" as is in correct format
        >>> Model.income_list[0]
        '999'

        #Raw input is "87", should return "87" because it is correct format
        >>> Model.income_list[1]
        '87'

        """
        match_income = re.match('[0-9]{2,3}', income)
        if match_income is None or len(income) > 3:
            print('income format incorrect:  entered as 0')
            income = 0
            return income
        else:
            return int(income)


class View():
    pass

    """ def scatter_plot(x, xName, y, yName):

        arrayX = np.array(x)
        arrayY = np.array(y)

        plt.bar(x, y)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Interesting graph\nCheck it out')
        plt.legend()
        plt.show()"""

    def pie_chart_gender():
        m_count = 0
        f_count = 0
        all_valid_count = 0
        for element in Model.gender_list:
            if element == 'F':
                f_count += 1
                all_valid_count += 1
            elif element == 'M':
                m_count += 1
                all_valid_count += 1
        try:
            m_percentage = m_count / all_valid_count * 100
        except ZeroDivisionError:
            m_percentage = 0
        try:
            f_percentage = f_count / all_valid_count * 100
        except ZeroDivisionError:
            f_percentage = 0

        labels = 'Female', 'Male'
        sizes = f_percentage, m_percentage
        colors = 'pink', 'blue'

        plt.title('Employee Gender Percentages')
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()

    def pie_chart_bmi():
        obesity_count = 0
        overweight_count = 0
        normal_count = 0
        underweight_count = 0
        all_valid_count = 0

        for element in Model.bmi_list:
            if element == 'Obesity':
                print('ob')
                obesity_count += 1
                all_valid_count += 1
            elif element == 'Overweight':
                print('ov')
                overweight_count += 1
                all_valid_count += 1
            elif element == 'Normal':
                print('norm')
                normal_count += 1
                all_valid_count += 1
            elif element == 'Underweight':
                print('und')
                underweight_count += 1
                all_valid_count += 1

        try:
            ob_percent = obesity_count / all_valid_count * 100
            print('obese ' + str(ob_percent))
        except ZeroDivisionError:
            ob_percent = 0
        try:
            ov_percent = overweight_count / all_valid_count * 100
            print('over ' + str(ov_percent))
        except ZeroDivisionError:
            ov_percent = 0
        try:
            norm_percent = normal_count / all_valid_count * 100
            print('norm ' + str(norm_percent))
        except ZeroDivisionError:
            norm_percent = 0
        try:
            und_percent = underweight_count / all_valid_count * 100
            print("und " + str(und_percent) + ' ' + str(underweight_count))
        except ZeroDivisionError:
            und_percent = 0

        print(all_valid_count)
        labels = 'Obesity', 'Overweight', 'Normal', 'Underweight'
        sizes = ob_percent, ov_percent, norm_percent, und_percent
        colors = 'red', 'orange', 'green', 'orange'

        plt.title("Percentage of Employees in Each BMI Category")
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()


class Controller(cmd.Cmd):

    def do_load_file(self, args):
        """
        :method: load_file or lf
        :description: Gets employee data from a text file. This method will
        prompt the user to enter the location/text file name. Text file must
        contain lines of data (id gender age sales bmi income)like this - A111
        F 32 300 Normal 500 - with each employee on a new line. Any invalid
        data will be inputted as 0 or None. Once this is run the data will be
        loaded and ready to analyse or save in pickle.
        :param: self, args
        :return: Data into correct format to be saved or analysed in the app.
        """
        Model.get_data()

    def do_save_data(self, args):
        """
        :method: save_data
        :description: Saves data as a serialised file to access later.
        :param: self, args
        :return: Data saved in a serialised file
        """
        Model.serialise_data()

    def do_load_saved_file(self, args):
        """
        :method: load_saved_file
        :description: If data has been saved previously it can be reloaded.
        This is not for text files, but for serialised data.
        :param: self
        :return: Data reloaded from a previously saved file.
        """
        Model.load_serialised_data()

    def do_display_gender_data(self, args):
        """
        :method: display_gender_data or dg
        :description: If data has been loaded into the app it will show a pie
        chart of the percentage of Male and Female employees. If data has not
        already been loaded the user will be prompted to enter the
        location/filename of data to be loaded.
        :param: self
        :return: A pie chart of genders of employees
        """

        if not Model.gender_list:
            print("No data loaded, please enter data location")
            Model.get_data()
            if Model.gender_list:
                View.pie_chart_gender()
        else:
            View.pie_chart_gender()

    def do_display_bmi_data(self, args):
        """
        :method: display_bmi_data or db
        :description: If data has been loaded into the app it will show a pie
        chart of the percentage of Obese, Overweight, Normal and Underweight
        employees. If data has notalready been loaded the user will be
        prompted to enter the location/filename of data to be loaded.
        :param: self
        :return: A pie chart of bmi categories of employees.
        """
        if not Model.bmi_list:
            print("No data loaded, please enter data location")
            Model.get_data()
            if Model.bmi_list:
                View.pie_chart_bmi()
        else:
            View.pie_chart_bmi()

    def do_quit(self, args):
        """
        :method: quit or q
        :description: Quit the application. Will prompt the user as to
        whether the user would like to save the data serialised.
        :param: self
        :return: Will exit the app.
        """

        print('Quitting...')
        raise SystemExit

    do_q = do_quit
    do_db = do_display_bmi_data
    do_dg = do_display_gender_data
    do_lf = do_load_file


if __name__ == '__main__':


    controller = Controller()
    controller.prompt = ':) '
    controller.cmdloop('Starting prompt...')
