from tkinter import *  # import tkinter module as *
import datetime  # import datetime module

k = datetime.datetime.now()  # current date
a = str(k.date())  # convert date into string format


def display():  # display function
    display = Tk()  # assign display a Tk() value to create a root window
    display.title('Parking Management System')  # set windows title
    display.config(bg='#000000')  # set bg color
    display.minsize(439, 250)  # set minimum windows size
    display.maxsize(439, 250)  # set maximum windows size
    heading = Label(display, text='PARKING MANAGEMANT SYSTEM', bg='black',
                    fg='white', font=('Arial', 19))  # create a Label widget to display text
    heading.grid(columnspan=20, pady=10)  # create a grid

    def bikef():  # bikef function
        bk = Tk()  # assign bk a Tk() value to create a root window
        bk.title('Bike')  # set windows title
        bk.config(bg='#000000')  # set bg color
        heading = Label(bk, text='PARKING MANAGEMANT SYSTEM', bg='black',
                        fg='white', font=('Arial', 19))  # create a Label
        heading.grid(row=0, columnspan=20, pady=10)  # create a grid
        f = open('bike.txt')  # open bike.txt
        txt = f.read()  # read the file
        flable = Label(bk, text=txt)  # show the file
        flable.grid(row=3, columnspan=4)  # create the grid
        bk.mainloop()  # loop the window

    def carf():  # carf function
        bk = Tk()  # assign bk a Tk() value to create a root window
        bk.title('Car')  # set windows title
        bk.config(bg='#000000')  # set bg color
        heading = Label(bk, text='PARKING MANAGEMANT SYSTEM', bg='black',
                        fg='white', font=('Arial', 19))  # create a Label
        heading.grid(row=0, columnspan=20, pady=10)  # create a grid
        f = open('car.txt')  # open bike.txt
        txt = f.read()  # read the file
        flable = Label(bk, text=txt)  # show the file
        flable.grid(row=3, columnspan=4)  # create the grid
        bk.mainloop()  # loop the window

    bikebutton = Button(
        display,
        text='Bike',
        command=bikef,
        bg='gray',
        padx=20,
        fg='white',
    )

    # create a button using Tkinter Button widget

    bikebutton.grid(row=1, column=3, pady=30, sticky='w')  # create a grid

    carbutton = Button(
        display,
        text='Car',
        command=carf,
        bg='gray',
        padx=20,
        fg='white',
    )

    # create a button using Tkinter Button widget

    carbutton.grid(row=1, column=6, pady=30, sticky='w')  # create a grid

    display.mainloop()  # loop the window


def add():  # add function
    add = Tk()  # assign add a Tk() value to create a root window
    add.config(bg='#000000')  # set bg color
    add.minsize(439, 250)  # set minimum windows size
    add.maxsize(439, 250)  # set maximum windows size
    add.title('Parking Management System')  # set windows title
    heading = Label(add, text='PARKING MANAGEMANT SYSTEM', bg='black', fg='white', font=(
        'Arial', 19))  # create a Label widget to display text
    heading.grid(columnspan=20, pady=10)  # make a grid
    l1 = Label(add, text='Owner name:')  # create a Label widget
    l1.grid(row=1, column=0)  # create a grid
    l2 = Label(add, text='Vehical No:')  # create a Label widget
    l2.grid(row=2, column=0)  # create a grid
    owner = StringVar()  # a tkinter variable for editing widget's value
    vno = StringVar()  # a tkinter variable for editing widget's value

    # Entry widget for accepting text

    ownerentry = Entry(add, textvariable=owner)
    ownerentry.grid(row=1, column=1)  # create a grid

    # Entry widget for accepting text

    vnoentry = Entry(add, textvariable=vno)
    vnoentry.grid(row=2, column=1)  # create a grid

    l3 = Label(add, text='Vehicle Type:')  # create a Label widget
    l3.grid(row=3, column=0)  # create a grid

    def bikee():  # bikee function
        o = ownerentry.get()  # get the ownerentry value given by user
        v = vnoentry.get()  # get the vnoentry value given by user

        # open bike.txt file with mode - 'a' (Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.)

        f = open('bike.txt', 'a')
        f.write(o.lower() + '   ' + v + '   ' + a + '   ' + str(k.hour)
                + ':' + str(k.minute) + '\r\n')  # write function to add some text in the file

    def care():  # care function
        o = ownerentry.get()  # get the ownerentry value given by user
        v = vnoentry.get()  # get the vnoentry value given by user

        # open bike.txt file with mode - 'a' (Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.)

        f = open('car.txt', 'a')
        f.write(o.lower() + '   ' + v + '   ' + a + '    '
                + str(k.hour) + ':' + str(k.minute) + '\r\n')  # write function to add some text in the file

    def thankyou():  # thankyou function

        # create a Label widget to display text

        l = Label(add, text='Parking Done!!!', font=10)
        l.grid(row=6, column=1)  # create a grid

    bikebutton = Button(  # button text
                          # command to be executed when clicked
        add,
        text='Bike',
        command=bikee,
        padx=32,
        bg='gray',
        fg='white',
    )

    # create a button using Tkinter Button widget

    bikebutton.grid(row=4, column=0, pady=5)  # create a grid

    carbutton = Button(
        add,
        text='Car',
        command=care,
        padx=32,
        bg='gray',
        fg='white',
    )

    # create a button using Tkinter Button widget

    carbutton.grid(row=4, column=1)  # create a grid

    s = Button(add, text='Submit', padx=25, bg='gray',
               command=thankyou)

    # create a button using Tkinter Button widget

    s.grid(row=5, column=1, pady=10)  # create a grid

    add.mainloop()  # run a programm forever till the time user closes the window


def search():  # search function
    search = Tk()  # assign search a Tk() value to create a root window
    search.minsize(439, 250)  # set minimum windows size
    search.maxsize(439, 250)  # set maximum windows size
    search.config(bg='#000000')  # set bg color
    heading = Label(search, text='PARKING MANAGEMANT SYSTEM', bg='black',
                    fg='white', font=('Arial', 19))
    heading.grid(columnspan=20, pady=10)  # create a grid

    def bikes():  # bikes function
        b = Tk()  # assign b a Tk() value to create a root window
        b.minsize(439, 500)  # set miniimum windows size
        b.maxsize(439, 500)  # set maximum windows size
        b.config(bg='#000000')  # set bg color
        heading = Label(b, text='PARKING MANAGEMANT SYSTEM', bg='black',
                        fg='white', font=('Arial', 19))  # create a Label
        heading.grid(columnspan=20, pady=10)  # create a grid

        l1 = Label(b, text='Owner name:')  # create a Label
        l1.grid(row=3, column=0, pady=10)  # create a grid
        sowner = StringVar()  # a tkinter variable for editing widget's value

        # Entry widget for accepting text

        sownerentry = Entry(b, textvariable=sowner)
        sownerentry.grid(row=3, column=1, pady=10)  # create the grid

        def tra():  # tra function
            key = sownerentry.get().lower()  # get the sownerentry value given by user
            f = open('bike.txt')  # open the bike.txt file
            for line in f:  # for loop
                line = line.rstrip()  # remove the white spaces at the end
                if line.startswith(key):  # condition
                    lab = Label(b, text=line)  # label
                    lab.grid(row=6, columnspan=10)  # create a grid

        tr = Button(b, text='submit', command=tra, padx=10, bg='gray')

        # button

        tr.grid(row=4, column=1)  # grid

    def cars():  # cars function
        b = Tk()  # assign b a Tk() value to create a root window
        b.minsize(439, 500)  # set miniimum windows size
        b.maxsize(439, 500)  # set maximum windows size
        b.config(bg='#000000')  # set bg color
        heading = Label(b, text='PARKING MANAGEMANT SYSTEM', bg='black',
                        fg='white', font=('Arial', 19))  # create a Label
        heading.grid(columnspan=20, pady=10)  # create a grid

        l1 = Label(b, text='Owner name:')  # label
        l1.grid(row=3, column=0, pady=10)  # grid
        sowner = StringVar()  # a tkinter variable for editing widget's value

        # Entry widget for accepting text

        sownerentry = Entry(b, textvariable=sowner)
        sownerentry.grid(row=3, column=1, pady=10)  # create a grid

        def traa():  # traa function
            key = sownerentry.get().lower()  # get the sownerentry value
            f = open('car.txt')  # open the car.txt file
            for line in f:  # for loop
                line = line.rstrip()  # remove the white spaces
                if line.startswith(key):  # conditions
                    lab = Label(b, text=line)  # label
                    lab.grid(row=6)  # create a grid

        tr = Button(b, text='submit', command=traa, padx=10, bg='gray')

        # button

        tr.grid(row=4, column=1, sticky='w', pady=10)  # grid

    bikebutton = Button(
        search,
        text='Bike',
        command=bikes,
        bg='gray',
        padx=20,
        fg='white',
    )

    # button

    bikebutton.grid(row=2, column=3, pady=30, padx=5)  # grid

    carbutton = Button(
        search,
        text='Car',
        bg='gray',
        padx=20,
        command=cars,
        fg='white',
    )

    # button

    carbutton.grid(row=2, column=6, pady=30, padx=5)  # grid
    search.mainloop()  # run the loop


def remove():  # remove function
    remove = Tk()  # assign remove a Tk() value to create a root window
    remove.config(bg='#000000')  # set bg color
    remove.minsize(439, 250)  # set minimum windows size
    remove.maxsize(439, 250)  # set maximum windows size
    remove.title('Parking Management System')  # set windows title
    heading = Label(remove, text='PARKING MANAGEMANT SYSTEM', bg='black', fg='white', font=(
        'Arial', 19))  # create a Label widget to display text
    heading.grid(columnspan=20, pady=10)  # make a grid
    l1 = Label(remove, text='Owner name:')  # create a Label widget
    l1.grid(row=1, column=0)  # create a grid
    owner = StringVar()  # a tkinter variable for editing widget's value

    # Entry widget for accepting text

    ownerentry = Entry(remove, textvariable=owner)
    ownerentry.grid(row=1, column=1)  # create a grid

    def bikee():  # bikee function
        key = ownerentry.get().lower()  # get the ownerentry value given by user
        f = open('bike.txt')  # open the bike.txt file
        string_list = f.readlines()
        for line in string_list:  # for loop
            line = line.rstrip()  # remove the white spaces at the end
            if line.startswith(key):  # condition
                ourg = string_list.index(line + "\n")
                string_list[ourg] = ""
                my_file = open("bike.txt", "w")
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()

    def care():  # care function
        key = ownerentry.get().lower()  # get the sownerentry value given by user
        f = open('car.txt')  # open the bike.txt file
        string_list = f.readlines()
        for line in string_list:  # for loop
            line = line.rstrip()  # remove the white spaces at the end
            if line.startswith(key):  # condition
                ourg = string_list.index(line + "\n")
                string_list[ourg] = ""
                my_file = open("car.txt", "w")
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()

    def thankyou():  # thankyou function

        # create a Label widget to display text

        l = Label(remove, text='Parking removed!!!', font=10)
        l.grid(row=6, column=1)  # create a grid

    bikebutton = Button(  # button text
                          # command to be executed when clicked
        remove,
        text='Bike',
        command=bikee,
        padx=32,
        bg='gray',
        fg='white',
    )

    # create a button using Tkinter Button widget

    bikebutton.grid(row=4, column=0, pady=5)  # create a grid

    carbutton = Button(
        remove,
        text='Car',
        command=care,
        padx=32,
        bg='gray',
        fg='white',
    )

    # create a button using Tkinter Button widget

    carbutton.grid(row=4, column=1)  # create a grid

    s = Button(remove, text='Submit', padx=25, bg='gray',
               command=thankyou)

    # create a button using Tkinter Button widget

    s.grid(row=5, column=1, pady=10)  # create a grid

    remove.mainloop()  # run a programm forever till the time user closes the window


intro = Tk()
intro.minsize(439, 200)
intro.maxsize(439, 200)
intro.config(bg='#000000')
intro.title('Parking Management System')
heading = Label(intro, text='PARKING MANAGEMANT SYSTEM', bg='black',
                fg='white', font=('Arial', 19))
heading.grid(columnspan=20, pady=10, sticky='nw')
entryfram = Frame(intro, borderwidth=9)
b1 = Button(intro, text='Entry', command=add, bg='gray')
b1.grid(row=1, column=2, pady=30)
b2 = Button(intro, text='Show', command=display, bg='gray')
b2.grid(row=1, column=5, pady=30)
b3 = Button(intro, text='Search', bg='gray', command=search)
b3.grid(row=1, column=8, pady=30)
b3 = Button(intro, text='Remove', bg='gray', command=remove)
b3.grid(row=1, column=11, pady=30)
intro.mainloop()


# MADE BY Sujal Goel


# References
"""
https://www.geeksforgeeks.org/python-tkinter-label/
https://www.geeksforgeeks.org/introduction-to-tkinter/
https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/
https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/
https://www.programcreek.com/python/example/73631/tkinter.StringVar/
https://www.geeksforgeeks.org/python-tkinter-entry-widget/
https://www.programiz.com/python-programming/methods/built-in/open/
https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/
https://www.javatpoint.com/python-tkinter-button/
"""
