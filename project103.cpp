
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;


// Defining the class studentType 
class studentType 
{
    // Declaring the private members of the class
    private:
    string firstName; 
    string lastName; 
    char courseGrade;
    int testScore;
    int programmingScore; 
    double  GPA;
    // Defining the public members of the class

    public: 

    // Defining the constructor to set the initial value 

    studentType() 
    {
        firstName  = "";
        lastName = "";
        courseGrade = 'F';
        testScore = 0;
        programmingScore = 0;
        GPA = 0;
    }

    // Defining the function to read and store the data in the class variables.

    void readIn() 
    {
        int score; 
        // Promting the user to enter the input and storing that in its respective class variable. 
        cout <<"Enter the first name: ";
        cin>>firstName;
        cout <<"Enter the last Name: ";
        cin>>lastName;
        cout <<"Enter the test Score: ";
        cin>>testScore;
        cout <<"Enter the programming Score: ";
        cin>>programmingScore;
        cout <<"Enter the GPA: ";
        cin>>GPA;
        // computing the average score.
        score = (testScore + programmingScore) / 2;
        // Checking the value of the score and setting the grade.

        if (score >= 90)
        {
            courseGrade = 'A';
        }
        else if (score >= 80)
        {
            courseGrade = 'B';
        }
        else if (score >= 70)
        {
            courseGrade = 'C';
        }
        else if (score >= 60)
        {
            courseGrade = 'D';
        }
        else
        {
            courseGrade = 'F';
        }
    }

    // Defining the function to print the values.
    void printStudent()
    {
        cout << "Name: "<<firstName<<" "<<lastName;
        cout <<endl;
        cout << "Course Grade: "<< testScore <<endl;
        cout <<endl;
        cout << "Programming score: "<<  programmingScore;
        cout << endl <<"GPA: "<< GPA <<endl;
    }

    // Defining the getter and setter functions for all the variables of the class.

    string getFirstName()
    {
        return firstName;
    }
    string getLastName()
    {
        return lastName;
    }
    void setLastName(string fname)
    {
        firstName = fname;
    }
    char getCourseGrade()
    {
        return courseGrade;
    }
    void setCourseGrade(char grade)
    {
        courseGrade = grade;
    }
    int getProgrammingScore()
    {
        return programmingScore;
    }
    void setProgrammingScore(int pscore)
    {
        programmingScore = pscore;
    }
    double getGPA()
    {
        return GPA;
    }
    void setGPS(double gpa)
    {
        GPA = gpa;
    }

};







