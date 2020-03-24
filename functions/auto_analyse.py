""""
	Auteur : Julien Michelet
	Date : mars 2020
	But du programme :
	Fonction automatique des fonctions suivantes :

	Version : 0.0
"""
import os
import sys
import time
from datetime import datetime
from functions import email_identities

today_date = datetime.now()
report_date = "\nDATE: ", str(today_date.month) + str(today_date.day) + str(today_date.year)\
              + str(today_date.hour) + str(today_date.minute)


def auto_analyse_full(file):
    # full meta data
    contenu = email_identities.all_meta_data_var(file)
    today_date = datetime.now()
    name_file = "Report" + "_" + str(today_date.month) + "-" + str(today_date.day) +\
                "-" + str(today_date.year) + "-" + str(today_date.hour) +\
                ":" + str(today_date.minute) + ".txt"
    file_analyse = open(name_file, "w")
    file_analyse.write(contenu)
    file_analyse.close()

    # Short Meta data
    email_identities.short_meta_data_var(file, name_file)

    # body extract
    email_identities.body_extract_var(file)


