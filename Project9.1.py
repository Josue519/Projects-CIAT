"""
File: Project9.1.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __lt__(self, other):
        """Returns self < other, with respect to names. """
        return self.name < other.name
    def __ge__(self, other):
        """Retrurns self <= other with respect to names. """
        return self.name >= other.name

    def __eq__(self, other):
        """Test for equality."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False 
        else:
            return self.name == other.name


def main():
    """Tests for equality and comparisons."""
    s1 = Student("Ken", 10)
    s2 = Student("Wilma",10)
    s3 = Student("Ken", 10)

    print("False:",s1 == s2)
    print("True:", s1 == s3)
    print("True:", s1 == s1)
    print("False:",s1 is s3)
    print("True:", s1 < s2)
    print("True:", s2 > s1)
    print("True:", s2 >= s1)
    print("True:", s1 >= s3)
    print("True:", s1 <= s2)
    print("True:", s1 <= s3)

    

if __name__ == "__main__":
    main()