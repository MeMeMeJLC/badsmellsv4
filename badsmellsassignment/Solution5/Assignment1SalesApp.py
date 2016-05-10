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
    type_of_list = [id_list, gender_list, age_list, sales_list, bmi_list,
                    income_list]

    def get_data(filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    raw_line_data = line
                    i = 0
                    regex_list = [
                                    '[A-Z][0-9]{3}', '(M|F)', '[0-9]{2}',
                                    '[0-9]{3}',
                                    '(Normal|Overweight|Obesity|Underweight)',
                                    '[0-9]{2,3}']
                    for element in raw_line_data.split():
                        element = Model.validate(element, regex_list[i])
                        Model.type_of_list[i].append(element)
                        i += 1
        except IOError:
            print("IO error, not reading file. Try entering filename again")
        return "get_data(" + filename + ") run"

    def validate(element, regex_statement):
        match_element = re.match(regex_statement, element)
        if match_element is None:
            print('element format incorrect: element entered as None')
            element = None
            return element
        else:
            return element


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
