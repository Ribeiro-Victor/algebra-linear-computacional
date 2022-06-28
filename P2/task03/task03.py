from P2.task03.runge_kutta_nystron import Runge_Kutta_Nystron
from matplotlib import pyplot as plt
import configparser

def run():
    with open("P2/task03/input.txt", "r") as file:
        parser_string = '[INPUT]\n' + file.read()
    parser = configparser.ConfigParser()
    parser.read_string(parser_string)

    try:
        delta = float(parser['INPUT']['delta_t'])
        tf = float(parser['INPUT']['t_final'])
        m = float(parser['INPUT']['m'])
        c = float(parser['INPUT']['c'])
        k = float(parser['INPUT']['k'])
        a1 = float(parser['INPUT']['a1'])
        a2 = float(parser['INPUT']['a2'])
        a3 = float(parser['INPUT']['a3'])
        w1 = float(parser['INPUT']['w1'])
        w2 = float(parser['INPUT']['w2'])
        w3 = float(parser['INPUT']['w3'])
    except:
        raise Exception("ERROR: Arquivo de input com erro.")
    
    a = [a1, a2, a3]
    w = [w1, w2, w3]

    print("[INFO] Arquivo de entrada lido.")

    rkn = Runge_Kutta_Nystron(m=m, c=c, k=k, a=a, w=w)
    solution = rkn.solve_second_order_ode(t0=0, tf=tf, delta=delta, x0=0, dx0=0)

    t_vector = solution.get('t')
    s_vector = solution.get('x')
    v_vector = solution.get('dx')
    a_vector = solution.get('d2x')

    buffer = '-'*20 + 'Dados lidos' + '-'*20 + '\n'
    buffer += f'passo de integracao(delta_t) = {delta}\ntempo_total(tf) = {tf}\n'
    buffer += f'm = {m}\t\tc = {c}\t\tk = {k}\n'
    buffer += f'a1 = {a1}\ta2 = {a2}\ta3 = {a3}\n'
    buffer += f'w1 = {w1}\tw2 = {w2}\tw3 = {w3}\n'
    buffer += '-'*22 + 'Solucao' + '-'*22 + '\n'
    
    header = ["Tempo", "Deslocamento", "Velocidade", "Aceleracao"]
    format_header = '{:^8}|'+'{:^14}|' * (3)

    buffer += format_header.format(*header)
    buffer += '\n'

    format_row = '{:^8.2f}|'+'{:^14.4f}|' * (3)
    for i in range (len(t_vector)):
        data = [t_vector[i], s_vector[i], v_vector[i], a_vector[i]] 
        buffer+=(format_row.format(*data))
        buffer+='\n'
    
    with open("P2/task03/output.txt", "w") as file:
        file.write(buffer)
    
    print("P2 - Task03 executada com sucesso. Saída disponível em: P2/task03/output.txt")

    VERDE = '#2E7D32'
    AZUL = '#1565C0'
    VERMELHO = '#D32F2F'
    LARANJA = '#DB6114'
    ROXO = '#6557D2'

    print("[INFO] Exibindo gráfico...")
    fig, axs = plt.subplots(3)
    axs[0].plot(t_vector, s_vector, color=AZUL, label='Posicao')
    axs[0].set_title('Deslocamento')
    axs[0].set(xlabel='tempo(t)', ylabel='Deslocamento(y)')

    axs[1].plot(t_vector, v_vector, color=VERMELHO, label='Velocidade')
    axs[1].set_title('Velocidade')
    axs[1].set(xlabel='tempo(t)', ylabel='Velocidade(y\')')

    axs[2].plot(t_vector, a_vector, color=VERDE, label='Aceleracao(y\'\')')
    axs[2].set_title('Aceleracao')
    axs[2].set(xlabel='tempo(t)', ylabel='Aceleracao(y\'\')')

    for ax in axs.flat:
        ax.label_outer()
        ax.grid(True)

    plt.grid(True)
    plt.show()