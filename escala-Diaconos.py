
import random


diaconos = ["Silvania", "Atelmo", "Quitéria", "Laudicéia", 'Cicero']
dias_domingo = [3, 10, 17, 24 ,31]
dias_quinta = [7, 14, 21 , 28]
todos_os_dias = dias_domingo + dias_quinta

todos_os_dias_ordenado = sorted(todos_os_dias)

limpou_ultima_vez = []
vezes_trabalhadas = {nome: 0 for nome in diaconos}
quem_mais_trabalhou = 0
print(vezes_trabalhadas)
for i in todos_os_dias_ordenado:
    
    diacono_servico_1 = diaconos.pop(0)
    diacono_servico_2 = diaconos.pop(0)
    diacono_limpeza = diaconos.pop(0)
    if vezes_trabalhadas[diacono_servico_1]>= quem_mais_trabalhou:
        quem_mais_trabalhou = vezes_trabalhadas[diacono_servico_1]
        diaconos.appendd(diacono_servico_1)
        diacono_servico_1 = diaconos.pop(0)
        
    if i in dias_domingo:
                
        
        if i == 10:
            
            while diacono_limpeza not in ["Cicero","Atelmo"] or diacono_limpeza in limpou_ultima_vez:
                diaconos.append(diacono_limpeza)
                diacono_limpeza = diaconos.pop(0)
                if diacono_limpeza in limpou_ultima_vez :

                    if diacono_servico_1 in ["Cicero","Atelmo"]:
                        temp = diacono_servico_1
                        diacono_servico_1 = diacono_limpeza
                        diacono_limpeza = temp

                    else:
                        temp = diacono_servico_2
                        diacono_servico_2 = diacono_limpeza
                        diacono_limpeza = temp
            
            
        else:
             while diacono_limpeza not in ["Cicero","Atelmo", "Silvania"] or diacono_limpeza in limpou_ultima_vez:
                diaconos.append(diacono_limpeza)
                diacono_limpeza = diaconos.pop(0)   
        vezes_trabalhadas[diacono_servico_1] += 1
        vezes_trabalhadas[diacono_servico_2] += 1        
    elif i in dias_quinta:
               
        
        while diacono_limpeza not in ["Laudicéia", "Quitéria"] or diacono_limpeza in limpou_ultima_vez:
            diaconos.append(diacono_limpeza)
            diacono_limpeza = diaconos.pop(0)
            if diacono_servico_1 in ["Laudicéia", "Quitéria"]:
                temp = diacono_servico_1
                diacono_servico_1 = diacono_limpeza
                diacono_limpeza = temp
            else:
                temp = diacono_servico_2
                diacono_servico_2 = diacono_limpeza
                diacono_limpeza = temp
        vezes_trabalhadas[diacono_servico_1] += 1
        vezes_trabalhadas[diacono_servico_2] += 1
    if len(limpou_ultima_vez) >=1:
        limpou_ultima_vez.pop(0)  
    diaconos.append(diacono_servico_1)    
    diaconos.append(diacono_servico_2)    
    diaconos.append(diacono_limpeza)    
    limpou_ultima_vez.append(diacono_limpeza)
    print(f"DIA {i} {diacono_servico_1} e {diacono_servico_2} serve, {diacono_limpeza} limpa")
print(vezes_trabalhadas)