from tkinter import *
from mydb import Database
from tkinter import messagebox
from api import API

class NLPApp:

    def __int__(self):

        # create db object
        self.dbo = Database()
        self.apio = API()

        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap(' ')
        self.root.geometry(' ')
        self.root.configure(bg='#34494E')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34494E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='enter email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='enter password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='login', width=30, height=2, command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a member ?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='register now', command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        print('register func')
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34494E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='enter name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='enter email')
        label1.pack(pady=(10, 10))

        self.email_Input = Entry(self.root, width=30)
        self.email_Input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='enter password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='register', width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a member ?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='register now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        # clear the existing fun
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email = self.email_Input.get()
        password = self.password_input.get()
        print(name)

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'reg successful')
            print('reg successful')
        else:
            print('email exists')

    def perform_login(self):
        email = self.email_Input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('success', 'Login successful')
        else:
            messagebox.showinfo('error', 'Incorrect email/password')

    def home_gui(self):

        self.clear()

        heading = Label(self.root, teext='NLPAPP', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4,
                               command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4,
                         command=self.perform_registration)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4,
                             command=self.perform_registration)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment',
                               command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        print(txt)
        self.sentiment_result['text'] = text


nlp = NLPApp()
