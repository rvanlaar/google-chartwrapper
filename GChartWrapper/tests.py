from GChartWrapper.testing import TestClass
import os,sys
from inspect import getsource
        
if __name__=='__main__':
    arg = sys.argv[-1].lower()
    if not arg in ('save','wiki','img','url','show'):
        arg = 'url'
        
    Test = TestClass()

    if arg == 'save':  
        if not os.path.isdir('tests'):
            os.mkdir('tests')  
        for test in Test.all:
            getattr(Test,test)().save(os.path.join(os.getcwd(),'tests',test))

    elif arg == 'wiki':
        print '== Chart examples adapted from the Google examples taken from the wrapper module unit tests =='
        for test in Test.all:
            testobj = getattr(Test,test)
            G = testobj()
            print '=== %s ==='%test.title()
            print '{{{'
            print '\n'.join(map(lambda x: x.strip(), getsource(testobj).splitlines()[1:-1]))
            print '}}}'
            print '%s&.png'%G
            print

    elif arg == 'img':
        for test in Test.all:
            print test,'\t',getattr(Test,test)().img()
            print

    elif arg == 'url':
        for test in Test.all:
            print test,'\t',getattr(Test,test)()
            print

    elif arg == 'show':
        for test in Test.all:
            getattr(Test,test)().show()                
        
