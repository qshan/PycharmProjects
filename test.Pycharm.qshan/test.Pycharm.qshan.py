#/python2

import time, datetime

print "##start of test.Pycharm.qshan.py##"
print "Hello Pycharm from Qshan"

def test_qshan (str_qshan):
    print str_qshan
    return


#print_temp_qshan = raw_input("input what you want to print: ")
print_temp_qshan = "Hello, from Qshan"
test_qshan(print_temp_qshan)

for num_for_qshan in range(1, 15, 2):
    print"here is ", num_for_qshan
    if num_for_qshan > 10:
        print "end the for-loop when ", num_for_qshan, "times"
        break

num_while_qshan = 0
while (num_while_qshan < 5):
    print "whil-loop cycle is", num_while_qshan
    num_while_qshan = num_while_qshan + 1

pass


var1_test_qshan = "Hello Pycharm"
var2_test_qshan = 'Hello Python'
print var1_test_qshan[0:5]
print var1_test_qshan[:5]
print var1_test_qshan[0]

list1_test_qshan = ["Hello", 'Python', 2017]
print list1_test_qshan[2]


tup1_test_qshan = ("H", 'ello', 2017.9)
tup2_test_qshan = ("H",)
tup3_test_qshan = ()

dict_test_qshan = {"Xiaoming":"25", 'LaoWang':'30'}
print "Xiaoming is", dict_test_qshan['Xiaoming']
print 'LaoWang is', dict_test_qshan["LaoWang"]

file_test_qshan = open("/home/qshan/temp/Pycharm_test_qshan.txt", "a+")
file_test_qshan.writelines("just for Python test from qshan! \n")
file_test_qshan.flush()
file_test_qshan.close()
print "file name is", file_test_qshan.name
print "file mode is", file_test_qshan.mode
print "if file closed", file_test_qshan.closed


class person_test_qshan:
    name = "please input"
    old = 0
    def __init__(self,name,old):
        self.name = name
        self.old = old
    def display_name(self):
        print self.name
    def display_old(self):
        print self.old
    def get_name(self):
        return self.name
    def get_old(self):
        return self.old

test_person_test_qshan =  person_test_qshan("Xiaoming", 25)

print "#Class test#, print class name:", test_person_test_qshan.name
print "#Class function test#, print get_old function: ", test_person_test_qshan.get_old()

class son_test_qshan(person_test_qshan):
    job = "input"
    def __init__(self,name, old, job):
        self.name = name
        self.old = old
        self.job = job
    def get_job(self):
        return self.job
    def display_job(self):
        print self.job

test_son_test_qshan = son_test_qshan("Xiaoxiao", 15, "Student")

print "#Class test#, print display name: ", test_son_test_qshan.name
test_son_test_qshan.display_job()
print "#Class test#, print display job: ", test_son_test_qshan.job

pass

print "################################"
print time.localtime(time.time())
print "##end of test.Pycharm.qshan.py##"


