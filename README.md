# Invoicing-company-Django-Personal-Project
This repository is a personal project of an invoicing company using Django

Now we have an explanation of the deploy of this project:

1. Start and use the clients CRUD using the following paths:

      - Create a client using the url (host/signup/). Here you with be asked for an email, username, password, password confirmation, first name, last name and document.
      -Then, you can go ahead and login in the url (host). Please remember that if you don't do the signup process before getting to the login, you will receive and error message.
      - Once you are already authenticated, you will get in to main menu where you can select whether create, update and delete the client information. Moreover, you can also select to watch you profile information.

2. Once you are done with all client available process, you can use the bills CRUD:

      - On the main menu, you will find an option to watch all bill information of the current user. To begin with, you will find some basic information about the current client like number of clients, first name, last name, document and related bills.
      - You can create bills by clicking on the "Create here" bottom. Here you will be asked for a company name, nit, code and product data. Remember that you won't be able to create a bill unless you use a unique bill code. Moreover, product data are 3 fields with name and description each to add 3 maximum products.
      - Once you have some bills, you can go head and click the invoice name so you can watch the detail of each bill. Here, you will find options to delete and change a bill.
      - Every view has a back bottom, so you can go back to the previous page, and a log out bottom, so you close your client session.
      
3. You can also download a CSV register with all the client information saved, like document, first name, last name y invoice quantities related; by using the download url on the main menu. Moreover, you can also create clients by importing a CSV file with first name, last name, email, username, document and password; By using url update on the main menu. There has been provided an example CSV model file.
