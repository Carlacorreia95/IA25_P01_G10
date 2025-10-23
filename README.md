# IA25_P01_G10 – Class Timetable Scheduling Agent

## Descrição do Projeto
Este projeto foi desenvolvido no âmbito da unidade curricular de **Inteligência Artificial (2025/26)**, do curso de Engenharia de Sistemas Informáticos do IPCA.

O objetivo consiste em desenvolver um agente inteligente para gerar horários de aulas, modelado como um **Problema de Satisfação de Restrições (CSP)**, utilizando a biblioteca `python-constraint`.

## Estrutura do Repositório


## Dataset Utilizado
O problema baseia-se no seguinte conjunto de dados:

- **Aulas**: 2 horas cada, de segunda a sexta, em 4 blocos diários (total de 20 blocos).
- **Turmas**: t01, t02, t03, cada uma com 5 unidades curriculares (UCs).
- **Docentes**: jo, mike, rob, sue, com atribuição de UCs.
- **Restrições**:
  - Indisponibilidades de docentes (`tr`).
  - Salas fixas para certas UCs (`rr`).
  - Aulas online com lição semanal específica (`oc`).

## Funcionalidades Implementadas

### Restrições Obrigatórias (Hard Constraints)
- Cada aula tem duração de 2 horas.
- Todas as UCs têm 2 aulas por semana.
- Não mais de 3 aulas por dia por turma.
- Respeito pela disponibilidade dos docentes.
- Aulas online (máx. 3) no mesmo dia.
- Salas específicas para certas UCs.

### Restrições Preferenciais (Soft Constraints)
- Aulas da mesma UC em dias distintos.
- Preferência por 4 dias de aulas por turma.
- Aulas consecutivas no mesmo dia.
- Minimização do número de salas utilizadas por turma.

## Como Executar
1. Clona o repositório:
   ```bash
   git clone https://github.com/tuusername/IA25_P01_G##.git
   
2. Abre o Jupyter Notebook:

    ````bash
    jupyter notebook IA25_P01_G##.ipynb

3. Executa todas as células.

## Tecnologias Utilizadas
* Python 3
* Jupyter Notebook
* Biblioteca python-constraint

## Autores
Carla Correia, 10444

Leandro Machado, 20459

Pedro Costa, 20471

Ricardo Guimarães, 20469
