class classFunProjects():
    def Subfields():
        list=['Sub-fields in AI are:', 'Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for lesson in list:
            print(lesson)
            
    def OddEven():
        num=int(input("Enter a number: "))
        if ((num%2)==1):
            print(num," is Odd number")
        else:
            print(num," is Even number")
        
    def Elegible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=='Female'):
            if(Age>=18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(Gender=='Male'):
            if(Age>=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("INVALID DATA")
            
    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total : ",total)
        per=(total/500)*100
        print("Percentage : ",per)
        
    def triangle():
        High=int(input("Height:"))
        Breth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area=(High*Breth)/2
        print("Area of Trinangle: ",Area)
        High1=int(input("Height1:"))
        High2=int(input("Height2:"))
        Breth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter=High1+High2+Breth
        print("Perimeter of Triangle: ",Perimeter)