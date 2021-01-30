import pymongo
class contact:
    def myconnection(self):
        try:
            myclient = pymongo.MongoClient('mongodb://localhost:27017/')
            mydb = myclient['contact_book']
            mycol = mydb['my_content_list']
        except:
            print('Error in connections')
        else:
            def myoption():
                print('\nChosse options below and press buttons: \n1) Press A to add new contact.\n2) Press B to see your contact list. \n3) Press C to update details in existing contact. \n4) Press D to exit. \n5) Press X to delete a record.')
                firstCall()
            def dFun():
                myclient.close()
                print('Connection finished')
            def aFun():
                print('Please enter the below details for your new contact.')
                name = input('Enter the name: ')
                mobile = input('Enter mobile number: ')
                email = input('Enter email ID: ')
                otherdetails = input('Other Details you want to add: ')
                mydict = {'Name' : name, 'Mobile Number' : mobile, 'Email' : email, 'Other Details' : otherdetails}
                mycol.insert_one(mydict)
                print('Details added successfully')
                myoption()
            def bFun():
                userdata = mycol.find({}, {'_id' : 0, 'Name': 1, 'Mobile Number' : 1, 'Email' : 1, 'Other Details' : 1})
                print(userdata)
                for record in userdata:
                    print(record)
                myoption()
            def middle():
                Name = input('Enter the user name: ')
                data = mycol.find({'Name' : Name},{'_id' : 0, 'Name' : 1, 'Mobile Number' : 1, 'Email' : 1, 'Other Details' : 1})
                for i in data:
                    print(f'Old Details: {i}')
                return Name
            def cFun():
                updateName = middle()
                newupdatenumber = input('Enter new Mobile number: ')
                mycol.update_one({'Name' : updateName}, { "$set": {'Mobile Number' : newupdatenumber}})
                updatedate = mycol.find({'Name' : updateName},{'_id' : 0, 'Name' : 1, 'Mobile Number' : 1, 'Email' : 1, 'Other Details' : 1})
                for i in updatedate:
                    print(f'New Details: {i}')
                myoption()
            def xFun():
                deleteName = middle()
                mycol.delete_one({'Name' : deleteName})
                print('Record Deleted')
                myoption()
            def step(value):
                if value == 'd':
                    dFun()
                elif value == 'b':
                    bFun()
                elif value == 'a':
                    aFun()
                elif value == 'c':
                    cFun()
                elif value == 'x':
                    xFun()
            def firstCall():
                value = input().lower()
                step(value)
            print('What do you want to do with your contact list ? \nChosse options below and press buttons: \n1) Press A to add new contact.\n2) Press B to see your contact list. \n3) Press C to update details in existing contact. \n4) Press D to exit. \n5) Press X to delete a record.')
            firstCall()
        finally:
            myclient.close()
            
obj1 = contact()
obj1.myconnection()