from numpy import sin, cos

class Runge_Kutta_Nystron:

    def __init__(self, m, c, k, a, w):
        self.m = m
        self.c = c
        self.k = k
        self.a = a
        self.w = w

    def get_function_value(self, t, y, dy):
        m = self.m
        c = self.c
        k = self.k
        a = self.a
        w = self.w
        F = 0.0
        F += a[0]*sin(w[0]*t)
        F += a[1]*sin(w[1]*t)
        F += a[2]*cos(w[2]*t)
        #return -9.81 - dy*math.sqrt(dy**2)
        return (F - c*dy - k*y) / m
    
    def solve_second_order_ode(self, t0, tf, delta, x0, dx0):
        t_vector = [t0]
        x_vector = [x0]
        dx_vector = [dx0]
        d2x_vector = [self.get_function_value(t0, x0, dx0)]

        num_iterations = int((tf-t0)/delta)
        for i in range(num_iterations):
            t_vector.append(t0+(delta*(i+1)))
       
            K1 = (delta/2)*(self.get_function_value(t_vector[i], x_vector[i], dx_vector[i]))

            Q = (delta/2)*(dx_vector[i]+(K1/2))

            K2 = (delta/2)*(self.get_function_value(t_vector[i]+(delta/2), x_vector[i]+Q, dx_vector[i]+K1))

            K3 = (delta/2)*(self.get_function_value(t_vector[i]+(delta/2), x_vector[i]+Q, dx_vector[i]+K2))

            L = delta*(dx_vector[i]+K3)

            K4 = (delta/2)*(self.get_function_value(t_vector[i]+delta, x_vector[i]+L, dx_vector[i]+(2*K3)))

            x_vector.append(x_vector[i] + (delta * (dx_vector[i] + ((K1+K2+K3)/3) ) ))

            dx_vector.append(dx_vector[i] + ((K1+(2*K2)+(2*K3)+K4)/3))

            d2x_vector.append(self.get_function_value(t_vector[i+1], x_vector[i+1], dx_vector[i+1]))
            
            #print(f'{t_vector[i]:.2f}\t{x_vector[i]:.4f}\t')
        
        #print(f'{t_vector[num_iterations]:.2f}\t{x_vector[num_iterations]:.4f}\t')
        return {'x': x_vector,
                'dx': dx_vector,
                'd2x': d2x_vector,
                't': t_vector}