class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        
        seats.sort()
        students.sort()
        n = len(students) 
        moves = 0
    
        for i in range(n):
            moves += abs(students[i]-seats[i])
            
        return moves
        



    
            