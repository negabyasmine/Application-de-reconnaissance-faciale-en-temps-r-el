from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import sqlite3
from barcode import EAN13
from barcode.writer import ImageWriter
import random
import datetime
import os
import time
import time as tm
import cv2
from pyzbar.pyzbar import decode

root = Tk()
root.title("mémoire fin d'etudes")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f"{w}x{h}+-7+0")

# root.resizable(height = 'FALSE', width='False')
root.attributes('-fullscreen', False)






# function

def createuser():

    btncreateuser = Button(frameAdmin, text="Create New User", command=createuser, bd=1)
    btncreateuser.place(x=10, y=10, width="150")

    def deleteall_users():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        cur.execute("Delete from users")
        mydb.commit()
        mydb.close()
        for joiujo in tree.get_children():
            tree.delete(joiujo)

    def delte_selecteduser():
        mydb = sqlite3.connect('mydatabase.db')
        cur = mydb.cursor()
        laselection = tree.item(tree.selection())['values'][0]
        zebzobi = str(laselection)
        sytax = str(f"delete from users where name = '{zebzobi}'")
        delete = cur.execute(sytax)
        mydb.commit()
        mydb.close()
        tree.delete(tree.selection())

    def addnewusertotableuser():
        print("la fonction marche ")
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        datass = cur.execute("""SELECT * FROM users""")
        # datass = list(datass)
        user_name_list = []
        for times154 in datass:
            user_name_list.append(times154[0])
        if entry_createusername.get() not in user_name_list:
            cur.execute("""INSERT INTO users (name , password , type) VALUES(?,?,?)""",
                        (entry_createusername.get(), entry_createuserpassword.get(), combo.get()))
            print("inserted")
            datasadd_totree = cur.execute("SELECT * from users")
            datasadd_totree = list(datasadd_totree)
            tree.insert("", END, value=datasadd_totree[-1])
        else:
            print('sa existe mec pas ! change pas de nom')

        # last_elm = datasadd_totree[-1]

        entry_createusername.delete(0, END)
        entry_createuserpassword.delete(0, END)

        mydb.commit()
        mydb.close()

    framforcreateuser = Frame(frameAdmin, height=700, width=w)
    framforcreateuser.place(x=0, y=60)
    title_grand = Label(framforcreateuser, text="créer nouveau utilisateur: ", font=("arial", 20, "bold"))
    title_grand.place(x=50, y=50)
    label_createusername = Label(framforcreateuser, text="Nom", font=("arial", 16, "bold"))
    label_createusername.place(x=50, y=120)
    createuserpassword = Label(framforcreateuser, text="mot de passe", font=("arial", 16, "bold"))
    createuserpassword.place(x=50, y=220)
    entry_createusername = Entry(framforcreateuser, font=("arial", 16, "bold"))
    entry_createusername.place(x=60, y=150, width="300", height="35")
    entry_createuserpassword = Entry(framforcreateuser, font=("arial", 16, "bold"))
    entry_createuserpassword.place(x=60, y=250, width="300", height="35")
    createusertype = Label(framforcreateuser, text="Type", font=("arial", 16, "bold"))
    createusertype.place(x=50, y=320)
    ###################################################################
    listof_type = ['Admin', 'caissier']
    combo = ttk.Combobox(framforcreateuser, values=listof_type, font=("arial", 16, "bold"))
    combo.current(1)
    combo.place(x=60, y=350, width="300", height="35")
    ###################################################################
    # entry_createusertype = Entry(framforcreateuser, font=("Times", 16, "bold"))
    # entry_createusertype.place(x=60, y=350, width="300", height="35")
    btn_createuser = Button(framforcreateuser, text="créer utilisateur", bd=1, font=("arial", 12, "bold"),
                            command=addnewusertotableuser)  # create user button
    btn_createuser.place(x=240, y=430, width="130", height="50")  # user button  place()
    btn_showeuser = Button(framforcreateuser, text="supprimer tout", bd=1, font=("arial", 12, "bold"),
                           command=deleteall_users)  # create user button
    btn_showeuser.place(x=60, y=430, width="120", height="50")  # user button  place()
    btncreateuser.destroy()
    btn_deleteeuser = Button(framforcreateuser, text="supprimer", bd=1, font=("arial", 15, "bold"),
                             command=delte_selecteduser)  # create user button
    btn_deleteeuser.place(x=765, y=100, width="120", height="50")  # user button  place()

    # tree view ------------------------------------------------------------------------------------------
    mydb = sqlite3.connect("mydatabase.db")
    cur = mydb.cursor()
    datafortreevieuw = cur.execute("""SELECT * FROM users""")
    x775xssqq = Label(framforcreateuser, text="Liste des utilisateurs : ", font=("arial", 18, "bold"))
    x775xssqq.place(x=450, y=35)

    tree = ttk.Treeview(framforcreateuser, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=450, y=70, height=400, width=300)
    tree.column(1, width=100)
    tree.column(2, width=100)
    tree.column(3, width=95)
    tree.heading(1, text="Nom")
    tree.heading(2, text="mot de passe")
    tree.heading(3, text="Type utilisateur")
    for itemx02treeview in datafortreevieuw:
        tree.insert("", END, value=itemx02treeview)
    mydb.commit()
    mydb.close()


# tree view ------------------------------------------------------------------------------------------
#


# "---------------------------------------------------------------------"
# Introduction et Parametres de Tkraise()-------------------------------------------------------
framelogin = Frame(root, height=h, width=w)
frameAdmin = Frame(root, height=h, width=w)
frameuser = Frame(root, height=h, width=w)


def swap(frame):
    frame.tkraise()
    entry_name.delete(0, END)
    entry_password.delete(0, END)


for frame in (framelogin, frameAdmin, frameuser):
    frame.place(x=0, y=0)
# databases
mydb = sqlite3.connect("mydatabase.db")
cur = mydb.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
                name text UNIQUE,
                password text,
                type text
            )""")
cur.execute("""CREATE TABLE IF NOT EXISTS produits(
    id integer PRIMARY KEY AUTOINCREMENT,
    name text,
    codebarr integer unique,
    prix_achat integer not null,
    prixde_vente integer not null,
    remise_ int,
    dateso date,
    timeso time,
    note_ text
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS produit_vendu(
    idv integer PRIMARY KEY AUTOINCREMENT,
    namev text ,
    prix_achatv int not null,
    prixde_ventev int not null,
    remise_v int,
    datesov date,
    timesov time
    )""")

mydb.commit()
# cur.execute("""INSERT INTO users (name , password , type) VALUES("admin" , "admin" , "admin")""")
# cur.execute("""INSERT INTO users (name , password , type) VALUES("kam" , "kam" , "admin")""")
# cur.execute("""INSERT INTO users (name , password , type) VALUES("kame" , "kame" , "admin")""")
mydb.commit()
mydb.close()

# admin account = ----------------------------------------
admin1 = "admin"
password1 = "admin"


def login11():
  
        swap(frameAdmin)
    


# admin account = ----------------------------------------
# frame login------------------------------------------------------------------------------------
# frame login------------------------------------------------------------------------------------
# frame login------------------------------------------------------------------------------------
# frame login------------------------------------------------------------------------------------
# frame login------------------------------------------------------------------------------------

souframelogin = Frame(framelogin,
                      width='500',
                      height="350")
souframelogin.place(x=420,
                    y=180)
grosTitre1 = Label(souframelogin,
                   text="________________",
                   font=("Times", 24, "bold"),
                   fg="green")
grosTitre1.place(x=30,
                 y=28)
grosTitre = Label(souframelogin,
                  text=" yasmine c'est votre expace administrateur ",
                  font=("Times", 18, "bold"),
                  fg="green")
grosTitre.place(x=22,
                y=100)
soustitre_name = Label(souframelogin,
                       text="",
                       font=("Times", 16, "bold"),
                       fg="green")
soustitre_name.place(x=2,
                     y=100)
soustitre_password = Label(souframelogin,
                           text="",
                           font=("Times", 16, "bold"),
                           fg="green")
soustitre_password.place(x=30,
                         y=180)

button_Login = Button(souframelogin,
                      text="Login",
                      font=("Times", 16, "bold"),
                      fg="green", bd=0,
                      bg="#C6D9C6",
                      command=login11)
button_Login.place(x=350,
                   y=280,
                   width="120")
# frameAdmin------------------------------------------------------------------------------------
# frameAdmin------------------------------------------------------------------------------------
# frameAdmin------------------------------------------------------------------------------------
# frameAdmin------------------------------------------------------------------------------------
# frameAdmin------------------------------------------------------------------------------------
"""myframeadminimage = ImageTk.PhotoImage(file="images/background.jpg")
monfond_decranframeadmin = Label(frameAdmin , image = myframeadminimage )
monfond_decranframeadmin.place(x = 0 , y = 0 , relwidth =1 , relheight=1)"""


# frameAdmin-------------------------------------------------------------------------------------
# frameAdmin-------------------------------------------------------------------------------------


def stokemanage():

    def affichageparpack():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        dfhfdhfdf99_ = cur.execute(
            """SELECT id ,name,COUNT(*),prix_achat,prixde_vente,remise_,dateso ,timeso ,note_  from produits group by name """)
        dfhfdhfdf99_ = list(dfhfdhfdf99_)
        for totot in tree02.get_children():
            tree02.delete(totot)
        for xxxxx65 in dfhfdhfdf99_:
            tree02.insert("", END, value=xxxxx65)
        btnaffichage_parpack = Button(framforstokemanage, text="Tri TOUS", bd=1, command=affichagepararticles)
        btnaffichage_parpack.place(x=135, y=160, width=120, height=30)
        mydb.commit()
        mydb.close()


    def affichagepararticles():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        Articles = "No data"
        dfhfdhfdf99_ = cur.execute(
            f"""SELECT id ,name,'{Articles}',prix_achat,prixde_vente,remise_,dateso ,timeso ,note_  from produits order by id  """)
        dfhfdhfdf99_ = list(dfhfdhfdf99_)
        for totot in tree02.get_children():
            tree02.delete(totot)
        for xxxxx65 in dfhfdhfdf99_:
            tree02.insert("", END, value=xxxxx65)
        btnaffichage_parpack = Button(framforstokemanage, text="Tri PACK", bd=1, command=affichageparpack)
        btnaffichage_parpack.place(x=135, y=160, width=120, height=30)

        mydb.commit()
        mydb.close()


    def edit_function_pack():
        selected_artcles = tree02.item(tree02.selection())['values'][1]
        def change_namexox8():
            mydb = sqlite3.connect("mydatabase.db")
            cur = mydb.cursor()
            if labl___85__02.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET name = '{labl___85__02.get().lower()}'  where name = '{selected_artcles}'""")

            if labl___85__04.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET prix_achat = '{int(labl___85__04.get())}'  where name = '{selected_artcles}'""")
            if labl___85__06.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET prixde_vente = '{int(labl___85__06.get())}'  where name = '{selected_artcles}'""")
            if labl___85__08.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET remise_ = '{labl___85__08.get().lower() + " DA"}'  where name = '{selected_artcles}'""")
            if labl___85__010.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET note_ = '{labl___85__010.get().lower()}'  where name = '{selected_artcles}'""")

            nameounus = labl___85__02.get().lower()
            qq52_4 = cur.execute(
                f"""SELECT id ,name,COUNT(*),prix_achat,prixde_vente,remise_,dateso ,timeso ,note_ FROM produits  where name = '{nameounus}' """)
            qq52_4 = list(qq52_4)
            #print(nameounus)
            for forttjnh8__r in tree02.get_children():
                tree02.delete(forttjnh8__r)
            for ioklnn_uj in qq52_4:
                tree02.insert("", END, values=ioklnn_uj)
            capitalisationtotla887()
            mydb.commit()
            mydb.close()

        root2 = Toplevel()
        root2.geometry(f'{w}x{h}+0+0')
        root2.attributes('-fullscreen', False)
        
        root2.title("Edition de  Packs")
        root2.iconbitmap("images/logo.ico")
        ##########################################################################################
        labl___85__01 = Label(root2, text="Nom", font=('arial', 9, 'bold'))
        labl___85__01.place(x=10, y=10)
        ##########################################################################################
        labl___85__02 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__02.place(x=10, y=30, width=230, height=30)
        ##########################################################################################
        ##########################################################################################
        labl___85__03 = Label(root2, text="Prix De Gros", font=('arial', 9, 'bold'))
        labl___85__03.place(x=10, y=70)
        ##########################################################################################
        labl___85__04 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__04.place(x=10, y=90, width=230, height=30)
        ##########################################################################################
        ############4#############################################################################
        labl___85__05 = Label(root2, text="Prix de l'unitée", font=('arial', 9, 'bold'))
        labl___85__05.place(x=10, y=130)
        ############4#############################################################################
        labl___85__06 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__06.place(x=10, y=150, width=230, height=30)
        ##########################################################################################
        ##########################################################################################
        labl___85__07 = Label(root2, text="Remise", font=('arial', 9, 'bold'))
        labl___85__07.place(x=10, y=190)
        ############5#############################################################################
        labl___85__08 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__08.place(x=10, y=210, width=230, height=30)
        ##########################################################################################
        ##########################################################################################
        labl___85__09 = Label(root2, text="Note", font=('arial', 9, 'bold'))
        labl___85__09.place(x=10, y=250)
        ############6#############################################################################
        labl___85__010 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__010.place(x=10, y=270, width=230, height=30)
        ##########################################################################################
        ##########################################################################################
        labl___85__011 = Button(root2, text="Modifer", font=('arial', 12, 'bold'), command=change_namexox8)
        labl___85__011.place(x=10, y=310, width=233, height=50)
        ############7#############################################################################
        labl___85__012 = Button(root2, text="Annuler", font=('arial', 10, 'bold'), command=root2.destroy)
        labl___85__012.place(x=10, y=370, width=233, height=30)
        ############7#############################################################################
        root2.mainloop()


    def editfunction_article():
        selected_artcles = tree02.item(tree02.selection())['values'][0]
        print(selected_artcles)
        def change_namexox8():
            mydb = sqlite3.connect("mydatabase.db")
            cur = mydb.cursor()
            if labl___85__02.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET name = '{labl___85__02.get().lower()}'  where id = '{selected_artcles}'""")

            if labl___85__04.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET prix_achat = '{int(labl___85__04.get())}'  where id = '{selected_artcles}'""")
            if labl___85__06.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET prixde_vente = '{int(labl___85__06.get())}'  where id = '{selected_artcles}'""")
            if labl___85__08.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET remise_ = '{labl___85__08.get().lower() + " DA"}'  where id = '{selected_artcles}'""")
            if labl___85__010.get() == "":
                pass
            else:
                cur.execute(
                    f"""UPDATE produits SET note_ = '{labl___85__010.get().lower()}'  where id = '{selected_artcles}'""")

            for forttjnh8__r in tree02.get_children():
                tree02.delete(forttjnh8__r)
            qq52_4 = cur.execute(
                f"""SELECT id ,name,COUNT(*),prix_achat,prixde_vente,remise_,dateso ,timeso ,note_ FROM produits  where id = '{selected_artcles}' """)
            qq52_4 = list(qq52_4)
            for ioklnn_uj in qq52_4:
                tree02.insert("", END, values=ioklnn_uj)
            capitalisationtotla887()
            mydb.commit()
            mydb.close()

        root2 = Toplevel()
        root2.geometry(f'{w}x{h}+0+0')
        root2.title("Edition de l'article ")
        root2.iconbitmap("images/logo.ico")
        root2.attributes('-fullscreen', False)
        ##########################################################################################
        labl___85__01 = Label(root2, text="Nom", font=('arial', 9, 'bold'))
        labl___85__01.place(x=10, y=10)
        ##########################################################################################
        labl___85__02 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__02.place(x=10, y=30, width=230, height=30)
        ##########################################################################################
        ##########################################################################################
        labl___85__03 = Label(root2, text="Prix De Gros", font=('arial', 9, 'bold'))
        labl___85__03.place(x=10, y=70)
        ##########################################################################################
        labl___85__04 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__04.place(x=10, y=90, width=230, height=30)
        ##########################################################################################
        ############4#############################################################################
        labl___85__05 = Label(root2, text="Prix de l'unitée", font=('arial', 9, 'bold'))
        labl___85__05.place(x=10, y=130)
        ############4#############################################################################
        labl___85__06 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__06.place(x=10, y=150, width=230, height=30)
        ##########################################################################################
        ##########################################################################################
        labl___85__07 = Label(root2, text="Remise", font=('arial', 9, 'bold'))
        labl___85__07.place(x=10, y=190)
        ############5#############################################################################
        labl___85__08 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__08.place(x=10, y=210, width=230, height=30)
        ##########################################################################################
        ##########################################################################################
        labl___85__09 = Label(root2, text="Note", font=('arial', 9, 'bold'))
        labl___85__09.place(x=10, y=250)
        ############6#############################################################################
        labl___85__010 = Entry(root2, font=('arial', 9, 'bold'))
        labl___85__010.place(x=10, y=270, width=230, height=30)
        ##########################################################################################
        ##########################################################################################
        labl___85__011 = Button(root2, text="Modifer", font=('arial', 12, 'bold'), command=change_namexox8)
        labl___85__011.place(x=10, y=310, width=233, height=50)
        ############7#############################################################################
        labl___85__012 = Button(root2, text="Annuler", font=('arial', 10, 'bold'), command=root2.destroy)
        labl___85__012.place(x=10, y=370, width=233, height=30)
        ############7#############################################################################

        root2.mainloop()


    def delete_jsuteoneselected():
        selcted__onearticlesby_id = tree02.item(tree02.selection())['values'][0]
        mydb = sqlite3.connect('mydatabase.db')
        cur = mydb.cursor()
        forselect8895_ = cur.execute(f"""SELECT * FROM produits where id = '{selcted__onearticlesby_id}'""")
        forselect8895_ = list(forselect8895_)
        for xyung85_2 in forselect8895_:
            filebarcode822361_i = str(xyung85_2) + ".png"
            filuslistous = os.listdir("code")
            for jjnhg__jf in filuslistous:
                if filebarcode822361_i in filuslistous:
                    os.remove("code" + '/' + filebarcode822361_i)
        cur.execute(f"delete from produits where id = '{selcted__onearticlesby_id}'")
        tree02.delete(tree02.selection())
        mydb.commit()
        mydb.close()
        capitalisationtotla887()


    def delleteselectedfileintree02():
        mydb = sqlite3.connect('mydatabase.db')
        cur = mydb.cursor()
        selected_tree = tree02.item(tree02.selection())['values'][1]
        strlo = str(selected_tree)
        forbarcode_delete_file = cur.execute(f"""SELECT * FROM produits where name = '{strlo}'""")
        forbarcode_delete_file = list(forbarcode_delete_file)
        for xytb in forbarcode_delete_file:
            file_plus_extension = str(xytb[2]) + ".png"
            print(file_plus_extension)
            files02 = os.listdir("code")
            if file_plus_extension in files02:
                os.remove("code" + '/' + file_plus_extension)

        cur.execute(f"delete from produits where name = '{strlo}'")
        tree02.delete(tree02.selection())

        mydb.commit()
        mydb.close()
        capitalisationtotla887()


    def delete_allfromtree02():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        cur.execute("Delete from produits")
        mydb.commit()
        mydb.close()
        for xx541 in tree02.get_children():
            tree02.delete(xx541)
        files = os.listdir("code")
        for oklo in files:
            os.remove(str("code" + '/' + oklo))
        os.rmdir("code")
        capitalisationtotla887()


    def addnew_articles():
        files = os.listdir("C:/Users/Hp/Desktop/mohand")
        # C:/Users/MOHSAT/Desktop/Rkale/code
        # C:/Users/usuas/Desktop/Rkale
        if "code" not in files:
            os.mkdir('C:/Users/Hp/Desktop/mohand/code')
        top = Toplevel()
        top.title('Add new article')
        top.geometry(f'{w}x{h}+0+0')
        top.iconbitmap("images/logo.ico")
        top.attributes('-fullscreen', False)

        def add_new_article_boutton():

            numberofpr_dect = 1
            plusnumber = 1
            convert = int(name_Entry001forquantite.get())
            while (numberofpr_dect <= convert):
                # generateurdebarcode------------------------------------------------------------------------------
                # *************************************************************************************************
                # *************************************************************************************************
                # *************************************************************************************************
                # *************************************************************************************************
                list_of_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                num01 = random.choice(list_of_number)
                num02 = random.choice(list_of_number)
                num03 = random.choice(list_of_number)
                num04 = random.choice(list_of_number)
                num05 = random.choice(list_of_number)
                num06 = random.choice(list_of_number)
                num07 = random.choice(list_of_number)
                num08 = random.choice(list_of_number)
                num09 = random.choice(list_of_number)
                num010 = random.choice(list_of_number)
                num011 = random.choice(list_of_number)
                num012 = random.choice(list_of_number)
                list_of_numberplus131331 = [num01 * 1, num02 * 3, num03 * 1, num04 * 3, num05 * 1, num06 * 3, num07 * 1,
                                            num08 * 3, num09 * 1, num010 * 3, num011 * 1, num012 * 3]
                number = str(num01) + str(num02) + str(num03) + str(num04) + str(num05) + str(num06) + str(num07) + str(
                    num08) + str(num09) + str(num010) + str(num011) + str(num012)
                mycode = EAN13(number, writer=ImageWriter())
                somme_totale = sum(list_of_numberplus131331)
                clede_controle = (somme_totale % 10) - 10
                cle = str(abs(clede_controle))
                print(cle)
                filtre_duproblemede10 = ""
                if cle == "10":
                    filtre_duproblemede10 = "0"
                else:
                    filtre_duproblemede10 = cle
                codebarepouelabasededonnee = str(number) + str(filtre_duproblemede10)
                mycode.save(f"code/{str(number)}{filtre_duproblemede10}")
                # generateurdebarcode    fin   fin fin ---------------------------------------------------------------
                # *************************************************************************************************
                # *************************************************************************************************
                # *************************************************************************************************
                # *************************************************************************************************
                mydb = sqlite3.connect("mydatabase.db")
                cur = mydb.cursor()
                cur.execute(
                    """INSERT INTO produits(name , codebarr ,prix_achat , prixde_vente, remise_ , dateso , timeso , note_) VALUES (?,?,?,?,?,date('now'),time('now', 'localtime'),?)""",
                    (
                        name_Entry001.get().lower(),
                        codebarepouelabasededonnee,
                        name_EntryPrixachat001.get(),
                        name_EntryPrixventet001.get(),
                        name_Entryremise001.get().lower() ,
                        name_Entrynote1.get().lower()
                    ))
                mydb.commit()
                mydb.close()
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                print("temps de pause")
                mydb = sqlite3.connect("mydatabase.db")
                cur = mydb.cursor()
                resul0254136 = cur.execute(
                    """SELECT id ,name,COUNT(*),prix_achat,prixde_vente,remise_,dateso ,timeso ,note_  from produits group by name """)
                resul0254136 = list(resul0254136)
                for khddfgjh in tree02.get_children():
                    tree02.delete(khddfgjh)
                for polkoik in resul0254136:
                    print(str(polkoik))
                    if numberofpr_dect == convert:
                        tree02.insert("", END, value=polkoik)
                        name_Entry001.delete(0, END)
                        name_EntryPrixachat001.delete(0, END)
                        name_Entryremise001.delete(0, END)
                        name_EntryPrixventet001.delete(0, END)
                        name_Entrynote1.delete(0, END)
                        name_Entry001forquantite.delete(0, END)
                    else:
                        pass

                mydb.commit()
                mydb.close()
                numberofpr_dect = numberofpr_dect + plusnumber
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                print("respiration")
                capitalisationtotla887()

        name_produitsarticl = Label(top, text="Nom :", font=('Times', 12, 'bold'))
        name_produitsarticl.place(x=20, y=40)
        quantite_de_produits = Label(top, text="Quantité  :", font=('Times', 12, 'bold'))
        quantite_de_produits.place(x=20, y=400)
        name_Entry001forquantite = Entry(top, font=('Times', 12, 'bold'))
        name_Entry001forquantite.place(x=100, y=400, width=100, height=30)
        name_prixdachat = Label(top, text="Prix d'achat :", font=('Times', 12, 'bold'))
        name_prixdachat.place(x=20, y=100)
        name_prixddevente = Label(top, text="Prix de vente :", font=('Times', 12, 'bold'))
        name_prixddevente.place(x=20, y=160)
        name_remis_erd = Label(top, text="Remise :", font=('Times', 12, 'bold'))
        name_remis_erd.place(x=20, y=220)
        name_notesr = Label(top, text="Notes :", font=('Times', 12, 'bold'))
        name_notesr.place(x=20, y=280)
        name_barcode_ = Label(top, text="BarCode : Will be generated automatically", font=('Times', 12, 'bold'))
        name_barcode_.place(x=20, y=350)
        name_Entry001 = Entry(top, font=('Times', 12, 'bold'))
        name_Entry001.place(x=20, y=65, width=330, height=30)
        name_EntryPrixachat001 = Entry(top, font=('Times', 12, 'bold'))
        name_EntryPrixachat001.place(x=20, y=125, width=330, height=30)
        name_EntryPrixventet001 = Entry(top, font=('Times', 12, 'bold'))
        name_EntryPrixventet001.place(x=20, y=185, width=330, height=30)
        name_Entryremise001 = Entry(top, font=('Times', 12, 'bold'))
        name_Entryremise001.place(x=20, y=245, width=330, height=30)
        name_Entrynote1 = Entry(top, font=('Times', 12, 'bold'))
        name_Entrynote1.place(x=20, y=305, width=330, height=30)
        buttonadd_ = Button(top, text="Add article", command=add_new_article_boutton)
        buttonadd_.place(x=340, y=380, width=150, height=70)
        buttoncencel_ = Button(top, text="Cancel", command=top.destroy)
        buttoncencel_.place(x=340, y=460, width=150, height=30)


    framforstokemanage = Frame(frameAdmin, height=700, width=w)
    framforstokemanage.place(x=0, y=60)

    gros_titre_dutreeview = Label(framforstokemanage, text="All articles", font=('Times', 12, 'bold'))
    gros_titre_dutreeview.place(x=300, y=0)
    tree02 = ttk.Treeview(framforstokemanage, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), height=23, show="headings")
    vsb = ttk.Scrollbar(framforstokemanage, orient="vertical", command=tree02.yview)
    vsb.place(x=1313, y=21, height=585)
    tree02.configure(yscrollcommand=vsb.set)
    tree02.place(x=265, y=20, width=1050)
    tree02.column(1, width=5, anchor=CENTER)
    tree02.column(2, width=60, anchor=CENTER)
    tree02.column(3, width=5, anchor=CENTER)
    tree02.column(4, width=40, anchor=CENTER)
    tree02.column(5, width=40, anchor=CENTER)
    tree02.column(6, width=40, anchor=CENTER)
    tree02.column(7, width=40, anchor=CENTER)
    tree02.column(8, width=40, anchor=CENTER)
    tree02.column(9)
    tree02.heading(1, text="Id", anchor=CENTER)
    tree02.heading(2, text="Name", anchor=CENTER)
    tree02.heading(3, text="Quantité", anchor=CENTER)
    tree02.heading(4, text="Prix De Gros", anchor=CENTER)
    tree02.heading(5, text="Prix Unité", anchor=CENTER)
    tree02.heading(6, text="Remise", anchor=CENTER)
    tree02.heading(7, text="Date d'achat", anchor=CENTER)
    tree02.heading(8, text="Heure", anchor=CENTER)
    tree02.heading(9, text="Notes", anchor=CENTER)

  
    bouton_delete_all = Button(framforstokemanage, text="supprimer tout les articles", bd=1,
                               command=delete_allfromtree02)  # bouton supprimer un nouvel article
    bouton_delete_all.place(x=10, y=200, width=245, height=30)
    bouton_delete_oneprodect = Button(framforstokemanage, text="Supprimer l'article", bd=1,
                                      command=delete_jsuteoneselected)  # bouton supprimer un nouvel article
    bouton_delete_oneprodect.place(x=10, y=160, width=245, height=30)
   


###########################################################manuel add articl ########################################################################################
###########################################################manuel add articl ########################################################################################
###########################################################manuel add articl ########################################################################################
###########################################################manuel add articl ########################################################################################
    def xoxoadd_new_article_boutton():
        myfiles = os.listdir("C:/Users/Hp/Desktop/mohand")

        # C:/Users/User/Desktop/Rkale
        if "code" not in myfiles:
            os.mkdir("C:/Users/Hp/Desktop/mohand/code")
        numberofpr_dect = 1
        plusnumber = 1
        convert = 1
        while (numberofpr_dect <= convert):
            # generateurdebarcode------------------------------------------------------------------------------
            # *************************************************************************************************
            # *************************************************************************************************
            # *************************************************************************************************
            # *************************************************************************************************
            list_of_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            num01 = random.choice(list_of_number)
            num02 = random.choice(list_of_number)
            num03 = random.choice(list_of_number)
            num04 = random.choice(list_of_number)
            num05 = random.choice(list_of_number)
            num06 = random.choice(list_of_number)
            num07 = random.choice(list_of_number)
            num08 = random.choice(list_of_number)
            num09 = random.choice(list_of_number)
            num010 = random.choice(list_of_number)
            num011 = random.choice(list_of_number)
            num012 = random.choice(list_of_number)
            list_of_numberplus131331 = [num01 * 1, num02 * 3, num03 * 1, num04 * 3, num05 * 1, num06 * 3, num07 * 1,
                                        num08 * 3, num09 * 1, num010 * 3, num011 * 1, num012 * 3]
            number = str(num01) + str(num02) + str(num03) + str(num04) + str(num05) + str(num06) + str(num07) + str(
                num08) + str(num09) + str(num010) + str(num011) + str(num012)
            mycode = EAN13(number, writer=ImageWriter())
            somme_totale = sum(list_of_numberplus131331)
            clede_controle = (somme_totale % 10) - 10
            cle = str(abs(clede_controle))
            print(cle)
            filtre_duproblemede10 = ""
            if cle == "10":
                filtre_duproblemede10 = "0"
            else:
                filtre_duproblemede10 = cle
            codebarepouelabasededonnee = str(number) + str(filtre_duproblemede10)
            mycode.save(f"code/{str(number)}{filtre_duproblemede10}")
            # generateurdebarcode    fin   fin fin ---------------------------------------------------------------
            # *************************************************************************************************
            # *************************************************************************************************
            # *************************************************************************************************
            # *************************************************************************************************
            mydb = sqlite3.connect("mydatabase.db")
            cur = mydb.cursor()
            cur.execute(
                """INSERT INTO produits(name , codebarr ,prix_achat , prixde_vente, remise_ , dateso , timeso , note_) VALUES (?,?,?,?,?,date('now'),time('now', 'localtime'),?)""",
                (
                    entry__name01.get().lower(),
                    codebarepouelabasededonnee,
                    entry__name02.get(),
                    entry__name03.get(),
                    entry__name04.get().lower() ,
                    entry__name05.get().lower()
                ))
            mydb.commit()
            mydb.close()
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            print("temps de pause")
            mydb = sqlite3.connect("mydatabase.db")
            cur = mydb.cursor()
            resul0254136 = cur.execute(
                """SELECT id ,name,COUNT(*),prix_achat,prixde_vente,remise_,dateso ,timeso ,note_  from produits group by name """)
            resul0254136 = list(resul0254136)
            for khddfgjh in tree02.get_children():
                tree02.delete(khddfgjh)
            for polkoik in resul0254136:
                print(str(polkoik))
                if numberofpr_dect == convert:
                    tree02.insert("", END, value=polkoik)

                else:
                    pass
            mydb.commit()
            mydb.close()
            numberofpr_dect = numberofpr_dect + plusnumber
            capitalisationtotla887()

        entry__name01.delete(0, END)
        entry__name02.delete(0, END)
        entry__name04.delete(0, END)
        entry__name03.delete(0, END)
        entry__name05.delete(0, END)


    def delete_entry_addoneartces():
        entry__name01.delete(0, END)
        entry__name02.delete(0, END)
        entry__name04.delete(0, END)
        entry__name03.delete(0, END)
        entry__name05.delete(0, END)


    frame_foradd_nw_articl = Frame(framforstokemanage, width=260, height=360)
    frame_foradd_nw_articl.place(x=0, y=280)
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Lbl_Namex01 = Label(frame_foradd_nw_articl, text="nom", font=('arial', 12, 'bold'))
    Lbl_Namex01.place(x=5, y=10)
    entry__name01 = Entry(frame_foradd_nw_articl, font=('arial', 12, 'bold'))
    entry__name01.place(x=5, y=40, width=230, height=25)
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Lbl_Namex02 = Label(frame_foradd_nw_articl, text="Prix d'achat :", font=('arial', 12, 'bold'))
    Lbl_Namex02.place(x=5, y=70)
    entry__name02 = Entry(frame_foradd_nw_articl, font=('arial', 12, 'bold'))
    entry__name02.place(x=5, y=100, width=230, height=25)
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Lbl_Namex03 = Label(frame_foradd_nw_articl, text="Prix de vente :", font=('arial', 12, 'bold'))
    Lbl_Namex03.place(x=5, y=130)
    entry__name03 = Entry(frame_foradd_nw_articl, font=('arial', 12, 'bold'))
    entry__name03.place(x=5, y=160, width=230, height=25)
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Lbl_Namex04 = Label(frame_foradd_nw_articl, text="Remise :", font=('arial', 12, 'bold'))
    Lbl_Namex04.place(x=5, y=190)
    entry__name04 = Entry(frame_foradd_nw_articl, font=('arial', 12, 'bold'))
    entry__name04.place(x=5, y=220, width=230, height=25)
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Lbl_Namex05 = Label(frame_foradd_nw_articl, text="Note :", font=('arial', 12, 'bold'))
    Lbl_Namex05.place(x=5, y=250)
    entry__name05 = Entry(frame_foradd_nw_articl, font=('arial', 12, 'bold'))
    entry__name05.place(x=5, y=280, width=230, height=25)
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Lbl_Namex06 = Button(frame_foradd_nw_articl, text="Ajouter  ", command=xoxoadd_new_article_boutton)
    Lbl_Namex06.place(x=5, y=310, width=150, height=30)
    Lbl_Namex07 = Button(frame_foradd_nw_articl, text="Effacer ", command=delete_entry_addoneartces)
    Lbl_Namex07.place(x=160, y=310, width=78, height=30)


# search by id

# searching ---------------------------------------------------------------------------------------------------------

    def serach_by_name778():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        get_the_name_prodect_forsearch = str(search_product_Entrysrarchbyidandname.get().lower())
        count___ = cur.execute(f"""SELECT COUNT(*) FROM produits where name ='{get_the_name_prodect_forsearch}'""")
        count___ = list(count___)
        countforselect = str(count___[0][0])
        results_of_our_serach = cur.execute(
            f"""SELECT id ,name,'{countforselect}',prix_achat,prixde_vente,remise_ ,dateso ,timeso,note_ from produits where name = '{get_the_name_prodect_forsearch}'""")
        results_of_our_serach = list(results_of_our_serach)
        for xcox85 in tree02.get_children():
            tree02.delete(xcox85)
        for xoxo774 in results_of_our_serach:
            tree02.insert("", END, value=xoxo774)
        # print(xoxo774[2])
        lblforresults__7 = Label(framforstokemanage,
                                 text="Le Nombre Total de produits trouver dans votre recherche est de : " + countforselect + " produits trouvers ",
                                 font=('arial', 12, 'bold'))
        lblforresults__7.place(x=280, y=510)

        mydb.commit()
        mydb.close()


    def serach_by_barrecode778():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        get_the_name_prodect_forsearch9 = int(search_product_Entrysrarchbyidandname.get())
        results_of_our_serach9 = cur.execute(
            f"""SELECT id ,name,COUNT(*),prix_achat,prixde_vente,remise_ ,dateso ,timeso,note_ from produits where codebarr = '{get_the_name_prodect_forsearch9}' group by name""")
        results_of_our_serach9 = list(results_of_our_serach9)
        for xcox859 in tree02.get_children():
            tree02.delete(xcox859)
        for xoxo7749 in results_of_our_serach9:
            tree02.insert("", END, value=xoxo7749)

        mydb.commit()
        mydb.close()


    btn_forsearch = Button(framforstokemanage, text="trouver avec nom", bd=1, command=serach_by_name778)
    btn_forsearch.place(x=10, y=120, width=245, height=30)
    search_product_labelbycb = Label(framforstokemanage, text="Recherche", font=('Times', 12, 'bold'))
    search_product_labelbycb.place(x=10, y=0)
    search_product_Entrysrarchbyidandname = Entry(framforstokemanage, font=('Times', 18, 'bold'))
    search_product_Entrysrarchbyidandname.place(x=10, y=22, width=245)
    
    mydb = sqlite3.connect("mydatabase.db")
    cur = mydb.cursor()
    FFFFFF55 = cur.execute(
        """SELECT id ,name,COUNT(*),prix_achat,prixde_vente,remise_,dateso ,timeso,note_ from produits group by name """)
    FFFFFF55 = list(FFFFFF55)
    for polkoikFH in FFFFFF55:
        print(str(polkoikFH))
        tree02.insert("", END, value=polkoikFH)
    mydb.commit()
    mydb.close()

 
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    #################################################################################Filtrage par date commencement
    def filtre_between():

        mydb = sqlite3.connect('mydatabase.db')
        cur = mydb.cursor()
        jour01 = str(combo12.get())
        mois01 = str(combo14.get())
        annee01 = str(combo15.get())
        jour02 = str(combo12x.get())
        mois02 = str(combo14x.get())
        annee02 = str(combo15x.get())
        date__01 = annee01+"-"+mois01+"-"+jour01
        date__02 = annee02+"-"+mois02+"-"+jour02
        print(date__01)
        print(date__02)
        sosoresultas_ = cur.execute(f"""SELECT id ,name,COUNT(name),prix_achat,prixde_vente,remise_,dateso ,timeso ,note_  FROM produits where dateso BETWEEN '{date__01}' AND '{date__02}' group by name""")
        sosoresultas_ = list(sosoresultas_)
        for nulsexo in tree02.get_children():
            tree02.delete(nulsexo)
        for kolpmllm in sosoresultas_:
            tree02.insert("",END,value=kolpmllm)
        mydb.commit()
        mydb.close()
    def filtre_between_article():

        mydb = sqlite3.connect('mydatabase.db')
        cur = mydb.cursor()
        jour01 = str(combo12.get())
        mois01 = str(combo14.get())
        annee01 = str(combo15.get())
        jour02 = str(combo12x.get())
        mois02 = str(combo14x.get())
        annee02 = str(combo15x.get())
        date__01 = annee01+"-"+mois01+"-"+jour01
        date__02 = annee02+"-"+mois02+"-"+jour02
        print(date__01)
        print(date__02)
        sosoresultas_ = cur.execute(f"""SELECT id ,name,"Article",prix_achat,prixde_vente,remise_,dateso ,timeso ,note_  FROM produits where dateso BETWEEN '{date__01}' AND '{date__02}' order by id""")
        sosoresultas_ = list(sosoresultas_)
        for nulsexo in tree02.get_children():
            tree02.delete(nulsexo)
        for kolpmllm in sosoresultas_:
            tree02.insert("",END,value=kolpmllm)
        mydb.commit()
        mydb.close()


    frm_forserachbydate = Frame(framforstokemanage , height = 0 , width=0 )
    frm_forserachbydate.place(x= 0 , y= 0)
    lbl01 = Label(frm_forserachbydate,text="" , font =("arial", 16 , "bold"))
    lbl01.place(x= 0 , y= 0)
    lbl010 = Label(frm_forserachbydate,text="" , font =("arial", 14))
    lbl010.place(x= 0 , y= 0)
    listjours12 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    combo12 = ttk.Combobox(frm_forserachbydate,values = listjours12,font=("Times", 14, "bold"))
    combo12.current(17)
    combo12.place(x=0, y=0, width="0", height="0")
    #--------------------------------------------------------------------------------------------------------------------------------
    listof_type =["01","02","03","04","05","06","07","08","09","10","11","12"]
    combo14 = ttk.Combobox(frm_forserachbydate,values = listof_type,font=("Times", 14, "bold"))
    combo14.current(5)
    combo14.place(x=0, y=0, width="0", height="0")
    #--------------------------------------------------------------------------------------------------------------------------------
    listdanes = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100]
    combo15 = ttk.Combobox(frm_forserachbydate,values = listdanes,font=("Times", 16, "bold"))
    combo15.current(21)
    combo15.place(x=0, y=0, width="0", height="0")
    #--------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------------

    
    lbl016 = Label(frm_forserachbydate,text="" , font =("arial", 14))
    lbl016.place(x= 0 , y= 0)
    listjours13 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    combo12x = ttk.Combobox(frm_forserachbydate,values = listjours13,font=("Times", 14, "bold"))
    combo12x.current(18)
    combo12x.place(x=0, y=0, width="0", height="0")
    #--------------------------------------------------------------------------------------------------------------------------------
    listof_typex =["01","02","03","04","05","06","07","08","09","10","11","12"]
    combo14x = ttk.Combobox(frm_forserachbydate,values = listof_typex,font=("Times", 14, "bold"))
    combo14x.current(5)
    combo14x.place(x=429, y=50, width="0", height="0")
    #--------------------------------------------------------------------------------------------------------------------------------
    listdanesx = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100]
    combo15x = ttk.Combobox(frm_forserachbydate,values = listdanesx,font=("Times", 16, "bold"))
    combo15x.current(21)
    combo15x.place(x=0, y=0, width="0", height="0")
   
  
    mydb = sqlite3.connect('mydatabase.db')
    cur = mydb.cursor()
    def capitalisationtotla887():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        sosoresultas_aa = cur.execute("""SELECT SUM(prix_achat) ,COUNT(*) FROM produits """)
        sosoresultas_aa = list(sosoresultas_aa)
        for yujhnj in sosoresultas_aa:
            capitalisationni = " Avec une Capitalisation total de : " + str(yujhnj[0]) +" DA راس المال  "
            lenombredrticletotal = " Vous avez : " +str(yujhnj[1]) + " Articles dans votre stocke"
            tot02020 =  str(lenombredrticletotal) + str(capitalisationni) 
            print(capitalisationni)
            labelcapitalisationtotal = Label(framforstokemanage , text=tot02020 , font=('arial' , 10 , 'bold'))
            labelcapitalisationtotal.place(x= 490 , y = 0 , height=20)
        mydb.commit()
        mydb.close()

    capitalisationtotla887()
    

    noteajouterunseulproduit = Label(framforstokemanage , text="Ajouter un seul Produit" , font=('arial' , 11 , 'bold'))
    noteajouterunseulproduit.place(x= 10 , y = 240)

    
btncreateuser = Button(frameAdmin, text="Gestion d'utilisateurs", command=createuser, bd=0, bg='#007BF7', fg="#FFFFFF",
                       font=('arial', 11, 'bold'), relief=FLAT, activebackground="#FFFFFF", activeforeground='#007BF7')
btncreateuser.place(x=10, y=10, width="170", height=50)
btnstockemaneg = Button(frameAdmin, text="Gestion de Stockage", command=stokemanage, bd=0, bg='#007BF7', fg="#FFFFFF",
                        font=('arial', 11, 'bold'), relief=FLAT, activebackground="#FFFFFF", activeforeground='#007BF7')
btnstockemaneg.place(x=190, y=10, width="170", height=50)
btnstockemaneg011 = Button(frameAdmin, text="Quiter", command=quit, bd=0, bg='#FA8072', fg="#FFFFFF",
                           font=('arial', 10, 'bold'), relief=FLAT, activebackground="#FFFFFF",
                           activeforeground='#007BF7')
btnstockemaneg011.place(x=1230, y=10, width="120", height=20)
btnstockemaneg011 = Button(framelogin, text="Quiter", command=quit, bd=0, bg='#FA8072', fg="#FFFFFF",
                           font=('arial', 10, 'bold'), relief=FLAT, activebackground="#FFFFFF",
                           activeforeground='#007BF7')
btnstockemaneg011.place(x=1230, y=10, width="120", height=20)
btndescounnect = Button(frameAdmin, text="Se Déconnecter", command=lambda: [swap(framelogin)], bd=0, bg='#FA8072',
                        fg="#FFFFFF", font=('arial', 10, 'bold'), relief=FLAT, activebackground="#FFFFFF",
                        activeforeground='#007BF7')
btndescounnect.place(x=1230, y=40, width="120", height=20)
btnstockemaneg011frmuser = Button(frameuser, text="Quiter", command=quit, bd=0, bg='#FA8072', fg="#FFFFFF",
                           font=('arial', 10, 'bold'), relief=FLAT, activebackground="#FFFFFF",
                           activeforeground='#007BF7')
btnstockemaneg011frmuser.place(x=1230, y=10, width="120", height=20)
btndescounnectfrmuser = Button(frameuser, text="Se Déconnecter", command=lambda: [swap(framelogin)], bd=0, bg='#FA8072',
                        fg="#FFFFFF", font=('arial', 10, 'bold'), relief=FLAT, activebackground="#FFFFFF",
                        activeforeground='#007BF7')
btndescounnectfrmuser.place(x=1230, y=40, width="120", height=20)

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
#mode caisse#mode caisse#mode caisse
def modecaisserkale():
    def desplay_time():
       current_time = tm.strftime('%H:%M:%p')
       clock_label ['text'] = current_time
       clock_label.after(200,desplay_time)
    def desplay_timeseconde():
       secondes___8 = tm.strftime('%S')
       clock_labelsec ['text'] = secondes___8
       clock_labelsec.after(200,desplay_timeseconde)
    

    def fonction___de_remise():
        
        del latotal_dupanier874[:]

        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        lelement_amodiferdans_treemodecaisse = treemodecaisse.item(treemodecaisse.selection())["values"][5]
        ancienprix_treemodecaisse = treemodecaisse.item(treemodecaisse.selection())["values"][2]
        equation_pour_la_remise = ancienprix_treemodecaisse - int(entry_7421000p.get())
        for iokloik in treemodecaisse.get_children():
            treemodecaisse.delete(iokloik)
        print(lelement_amodiferdans_treemodecaisse)

        cur.execute(f"""UPDATE produits SET prixde_vente = '{int(equation_pour_la_remise)}' where codebarr ='{int(lelement_amodiferdans_treemodecaisse)}' """)
        mydb.commit()
        for mybarcodeinmylis__  in list_codeused:
            list_articles_howremisearactived = cur.execute(f"""SELECT name,"Remise activee",prixde_vente,remise_ ,note_, codebarr from produits where codebarr ='{int(mybarcodeinmylis__)}' """)
            list_articles_howremisearactived = list(list_articles_howremisearactived)
            for koikmlk in list_articles_howremisearactived :
                treemodecaisse.insert("" , END , values = koikmlk)
                latotal_dupanier874.append(koikmlk[2])
        print(latotal_dupanier874)
        sumtotal_du_add_simillarrarticfonction_de_remise = sum(latotal_dupanier874)
        Labeltotaldescours_add_simillarrarticles_852_fonctionderemise = Label(framesousmodecaisse , text = "Total : " + str(sumtotal_du_add_simillarrarticfonction_de_remise) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescours_add_simillarrarticles_852_fonctionderemise.place(x = 730, y =125 ,width=240)
        entry_7421000p.delete(0,END)


        mydb.commit()
        mydb.close()
        
    def affichermkldk():
        for iokloik in treemodecaisse.get_children():
            treemodecaisse.delete(iokloik)
        del latotal_dupanier874[:]
        sumtotal_du_add_simillarrarticaffichermkldk = sum(latotal_dupanier874)
        Labeltotaldescours_add_simillarrarticles_852_affichermkldk = Label(framesousmodecaisse , text = "Total : " + str(sumtotal_du_add_simillarrarticaffichermkldk) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescours_add_simillarrarticles_852_affichermkldk.place(x = 730, y =125 ,width=240)

        
    def confimation_du_panier_01():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        for xvnbct_12 in list_codeused:
            infomartion_to_insertinpv = cur.execute(f"""SELECT name , prix_achat ,prixde_vente , remise_  from produits where codebarr = '{xvnbct_12}'""")
            infomartion_to_insertinpv = list(infomartion_to_insertinpv)
            for chichi85 in infomartion_to_insertinpv:
                xxxx1 = chichi85[0]
                xxxx2 = chichi85[1]
                xxxx3 = chichi85[2]
                xxxx4 = chichi85[3]
                print(xxxx1)
                print(xxxx2)
                print(xxxx3)
                print(xxxx4)
        cur.execute("""INSERT INTO  produit_vendu (namev ,prix_achatv, prixde_ventev , remise_v , datesov ,timesov) VALUES(?,?,?,?,date('now'),time('now', 'localtime'))""",(xxxx1,xxxx2,xxxx3,xxxx4))        

        mydb.commit()
        mydb.close()
        #print("Confirmation du panier s'execute tres bien")
        #print(list_codeused)

    def add_simillarrarticles_852():
        llllllllllllllllll = 1
        print('sa roule')
        selected___prodectforaddsimillar__ = treemodecaisse.item(treemodecaisse.selection())["values"][0]
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        rrrrrforsimillararticles___85 = cur.execute(f"""
                        SELECT name,"Produit ajouter",prixde_vente,remise_ ,note_, codebarr from produits where name = '{selected___prodectforaddsimillar__}' group by name """)
        rrrrrforsimillararticles___85 = list(rrrrrforsimillararticles___85)
        for luiokdh in rrrrrforsimillararticles___85:
            while llllllllllllllllll <= int(ajouterdelaquantit.get()):
                treemodecaisse.insert("" , END , values =luiokdh )
                print(luiokdh[2])
                latotal_dupanier874.append(luiokdh[2])
                list_codeused.append(luiokdh[4])
                llllllllllllllllll = llllllllllllllllll + 1

        sumtotal_du_add_simillarrarticles_852 = sum(latotal_dupanier874)
        Labeltotaldescours_add_simillarrarticles_852 = Label(framesousmodecaisse , text = "Total : " + str(sumtotal_du_add_simillarrarticles_852) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescours_add_simillarrarticles_852.place(x = 730, y =125 ,width=240)
        mydb.commit()
        mydb.close()
    def annuler_unarticle885():
        sumtotal_du2 = sum(latotal_dupanier874)

        selected___prodect200 = treemodecaisse.item(treemodecaisse.selection())["values"][0]
        prixxxxxxxxxxxxxxxxxx = treemodecaisse.item(treemodecaisse.selection())["values"][2]
        coddebarre854222 = treemodecaisse.item(treemodecaisse.selection())["values"][5]
        latotal_dupanier874.remove(prixxxxxxxxxxxxxxxxxx)
        list_codeused.remove(str(coddebarre854222))

        
        prixxxxxxxxxxxxxxxxxx = treemodecaisse.item(treemodecaisse.selection())["values"][2]
        ttotalapressoustraction = sumtotal_du2 - int(prixxxxxxxxxxxxxxxxxx)
        Labeltotaldescours8e = Label(framesousmodecaisse , text = "Total : " + str(ttotalapressoustraction) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescours8e.place(x = 730, y =125 ,width=240)
        treemodecaisse.delete(treemodecaisse.selection())
        rendre__actualisation = Label(framesousmodecaisse , text = "" ,bg="#059862",fg="red",font="arial 20 bold")
        rendre__actualisation.place(x = 730, y =210,height=108 ,width=240) 
        
    latotal_dupanier874 = []
    list_codeused=[]
  
    def rendref5_combien():
        sumtotal_du1 = sum(latotal_dupanier874)
        resulatdurendement__120 = int(ecranmonaierapide.get()) - sumtotal_du1
        rendre__ = Label(framesousmodecaisse , text = "Rendre :" + str(resulatdurendement__120)+" DA" ,bg="white",fg="red",font="arial 20 bold")
        rendre__.place(x = 730, y =210,height=108 ,width=240)    

        

    


                    
    
    
    framesousmodecaisse = Frame(frameAdmin, height=700, width=w)
    framesousmodecaisse.place(x=0, y=60)

   
    monnaiearendreresultat = Label(framesousmodecaisse , text="",bg="#059862",fg="#FFFFFF",font="arial 11 bold")
    monnaiearendreresultat .place(x =730 , y = 115 ,height=202 , width=240)
    ecranmonaierapide = Entry(framesousmodecaisse  , borderwidth= 0 , bg="#FFF4A3" ,font=("arial 19 bold"))
    ecranmonaierapide.place(x=730, y =35 ,bordermode=OUTSIDE,height=50,width=240)
    resultasdelamonnaiearendre = Button(framesousmodecaisse , text="monnaie a rendre" ,font=("arial 14 bold") ,bg="#FA8072",fg="#FFFFFF",bd = 0 ,command=rendref5_combien)
    resultasdelamonnaiearendre.place(x=730 , y =85 , width =240 , height =30 )
    button_nouveaupanier =Button(framesousmodecaisse , text="Nouveau \n Panier ⏎" , font=('arial 16 bold') , bd=0 ,bg="#059862",fg="#FFFFFF" )
    button_nouveaupanier.place(x = 1230, y=10, height=150,width=120)
    button_nouveaupanier =Button(framesousmodecaisse , text="Confirmer\nLe Panier " , font=('arial 16 bold') , bd=0 ,bg="#FA8072",fg="#FFFFFF" ,command=confimation_du_panier_01)
    button_nouveaupanier.place(x = 1230, y=167, height=150,width=120)
    imprimmer__bouttton =Button(framesousmodecaisse , text="Imprimer un Ticket ⏎" , font=('arial 16 bold') , bd=0 ,bg="#059862",fg="#FFFFFF")
    imprimmer__bouttton.place(x =980, y=320, height=70,width=240)
    imprimmer__boutttonbon =Button(framesousmodecaisse , text="Imprimer un Bon ⏎" , font=('arial 16 bold') , bd=0 ,bg="#059862",fg="#FFFFFF" )
    imprimmer__boutttonbon.place(x =980, y=400, height=70,width=240)

    clock_label =Label(framesousmodecaisse  , font=('arial 15 bold') , bd=0 ,bg="#059862",fg="#FFFFFF")
    clock_label.place(x = 1230, y=320, height=40,width=120)
    clock_labelsec =Label(framesousmodecaisse  , font=('arial 30 bold') , bd=0 ,bg="#FA8072",fg="#FFFFFF")
    clock_labelsec.place(x = 1230, y=360, height=110,width=120)
    
    desplay_time()
    desplay_timeseconde()
    
    
    ######################## Tree view acticles du panier  ##################################################################
    treemodecaisse = ttk.Treeview(framesousmodecaisse , col=(1,2,3,4,5) , height = 18 , show = "headings")
    treemodecaisse.place(x = 10 , y = 10 ,width=700)
    vsb1 = ttk.Scrollbar(framesousmodecaisse, orient="vertical", command=treemodecaisse.yview)
    vsb1.place(x=709, y=10, height=430)
    treemodecaisse.configure(yscrollcommand=vsb1.set)
    treemodecaisse.heading(1 , text='Nom')
    treemodecaisse.heading(2 , text='Quantité')
    treemodecaisse.heading(3 , text='Prix' )
    treemodecaisse.heading(4 , text='RM MAX' )
    treemodecaisse.heading(5, text='Note' )
    treemodecaisse.column(1 , width=150)
    treemodecaisse.column(2 , width=100)
    treemodecaisse.column(3 , width=100)
    treemodecaisse.column(4 , width=100)
    treemodecaisse.column(5 , width=200)
    
    ajouterdelaquantit = Entry(framesousmodecaisse , font=('arial 25 bold'),bg="#FFF4A3")
    ajouterdelaquantit.place(x =0 , y = 0, width=0 , height=0)
    ajouterdelaquantit.insert(1,1)
  
    Anuler_lepanier =Button(framesousmodecaisse , text="Annuler" , font=('arial 16 bold') , bd=0 ,bg="#059862",fg="#FFFFFF" ,command=annuler_unarticle885)
    Anuler_lepanier.place(x = 416, y=410, height=60,width=295)
    supprimerle_panier =Button(framesousmodecaisse , text="Supprimer\nLe Panier" , font=('arial 16 bold') , bd=0 ,bg="#FA8072",fg="#FFFFFF" ,command=affichermkldk)
    supprimerle_panier.place(x = 10, y=410, height=60,width=295)

    ######optionde remise-----------------------------------------------------------------------------------------------------------------------------
    framer_mise = Frame(framesousmodecaisse , height=150 , width=240 , bg ="#059862")
    framer_mise.place(x = 730 , y = 320)
    lblty____remise = Label(framer_mise , text="Remise", font=("arial 15 bold") ,bg="#007BF7",fg="#FFFFFF")
    lblty____remise.place(x = 0 ,y = 0,width=240)
    entry_7421000p = Entry(framer_mise , font=("arial 20 bold"), bg="#FFF4A3",bd=0)
    entry_7421000p.place(x = 0 , y = 30 , height=50,width=240)
    button__pour_remise = Button(framer_mise , text="Total" , bd = 0 , command = fonction___de_remise , bg="#FA8072",fg="#FFFFFF", font=('arial 16 bold'))
    button__pour_remise.place(x = 5 , y = 100 , height = 30 , width=230)


    ######optionde remise-----------------------------------------------------------------------------------------------------------------------------
    
   

    #btn_forsearch = Button(framesousmodecaisse, text="Find by name", bd=0,bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
    #btn_forsearch.place(x=10, y=55, width=250, height=30)
    #bearch_product_labelbycb = Label(framesousmodecaisse, text="Search:", font=('Times', 12, 'bold'))
    #bearch_product_labelbycb.place(x=10, y=0)
    #bearch_product_Entrysrarchbyidandname = Entry(framesousmodecaisse, font=('Times', 18, 'bold'),bg="#FFF4A3")
    #bearch_product_Entrysrarchbyidandname.place(x=10, y=22, width=530)
    #btn_forsearchbycb = Button(framesousmodecaisse, text="Find by Barcode", bd=0,bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
    #btn_forsearchbycb.place(x=290, y=55, width=250, height=30)
    #btn_tripack88221 = Button(framesousmodecaisse, text="Tri PACK", bd=0,bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
    #btn_tripack88221.place(x=10, y=90, width=250, height=30)
    #btn_tripararticler45 = Button(framesousmodecaisse, text="Tri TOUS", bd=0,bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
    #btn_tripararticler45.place(x=290, y=90, width=250, height=30)

    
    
    

    


    def calculatrice__Rkale():
        frame_pricipale = Frame( framesousmodecaisse, width=240 , height=308 ,bg="#059862" )
        frame_pricipale.place(x = 980 , y = 10)
        fon = "arial 19 "
        fontbu="arial 14 bold"
        ecran = Entry(frame_pricipale  , borderwidth= 0 , font = fon, bg="#FFF4A3" )
        ecran.place(x= 0, y =25 ,bordermode=OUTSIDE,height=50,width=240)
        root.overrideredirect(0)
        #----------------------------------------------

        
        #----------------------------------------------
        btn2 = Button(frame_pricipale , text="0",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn2.place(x =60 , y = 250 ,height=50 , width=60)
        
        #----------------------------------------------#E0E0E0
        btn3 = Button(frame_pricipale , text=",",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn3.place(x =120 , y = 250 ,height=50 , width=60)
        #----------------------------------------------
        
        btn4 = Button(frame_pricipale , text="=",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn4.place(x =180 , y = 250 ,height=50 , width=60)
        
        btn5 = Button(frame_pricipale , text="1",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn5.place(x =0 , y = 200 ,height=50 , width=60)
        
        btn6 = Button(frame_pricipale , text="2",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn6.place(x =60 , y = 200 ,height=50 , width=60)
        
        btn7 = Button(frame_pricipale , text="3",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn7.place(x =120 , y =200  ,height=50 , width=60)
        
        btn8 = Button(frame_pricipale , text="-",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn8.place(x =180 , y = 200 ,height=50 , width=60)
        
        btn9 = Button(frame_pricipale , text="4",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn9 .place(x =0 , y = 150 ,height=50 , width=60)
        btn10 = Button(frame_pricipale , text="5",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn10 .place(x =60 , y =150  ,height=50 , width=60)
        btn11 = Button(frame_pricipale , text="6",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn11 .place(x =120, y = 150 ,height=50 , width=60)
        btn12 = Button(frame_pricipale , text="X",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn12 .place(x =180 , y = 150 ,height=50 , width=60)
        
        btn13 = Button(frame_pricipale , text="7",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn13.place(x =0 , y =100  ,height=50 , width=60)
        btn14 = Button(frame_pricipale , text="8",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn14 .place(x =60 , y =100 ,height=50 , width=60)
        btn15 = Button(frame_pricipale , text="9",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn15 .place(x =120, y = 100 ,height=50 , width=60)
        btn16 = Button(frame_pricipale , text="/",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn16 .place(x =180 , y = 100 ,height=50 , width=60)
        btn17 = Button(frame_pricipale , text="C",borderwidth= 0,bg="#FA8072",fg="#FFFFFF",font="arial 11 bold")
        btn17 .place(x =0 , y = 75 ,height=30 , width=240)
    calculatrice__Rkale()








modecaisserkale()
def modecaisserkaleframeuser():
    def desplay_time():
       current_time = tm.strftime('%H:%M:%p')
       clock_label ['text'] = current_time
       clock_label.after(200,desplay_time)
    def desplay_timeseconde():
       secondes___8 = tm.strftime('%S')
       clock_labelsec ['text'] = secondes___8
       clock_labelsec.after(200,desplay_timeseconde)
    

    def fonction___de_remise():
        
        del latotal_dupanier874[:]

        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        lelement_amodiferdans_treemodecaisse = treemodecaisse.item(treemodecaisse.selection())["values"][5]
        ancienprix_treemodecaisse = treemodecaisse.item(treemodecaisse.selection())["values"][2]
        equation_pour_la_remise = ancienprix_treemodecaisse - int(entry_7421000p.get())
        for iokloik in treemodecaisse.get_children():
            treemodecaisse.delete(iokloik)
        print(lelement_amodiferdans_treemodecaisse)

        cur.execute(f"""UPDATE produits SET prixde_vente = '{int(equation_pour_la_remise)}' where codebarr ='{int(lelement_amodiferdans_treemodecaisse)}' """)
        mydb.commit()
        for mybarcodeinmylis__  in list_codeused:
            list_articles_howremisearactived = cur.execute(f"""SELECT name,"Remise activee",prixde_vente,remise_ ,note_, codebarr from produits where codebarr ='{int(mybarcodeinmylis__)}' """)
            list_articles_howremisearactived = list(list_articles_howremisearactived)
            for koikmlk in list_articles_howremisearactived :
                treemodecaisse.insert("" , END , values = koikmlk)
                latotal_dupanier874.append(koikmlk[2])
        print(latotal_dupanier874)
        sumtotal_du_add_simillarrarticfonction_de_remise = sum(latotal_dupanier874)
        Labeltotaldescours_add_simillarrarticles_852_fonctionderemise = Label(souframepourframeuser , text = "Total : " + str(sumtotal_du_add_simillarrarticfonction_de_remise) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescours_add_simillarrarticles_852_fonctionderemise.place(x = 730, y =125 ,width=240)
        entry_7421000p.delete(0,END)


        mydb.commit()
        mydb.close()
        
    def affichermkldk():
        for iokloik in treemodecaisse.get_children():
            treemodecaisse.delete(iokloik)
        del latotal_dupanier874[:]
        sumtotal_du_add_simillarrarticaffichermkldk = sum(latotal_dupanier874)
        Labeltotaldescours_add_simillarrarticles_852_affichermkldk = Label(souframepourframeuser , text = "Total : " + str(sumtotal_du_add_simillarrarticaffichermkldk) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescours_add_simillarrarticles_852_affichermkldk.place(x = 730, y =125 ,width=240)

        
    def confimation_du_panier_01():
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        for xvnbct_12 in list_codeused:
            infomartion_to_insertinpv = cur.execute(f"""SELECT name , prix_achat ,prixde_vente , remise_  from produits where codebarr = '{xvnbct_12}'""")
            infomartion_to_insertinpv = list(infomartion_to_insertinpv)
            for chichi85 in infomartion_to_insertinpv:
                xxxx1 = chichi85[0]
                xxxx2 = chichi85[1]
                xxxx3 = chichi85[2]
                xxxx4 = chichi85[3]
                print(xxxx1)
                print(xxxx2)
                print(xxxx3)
                print(xxxx4)
        cur.execute("""INSERT INTO  produit_vendu (namev ,prix_achatv, prixde_ventev , remise_v , datesov ,timesov) VALUES(?,?,?,?,date('now'),time('now', 'localtime'))""",(xxxx1,xxxx2,xxxx3,xxxx4))        

        mydb.commit()
        mydb.close()
        #print("Confirmation du panier s'execute tres bien")
        #print(list_codeused)

    def add_simillarrarticles_852():
        llllllllllllllllll = 1
        print('sa roule')
        selected___prodectforaddsimillar__ = treemodecaisse.item(treemodecaisse.selection())["values"][0]
        mydb = sqlite3.connect("mydatabase.db")
        cur = mydb.cursor()
        rrrrrforsimillararticles___85 = cur.execute(f"""
                        SELECT name,"Produit ajouter",prixde_vente,remise_ ,note_, codebarr from produits where name = '{selected___prodectforaddsimillar__}' group by name """)
        rrrrrforsimillararticles___85 = list(rrrrrforsimillararticles___85)
        for luiokdh in rrrrrforsimillararticles___85:
            while llllllllllllllllll <= int(ajouterdelaquantit.get()):
                treemodecaisse.insert("" , END , values =luiokdh )
                print(luiokdh[2])
                latotal_dupanier874.append(luiokdh[2])
                list_codeused.append(luiokdh[4])
                llllllllllllllllll = llllllllllllllllll + 1

        sumtotal_du_add_simillarrarticles_852 = sum(latotal_dupanier874)
        Labeltotaldescours_add_simillarrarticles_852 = Label(souframepourframeuser , text = "Total : " + str(sumtotal_du_add_simillarrarticles_852) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescours_add_simillarrarticles_852.place(x = 730, y =125 ,width=240)
        mydb.commit()
        mydb.close()
    def annuler_unarticle885():
        sumtotal_du2 = sum(latotal_dupanier874)

        selected___prodect200 = treemodecaisse.item(treemodecaisse.selection())["values"][0]
        prixxxxxxxxxxxxxxxxxx = treemodecaisse.item(treemodecaisse.selection())["values"][2]
        coddebarre854222 = treemodecaisse.item(treemodecaisse.selection())["values"][5]
        latotal_dupanier874.remove(prixxxxxxxxxxxxxxxxxx)
        list_codeused.remove(str(coddebarre854222))

        
        prixxxxxxxxxxxxxxxxxx = treemodecaisse.item(treemodecaisse.selection())["values"][2]
        ttotalapressoustraction = sumtotal_du2 - int(prixxxxxxxxxxxxxxxxxx)
        Labeltotaldescours8e = Label(souframepourframeuser , text = "Total : " + str(ttotalapressoustraction) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescours8e.place(x = 730, y =125 ,width=240)
        treemodecaisse.delete(treemodecaisse.selection())
        rendre__actualisation = Label(souframepourframeuser , text = "" ,bg="#059862",fg="red",font="arial 20 bold")
        rendre__actualisation.place(x = 730, y =210,height=108 ,width=240) 
        
    latotal_dupanier874 = []
    list_codeused=[]
    def nouveau_panier_bs():
        
        status_dupanier = True
        cap = cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)
        while status_dupanier == True:
            succes, frame = cap.read()
            for code in decode(frame):
                if code.data.decode("utf-8") not in list_codeused:
                    list_codeused.append(code.data.decode("utf-8"))
                    mydb = sqlite3.connect("mydatabase.db")
                    cur = mydb.cursor()
                    barcode_8562 = code.data.decode("utf-8")
                    resuled_barcodemodecaisse = cur.execute(f"""
                        SELECT name,COUNT(*),prixde_vente,remise_,note_,codebarr  from produits where codebarr = '{code.data.decode("utf-8")}' group by name """)
                    time.sleep(0.2)
                    resuled_barcodemodecaisse = list(resuled_barcodemodecaisse)
                    for olkoikll77_85 in resuled_barcodemodecaisse:
                        treemodecaisse.insert("" , END , values = olkoikll77_85)
                    resuled_barcodemodecaissepoursum = cur.execute(f"""
                        SELECT prixde_vente from produits where codebarr = '{code.data.decode("utf-8")}' group by name """)
                    resuled_barcodemodecaissepoursum=list(resuled_barcodemodecaissepoursum)
                    
                    for iknjou51 in resuled_barcodemodecaissepoursum:
                        latotal_dupanier874.append(*iknjou51)
                    print(type(latotal_dupanier874))
                    mydb.commit()
                    mydb.close()
                    status_dupanier = False
                else:
                    status_dupanier = False
            cv2.imshow('salut',frame)
            cv2.waitKey(1)
        sumtotal_du = sum(latotal_dupanier874)
        Labeltotaldescourse = Label(souframepourframeuser , text = "Total : " + str(sumtotal_du) + " DA" ,bg="#059862",fg="#FFFFFF",font="arial 20 bold")
        Labeltotaldescourse.place(x = 730, y =125,width=240 )
        print(sumtotal_du) 
    def rendref5_combien():
        sumtotal_du1 = sum(latotal_dupanier874)
        resulatdurendement__120 = int(ecranmonaierapide.get()) - sumtotal_du1
        rendre__ = Label(souframepourframeuser , text = "Rendre :" + str(resulatdurendement__120)+" DA" ,bg="white",fg="red",font="arial 20 bold")
        rendre__.place(x = 730, y =210,height=108 ,width=240)    

        

    


                    
    
    
    souframepourframeuser = Frame(frameuser, height=700, width=w)
    souframepourframeuser.place(x=0, y=60)
    

    monnaiearendreresultat = Label(souframepourframeuser , text="",bg="#059862",fg="#FFFFFF",font="arial 11 bold")
    monnaiearendreresultat .place(x =730 , y = 115 ,height=202 , width=240)
    ecranmonaierapide = Entry(souframepourframeuser  , borderwidth= 0 , bg="#FFF4A3" ,font=("arial 19 bold"))
    ecranmonaierapide.place(x=730, y =35 ,bordermode=OUTSIDE,height=50,width=240)
    resultasdelamonnaiearendre = Button(souframepourframeuser , text="monnaie a rendre" ,font=("arial 14 bold") ,bg="#FA8072",fg="#FFFFFF",bd = 0 ,command=rendref5_combien)
    resultasdelamonnaiearendre.place(x=730 , y =85 , width =240 , height =30 )
    button_nouveaupanier =Button(souframepourframeuser , text="Nouveau \n Panier ⏎" , font=('arial 16 bold') , bd=0 ,bg="#059862",fg="#FFFFFF" ,command=nouveau_panier_bs)
    button_nouveaupanier.place(x = 1230, y=10, height=150,width=120)
    button_nouveaupanier =Button(souframepourframeuser , text="Confirmer\nLe Panier " , font=('arial 16 bold') , bd=0 ,bg="#FA8072",fg="#FFFFFF" ,command=confimation_du_panier_01)
    button_nouveaupanier.place(x = 1230, y=167, height=150,width=120)
    imprimmer__bouttton =Button(souframepourframeuser , text="Imprimer un Ticket ⏎" , font=('arial 16 bold') , bd=0 ,bg="#059862",fg="#FFFFFF")
    imprimmer__bouttton.place(x =980, y=320, height=70,width=240)
    imprimmer__boutttonbon =Button(souframepourframeuser , text="Imprimer un Bon ⏎" , font=('arial 16 bold') , bd=0 ,bg="#059862",fg="#FFFFFF" )
    imprimmer__boutttonbon.place(x =980, y=400, height=70,width=240)

    clock_label =Label(souframepourframeuser  , font=('arial 15 bold') , bd=0 ,bg="#059862",fg="#FFFFFF")
    clock_label.place(x = 1230, y=320, height=40,width=120)
    clock_labelsec =Label(souframepourframeuser  , font=('arial 30 bold') , bd=0 ,bg="#FA8072",fg="#FFFFFF")
    clock_labelsec.place(x = 1230, y=360, height=110,width=120)
    
    desplay_time()
    desplay_timeseconde()
    
    
    ######################## Tree view acticles du panier  ##################################################################
    treemodecaisse = ttk.Treeview(souframepourframeuser , col=(1,2,3,4,5) , height = 18 , show = "headings")
    treemodecaisse.place(x = 10 , y = 10 ,width=700)
    vsb1 = ttk.Scrollbar(souframepourframeuser, orient="vertical", command=treemodecaisse.yview)
    vsb1.place(x=709, y=10, height=430)
    treemodecaisse.configure(yscrollcommand=vsb1.set)
    treemodecaisse.heading(1 , text='Nom')
    treemodecaisse.heading(2 , text='Quantité')
    treemodecaisse.heading(3 , text='Prix' )
    treemodecaisse.heading(4 , text='Remise' )
    treemodecaisse.heading(5, text='Note' )
    treemodecaisse.column(1 , width=150)
    treemodecaisse.column(2 , width=100)
    treemodecaisse.column(3 , width=100)
    treemodecaisse.column(4 , width=100)
    treemodecaisse.column(5 , width=200)
    
    ajouterdelaquantit = Entry(souframepourframeuser , font=('arial 25 bold'),bg="#FFF4A3")
    ajouterdelaquantit.place(x =307 , y = 410, width=65 , height=60)
    ajouterdelaquantit.insert(1,1)
   
    Anuler_lepanier =Button(souframepourframeuser , text="Annuler" , font=('arial 16 bold') , bd=0 ,bg="#059862",fg="#FFFFFF" ,command=annuler_unarticle885)
    Anuler_lepanier.place(x = 416, y=410, height=60,width=295)
    supprimerle_panier =Button(souframepourframeuser , text="Supprimer\nLe Panier" , font=('arial 16 bold') , bd=0 ,bg="#FA8072",fg="#FFFFFF" ,command=affichermkldk)
    supprimerle_panier.place(x = 10, y=410, height=60,width=295)

    ######optionde remise-----------------------------------------------------------------------------------------------------------------------------
    framer_mise = Frame(souframepourframeuser , height=150 , width=240 , bg ="#059862")
    framer_mise.place(x = 730 , y = 320)
    lblty____remise = Label(framer_mise , text="Remise", font=("arial 15 bold") ,bg="#007BF7",fg="#FFFFFF")
    lblty____remise.place(x = 0 ,y = 0,width=240)
    entry_7421000p = Entry(framer_mise , font=("arial 20 bold"), bg="#FFF4A3",bd=0)
    entry_7421000p.place(x = 0 , y = 30 , height=50,width=240)
    button__pour_remise = Button(framer_mise , text="Activer la Remise" , bd = 0 , command = fonction___de_remise , bg="#FA8072",fg="#FFFFFF", font=('arial 16 bold'))
    button__pour_remise.place(x = 5 , y = 100 , height = 30 , width=230)


    ######optionde remise-----------------------------------------------------------------------------------------------------------------------------
    
   

    #btn_forsearch = Button(souframepourframeuser, text="Find by name", bd=0,bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
    #btn_forsearch.place(x=10, y=55, width=250, height=30)
    #bearch_product_labelbycb = Label(souframepourframeuser, text="Search:", font=('Times', 12, 'bold'))
    #bearch_product_labelbycb.place(x=10, y=0)
    #bearch_product_Entrysrarchbyidandname = Entry(souframepourframeuser, font=('Times', 18, 'bold'),bg="#FFF4A3")
    #bearch_product_Entrysrarchbyidandname.place(x=10, y=22, width=530)
    #btn_forsearchbycb = Button(souframepourframeuser, text="Find by Barcode", bd=0,bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
    #btn_forsearchbycb.place(x=290, y=55, width=250, height=30)
    #btn_tripack88221 = Button(souframepourframeuser, text="Tri PACK", bd=0,bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
    #btn_tripack88221.place(x=10, y=90, width=250, height=30)
    #btn_tripararticler45 = Button(souframepourframeuser, text="Tri TOUS", bd=0,bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
    #btn_tripararticler45.place(x=290, y=90, width=250, height=30)

    
    
    

    


    def calculatrice__Rkale():
        frame_pricipale = Frame( souframepourframeuser, width=240 , height=308 ,bg="#059862" )
        frame_pricipale.place(x = 980 , y = 10)
        fon = "arial 19 "
        fontbu="arial 14 bold"
        ecran = Entry(frame_pricipale  , borderwidth= 0 , font = fon, bg="#FFF4A3" )
        ecran.place(x= 0, y =25 ,bordermode=OUTSIDE,height=50,width=240)
        root.overrideredirect(0)
        #----------------------------------------------
        btn121 = Label(frame_pricipale , text="Calculatrice",bg="#007BF7",fg="#FFFFFF",font="arial 11 bold")
        btn121 .place(x =0 , y = 0 ,height=25 , width=240)
    
        
        #----------------------------------------------
        btn2 = Button(frame_pricipale , text="0",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn2.place(x =60 , y = 250 ,height=50 , width=60)
        
        #----------------------------------------------#E0E0E0
        btn3 = Button(frame_pricipale , text=",",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn3.place(x =120 , y = 250 ,height=50 , width=60)
        #----------------------------------------------
        
        btn4 = Button(frame_pricipale , text="=",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn4.place(x =180 , y = 250 ,height=50 , width=60)
        
        btn5 = Button(frame_pricipale , text="1",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn5.place(x =0 , y = 200 ,height=50 , width=60)
        
        btn6 = Button(frame_pricipale , text="2",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn6.place(x =60 , y = 200 ,height=50 , width=60)
        
        btn7 = Button(frame_pricipale , text="3",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn7.place(x =120 , y =200  ,height=50 , width=60)
        
        btn8 = Button(frame_pricipale , text="-",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn8.place(x =180 , y = 200 ,height=50 , width=60)
        
        btn9 = Button(frame_pricipale , text="4",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn9 .place(x =0 , y = 150 ,height=50 , width=60)
        btn10 = Button(frame_pricipale , text="5",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn10 .place(x =60 , y =150  ,height=50 , width=60)
        btn11 = Button(frame_pricipale , text="6",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn11 .place(x =120, y = 150 ,height=50 , width=60)
        btn12 = Button(frame_pricipale , text="X",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn12 .place(x =180 , y = 150 ,height=50 , width=60)
        
        btn13 = Button(frame_pricipale , text="7",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn13.place(x =0 , y =100  ,height=50 , width=60)
        btn14 = Button(frame_pricipale , text="8",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn14 .place(x =60 , y =100 ,height=50 , width=60)
        btn15 = Button(frame_pricipale , text="9",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn15 .place(x =120, y = 100 ,height=50 , width=60)
        btn16 = Button(frame_pricipale , text="/",borderwidth= 0,bg="#059862",fg="#FFFFFF",font=fontbu)
        btn16 .place(x =180 , y = 100 ,height=50 , width=60)
        btn17 = Button(frame_pricipale , text="C",borderwidth= 0,bg="#FA8072",fg="#FFFFFF",font="arial 11 bold")
        btn17 .place(x =0 , y = 75 ,height=30 , width=240)
    calculatrice__Rkale()

modecaisserkaleframeuser()
retour_oumodecaisse = Button(frameAdmin, text="Mode Caisse", command=modecaisserkale, bd=0, bg='#007BF7', fg="#FFFFFF",
                       font=('arial', 11, 'bold'), relief=FLAT, activebackground="#FFFFFF", activeforeground='#007BF7')
retour_oumodecaisse.place(x=370, y=10, width="170", height=50)

# frameAdmin-------------------------- -----------------------------------------------------------

framelogin.tkraise()
root.mainloop()
