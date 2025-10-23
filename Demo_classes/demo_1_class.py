from constraint import Problem, AllDifferentConstraint

# Exemplo
# Algoritmos — docente Ana; sala fixa Sala A
# Matematica — docente Ana; sala escolhida entre Sala A ou Laboratorio
# Inteligencia Artificial — docente Bruno; decorre exclusivamente online
# Bases de Dados — docente Bruno; sempre no Laboratorio

# Dados reduzidos: 4 cadeiras, 2 docentes e 4 blocos possiveis.
BLOCOS = [1, 2, 3, 4]
SALAS = ["Sala A", "Laboratorio", "Online"]

problema = Problem()

######################################################################
######################################################################
# 1º Definição de Variáveis e Dominios

# intervalo_algoritmos: define o bloco (1-4) para Algoritmos. 
# É excluido o bloco 2 para demonstrar indisponibilidade da Professora Ana.
problema.addVariable("intervalo_algoritmos", [1, 3, 4])

# sala_algoritmos: força Algoritmos a ficar sempre na Sala A (demonstracao de sala fixa).
problema.addVariable("sala_algoritmos", ["Sala A"])

# intervalo_matematica: bloco para Matematica, sem restricoes extra alem do conflito com Algoritmos.
# É excluido o bloco 2 para demonstrar indisponibilidade da Professora Ana.

#Simulação aula - implementação restricao
# blocos_auxiliar = range(1,21) # [1,2....,20]
# for restricao in bloco_resticoes["NomeProf"]:
#         blocos_auxiliar.remove(restricao)
# problema.addVariable(f"intervalo_matematica{"NomeProf"}", blocos_auxiliar)
problema.addVariable("intervalo_matematica", BLOCOS)
# sala_matematica: pode ser Sala A ou Laboratorio, mostrando escolha entre salas presenciais.
problema.addVariable("sala_matematica", ["Sala A", "Laboratorio"])

# intervalo_inteligenciaArtificial: bloco escolhido para Inteligencia Artificial.
problema.addVariable("intervalo_inteligenciaArtificial", BLOCOS) # [1,2,3,4]
# sala_inteligenciaArtificial: dominio apenas ["Online"], impondo aula remota obrigatoria.
problema.addVariable("sala_inteligenciaArtificial", ["Online"])

# intervalo_basesDeDados: bloco para Bases de Dados (docente Bruno).
problema.addVariable("intervalo_basesDeDados", BLOCOS)
# sala_basesDeDados: restrita ao laboratorio para enfatizar pratica obrigatoria.
problema.addVariable("sala_basesDeDados", ["Laboratorio"])

######################################################################
######################################################################

# Restricoes de docentes (Ana e Bruno) e da turma unica.
# Ou seja, Prof Ana e Prof Bruno apenas podem dar uma aula de cada vez
problema.addConstraint(AllDifferentConstraint(), [
    "intervalo_algoritmos",
    "intervalo_matematica",
    "intervalo_inteligenciaArtificial",
    "intervalo_basesDeDados",
])

solucoes = problema.getSolutions()

print(f"Número de soluções possíveis: {len(solucoes)}")

# _ | _ | _ | _
# UC "Algoritmos" tem 3 possibilidades dos 4 blocos totais
# Restantes 3 UCs tem 3 (considerando que 1 já foi ocupado para Algoritmos), ou seja, 3!

# Total 3 * 3! = 3 * (3*2*1) = 18
# Sala de Matemática pode ser na sala A ou Lab portanto 2 combinações possíveis para as 18 existentes

# Total = 18 * 2 = 36


if solucoes:
    melhor = solucoes[0]
    print("Horario simples encontrado:\n")
    print(
        f"Algoritmos (Prof. Ana) -> bloco {melhor['intervalo_algoritmos']} | "
        f"sala {melhor['sala_algoritmos']}"
    )
    print(
        f"Matematica (Prof. Ana) -> bloco {melhor['intervalo_matematica']} | "
        f"sala {melhor['sala_matematica']}"
    )
    print(
        f"Inteligencia Artificial (Prof. Bruno) -> bloco {melhor['intervalo_inteligenciaArtificial']} | "
        f"sala {melhor['sala_inteligenciaArtificial']}"
    )
    print(
        f"Bases de Dados (Prof. Bruno) -> bloco {melhor['intervalo_basesDeDados']} | "
        f"sala {melhor['sala_basesDeDados']}"
    )
else:
    print("Nao foi possivel encontrar solucao.")
