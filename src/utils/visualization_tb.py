#Este archivo contiene las funciones de visualización (pandas, matplolib y seaborn) que elaboramos en el proyecto.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import squarify as sq

def sns_gstyle():
    """Esta función cambia los gráficos de seaborn que vienen por defecto"""
    sns.set(style="ticks")

def alcohol_columns_intro():
    """Esta función introduce al usuario al significado de las columnas así
    como al valor que nos otorgan, de los datasets encontrados"""

    print("-school: Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)")
    print("-sex: Student's sex (binary: 'F' - female or 'M' - male)")
    print("-age: Student's age (numeric: from 15 to 22)")
    print("-address: Student's home address type (binary: 'U' - urban or 'R' - rural)")
    print("-famsize: Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)")
    print("-Pstatus: Parent's cohabitation status (binary: 'T' - living together or 'A' - living apart)")
    print("-Medu: Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, or 4 - higher education)")
    print("-Fedu: Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, or 4 - higher education)")
    print("-Mjob: Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
    print("-Fjob: Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
    print("-reason: Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')")
    print("-guardian: Student's guardian (nominal: 'mother', 'father' or 'other')")
    print("-traveltime: Home to school travel time (numeric: 1 - &lt;15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - &gt;1 hour)")
    print("-studytime: Weekly study time (numeric: 1 - &lt;2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - &gt;10 hours)")
    print("-failures: Number of past class failures (numeric: n if 1&lt;=n&lt;3, else 4)")
    print("-schoolsup: Extra educational support (binary: yes or no)")
    print("-famsup: Family educational support (binary: yes or no)")
    print("-paid: Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)")
    print("-activities: Extra-curricular activities (binary: yes or no)")
    print("-nursery: Attended nursery school (binary: yes or no)")
    print("-higher: Wants to take higher education (binary: yes or no)")
    print("-internet: Internet access at home (binary: yes or no)")
    print("-romantic: With a romantic relationship (binary: yes or no)")
    print("-famrel: Quality of family relationships (numeric: from 1 - very bad to 5 - excellent")
    print("-freetime: Free time after school (numeric: from 1 - very low to 5 - very high)")
    print("-goout: Going out with friends (numeric: from 1 - very low to 5 - very high)")
    print("-Dalc: Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)")
    print("-Walc: Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)")
    print("-health: Current health status (numeric: from 1 - very bad to 5 - very good)")
    print("-absences: Number of school absences (numeric: from 0 to 93)")
    print("-G1: First period grade (numeric: from 0 to 20)")
    print("-G2: Second period grade (numeric: from 0 to 20)")
    print("-G3: Final grade (numeric: from 0 to 20, output target)")

def alcohol_column_intro(column):
    
    if column == "school":
        print("-school: Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)")
    elif column == "sex":
        print("-sex: Student's sex (binary: 'F' - female or 'M' - male)")
    elif column == "age":
        print("-age: Student's age (numeric: from 15 to 22)")
    elif column == "address":
        print("-address: Student's home address type (binary: 'U' - urban or 'R' - rural)")
    elif column == "famsize":
        print("-famsize: Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)")
    elif column == "Pstatus":
        print("-Pstatus: Parent's cohabitation status (binary: 'T' - living together or 'A' - living apart)")
    elif column == "Medu":
        print("-Medu: Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, or 4 - higher education)")
    elif column == "Fedu":
        print("-Fedu: Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, or 4 - higher education)")
    elif column == "Mjob":
        print("-Mjob: Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
    elif column == "Fjob":
        print("-Fjob: Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')")
    elif column == "reason":
        print("-reason: Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')")
    elif column == "guardian":
        print("-guardian: Student's guardian (nominal: 'mother', 'father' or 'other')")
    elif column == "traveltime":
        print("-traveltime: Home to school travel time (numeric: 1 - &lt;15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - &gt;1 hour)")
    elif column == "studytime":
        print("-studytime: Weekly study time (numeric: 1 - &lt;2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - &gt;10 hours)")
    elif column == "failures":
        print("-failures: Number of past class failures (numeric: n if 1&lt;=n&lt;3, else 4)")
    elif column == "schoolsup":
        print("-schoolsup: Extra educational support (binary: yes or no)")
    elif column == "famsup":
        print("-famsup: Family educational support (binary: yes or no)")
    elif column == "paid":
        print("-paid: Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)")
    elif column == "activities":
        print("-activities: Extra-curricular activities (binary: yes or no)")
    elif column == "nursery":
        print("-nursery: Attended nursery school (binary: yes or no)")
    elif column == "higher":
        print("-higher: Wants to take higher education (binary: yes or no)")
    elif column == "internet":
        print("-internet: Internet access at home (binary: yes or no)")
    elif column == "romantic":
        print("-romantic: With a romantic relationship (binary: yes or no)")
    elif column == "famrel":
        print("-famrel: Quality of family relationships (numeric: from 1 - very bad to 5 - excellent")
    elif column == "freetime":
        print("-freetime: Free time after school (numeric: from 1 - very low to 5 - very high)")
    elif column == "goout":
        print("-goout: Going out with friends (numeric: from 1 - very low to 5 - very high)")
    elif column == "Dalc":
        print("-Dalc: Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)")
    elif column == "Walc":
        print("-Walc: Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)")
    elif column == "health":
        print("-health: Current health status (numeric: from 1 - very bad to 5 - very good)")
    elif column == "absences":
        print("-absences: Number of school absences (numeric: from 0 to 93)")
    elif column == "G1":
        print("-G1: First period grade (numeric: from 0 to 20)")
    elif column == "G2":
        print("-G2: Second period grade (numeric: from 0 to 20)")
    elif column == "G3":
        print("-G3: Final grade (numeric: from 0 to 20, output target)")
    
def corr_onevalue_graphic_abs(data, variable):
    """Esta función muestra un gráfico para un Series correspondiente a un mostreo de correlación
    de una columna con las demás del dataframe. No estudia la negatividad o positividad de los valores
    ya que trabaja con valores absolutos"""
    current_palette = sns.color_palette("crest")
    plt.figure(figsize=(18,9))
    sq.plot(label=data.keys(), sizes=data.sort_values()[:-1].abs().values, color=current_palette, text_kwargs={'fontsize':13,'color':'white'})
    plt.title(f"Correlación de las variables en estudio con {variable}")
    plt.axis('off')

def corr_onevalue_graphic_n(data, variable):
    """Esta función muestra un gráfico para un Series correspondiente a un mostreo de correlación
    de una columna con las demás del dataframe"""
    plt.figure(figsize=(12,9))
    current_palette = sns.color_palette("Greens")
    data.sort_values()[:-1].plot.bar(width=1,color=current_palette, rot=60)
    plt.title(f"Correlación de las variables en estudio con {variable}")
    plt.ylabel('Coeficiente de correlación en valor absoluto')
    plt.xlabel('Variables en estudio')
    


def doble_barplot(x, y1, y2, hue, figsize, data):
    """Esta función configura dos gráficos de barras con un mismo valor de x con hue"""
    fig, ax = plt.subplots(1,2, figsize=figsize)
    sns.barplot(data=data, x=x, y=y1, hue=hue, palette="husl", ax=ax[0])
    sns.barplot(data=data, x=x, y=y2, hue=hue, palette="husl", ax=ax[1])

def line_count(x1, x2, y, hue, figsize, data):
    """Esta función configura una lineplot y un countplot con mismo hue para hacer una comparativa"""
    fig, ax = plt.subplots(1,2, figsize=figsize)
    sns.lineplot(data=data, x=x1, y=y, hue=hue, ax=ax[0])
    sns.countplot(data=data, x=x2, hue =hue, ax=ax[1])



def multi_subplot(data):
    """Esta función está adaptada únicamente al proyecto por su extensión. Es decir, llamará directamente
    a las variables que ya se encuentran dentro del archivo main. Esta función se utiliza para mostrar
    una gran cantidad de subplots que reflejan valores del DataFrame limpio."""

    fig, ax = plt.subplots(3,3, figsize=(22,11))
    sns.set(palette="husl")
    sns.barplot(data=data, x="age", y="studytime", hue="sex", ax=ax[0,0])
    sns.barplot(data=data, x="age", y="goout", hue="sex", ax=ax[0,1])
    sns.barplot(data=data, x="age", y="absences", hue="sex", ax=ax[0,2])
    sns.countplot(data=data, x="paid", hue ="sex", ax=ax[1,0])
    sns.countplot(data=data, x="activities", hue ="sex", ax=ax[1,1])
    sns.countplot(data=data, x="romantic", hue ="sex", ax=ax[1,2])
    sns.countplot(data=data, x="internet", hue ="sex", ax=ax[2,0])
    sns.countplot(data=data, x="schoolsup", hue ="sex", ax=ax[2,1])
    sns.countplot(data=data, x="nursery", hue ="sex", ax=ax[2,2])

def pie_chart(data):
    """Esta función configura un 'piechart' para el Series que le pasamos"""
    plt.figure(1, figsize=(24,12))
    labels = data.keys()
    a = plt.pie(data, labels=labels, autopct='%.0f%%', radius=0.7, textprops= {"weight":"bold"})
    return a