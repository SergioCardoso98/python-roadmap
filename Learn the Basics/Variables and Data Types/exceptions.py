try:
    #some code
    raise NameError('HiThere') # can be the system to raise one when it finds
except NameError:
    print('An exception flew by!')
    raise
#We can also do
except (Exception, ZeroDivisionError) as e:
    print('another exception')


#An exception flew by!
#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#    raise NameError('HiThere')
#NameError: HiThere