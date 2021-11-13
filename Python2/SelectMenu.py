#Conversion selector

def displayMenu():
    print 'Temperature Conversion Menu';
    print '(1) Convert Farenheit to Celsius';
    print '(2) Convert Celsius to Farenheit';
    print '(3) Convert Inches to Centimeters';
    print '(4) Convert Centimeters to Inches';
    print '(5) Convert Gallons to Liters';
    print '(6) Convert Liters to Gallon';
    print '(7) Convert Yards to Meters';
    print '(8) Convert Meters to Yards';
    print '(9) Convert Pounds to Kilograms';
    print '(10) Convert Kilograms to punds';

def select():
        displayMenu();
        choice = input('Enter Choice number: ');
        if (choice==1):
            F2C();
        elif(choice==2):
            C2F();
        elif(choice==3):
            I2C();
        elif(choice==4):
            C2I();
        elif(choice==5):
            G2L();
        elif(choice==6):
            L2G();
        elif(choice==7):
            Y2M();
        elif(choice==8):
            M2Y();
        elif(choice==9):
            P2K();
        elif(choice==10):
            K2P();
        else:
            print "Invalid choice ",choice;
            print "xyz";
        print 'Bye-Bye.';

def C2F():
    Celsius = input ('Enter degrees in celsius: ');
    Farenheit = (9.0/5.0)*Celsius+32;
    print Celsius, 'Celsius =',Farenheit,'Farenheit';
        
        
def F2C():
    '''statements
    statements'''
    print 'write the code for F2C';

def I2C():
    '''statements
    statements'''
    print 'write the code for I2C';

def C2I():
    '''statements
    statements'''
    print 'write the code for C2I';

def G2L():
    '''statements
    statements'''
    print 'write the code for G2L';

def L2G():
    '''statements
    statements'''
    print 'write the code for L2G';

def Y2M():
    '''statements
    statements'''
    print 'write the code for Y2M';

def M2Y():
    '''statements
    statements'''
    print 'write the code for M2Y';

def P2K():
    '''statements
    statements'''
    print 'write the code for P2K';

def K2P():
    '''statements
    statements'''
    print 'write the code for K2P';
    
    
            
            
        
    
    
