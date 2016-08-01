from texttable import Texttable

def test_converter(original,retake, retake_score=0):
    '''If you have two tests with different total scores, this function will
    produce a table that shows the equivalent scores from the retake test vs. the 
    original test. retake_score is an optional input that will automatically 
    compute a students score and output that score below the table.
    
    Inputs:
        original - total possible points on the original test
        retake - total possible points on the retake test
        *optional* retake_score - a specific student's score that will get printed below the table.
        
    example:  In [1]:  test_converter(20,24)'''
    
    newlist=[["retake","original","letter"]]     #initializes the list for the table.  The title is already included
    for i in range(1,retake+1,1):             #for loop that runs through the possible scores on the retake test
        if ((float(i)/retake)*100)>90:          #Calculates the letter grade of the retake test
            grade = "A"
        elif ((float(i)/retake)*100)>80:
            grade = "B"
        elif ((float(i)/retake)*100)>70:
            grade = "C"
        elif ((float(i)/retake)*100)>60:
            grade = "D"
        else:
            grade = "F"
        j=round(float(i)*(float(original)/float(retake)),3)   #Calculates the equivalent score on the retake test vs. the original test
        newlist.append([i,j,grade],)                          #Adds necessary information to the list for the table
    
    t = Texttable()
    t.add_rows(newlist)              #Creates table
    print t.draw()                   #Draws table   
    if retake_score > 0:             #Tests to see if 'retake_score' has been changed to compute a specific score
        print (float(retake_score)/retake)*original
    if retake_score < 0:
        print "If the student got a negative score on the retake, they probably deserve to fail."

#Things we can do to improve: