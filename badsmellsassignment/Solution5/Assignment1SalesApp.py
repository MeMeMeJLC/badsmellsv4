import cmd
import pickle
import re
import doctest
import matplotlib.pyplot as plt
import numpy as np
import os


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

    def get_data(filename):

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

        return "get_data(" + filename + ") run"

    def validate(element, regex_statement):
        match_element = re.match(regex_statement, element)
        if match_element is None or len(element) is not 4:
            print('id format incorrect: id entered as None')
            id = None
            return id
        else:
            return id

    """
    def validate_id(id):

        match_id = re.match('[A-Z][0-9]{3}', id)
        if match_id is None or len(id) is not 4:
            print('id format incorrect: id entered as None')
            id = None
            return id
        else:
            return id

    def validate_gender(gender):

        match_gender = re.match('(M|F)', gender)
        if match_gender is None:
            print('gender format incorrect:  entered as None')
            gender = None
            return gender
        else:
            return gender

    def validate_age(age):

        match_age = re.match('[0-9]{2}', age)
        if match_age is None or len(age) is not 2:
            print('age format incorrect:  entered as 0')
            age = 0
            return age
        else:
            return int(age)

    def validate_sales(sales):

        match_sales = re.match('[0-9]{3}', sales)
        if match_sales is None or len(sales) is not 3:
            print('sales format incorrect:  entered as 0')
            sales = 0
            return sales
        else:
            return int(sales)

    def validate_bmi(bmi):

        match_bmi = re.match('(Normal|Overweight|Obesity|Underweight)', bmi)
        if match_bmi is None:
            print('bmi format incorrect:  entered as None')
            bmi = None
            return bmi
        else:
            return bmi

    def validate_income(income):

        match_income = re.match('[0-9]{2,3}', income)
        if match_income is None or len(income) > 3:
            print('income format incorrect:  entered as 0')
            income = 0
            return income
        else:
            return int(income)
        """

class View():

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
        print("pie_chart_gender run")

    def pie_chart_bmi():
        obesity_count = 0
        overweight_count = 0
        normal_count = 0
        underweight_count = 0
        all_valid_count = 0

        for element in Model.bmi_list:
            if element == 'Obesity':
                obesity_count += 1
                all_valid_count += 1
            elif element == 'Overweight':
                overweight_count += 1
                all_valid_count += 1
            elif element == 'Normal':
                normal_count += 1
                all_valid_count += 1
            elif element == 'Underweight':
                underweight_count += 1
                all_valid_count += 1

        try:
            ob_percent = obesity_count / all_valid_count * 100
        except ZeroDivisionError:
            ob_percent = 0
        try:
            ov_percent = overweight_count / all_valid_count * 100
        except ZeroDivisionError:
            ov_percent = 0
        try:
            norm_percent = normal_count / all_valid_count * 100
        except ZeroDivisionError:
            norm_percent = 0
        try:
            und_percent = underweight_count / all_valid_count * 100
        except ZeroDivisionError:
            und_percent = 0

        labels = 'Obesity', 'Overweight', 'Normal', 'Underweight'
        sizes = ob_percent, ov_percent, norm_percent, und_percent
        colors = 'red', 'orange', 'green', 'orange'

        plt.title("Percentage of Employees in Each BMI Category")
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()
        print("pie_chart_bmi run")


class Controller(cmd.Cmd):

    def do_load_file(self):
        """
        :method: load_file or lf
        :description: Gets employee data from a text file. This method will
        prompt the user to enter the location/text file name. Text file must
        contain lines of data (id gender age sales bmi income)like this - A111
        F 32 300 Normal 500 - with each employee on a new line. Any invalid
        data will be inputted as 0 or None. Once this is run the data will be
        loaded and ready to analyse or save in pickle.
        :param: none
        :return: Data into correct format to be saved or analysed in the app.
        """
        filename = input("Enter the destination/filename. \
        Eg: D:/data/load_data.txt")
        Model.get_data(filename)

    def do_display_gender_data(self, args):
        """
        :method: display_gender_data or dg
        :description: If data has been loaded into the app it will show a pie
        chart of the percentage of Male and Female employees. If data has not
        already been loaded the user will be prompted to enter the
        location/filename of data to be loaded.
        :param: none
        :return: A pie chart of genders of employees
        """
        filename = args
        if not Model.gender_list:
            print("No data loaded, please enter data location")
            Model.get_data(filename)
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
        filename = args
        if not Model.bmi_list:
            print("No data loaded, please enter data location")
            Model.get_data(filename)
            if Model.bmi_list:
                View.pie_chart_bmi()
        else:
            View.pie_chart_bmi()

    def do_quit(self, args):
        """
        :method: quit or q
        :description: Quit the application. Will prompt the user as to
        whether the user would like to save the data serialised.
        :param: none
        :return: Will exit the app.
        """
        #doctest.testfile("doctests.txt")

        print('Quitting...')
        raise SystemExit

    do_q = do_quit
    do_db = do_display_bmi_data
    do_dg = do_display_gender_data
    do_lf = do_load_file


if __name__ == '__main__':
    controller = Controller()
    controller.prompt = ':) '
    doctest.testfile("doctests.txt")
    controller.cmdloop('Starting prompt...')
