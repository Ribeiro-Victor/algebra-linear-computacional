from task03.method import Method

class Interpolation(Method):
    def solve(self):
        phi = 1.0
        y = 0.0
        for i in range(self.n):
            for k in range(self.n):
                if(k!=i):
                    phi *= (self.x - (self.points[k][0])) / (self.points[i][0] - self.points[k][0])
            
            y += phi * self.points[i][1]
            phi = 1.0
        
        return y