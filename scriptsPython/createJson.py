from connecting import connection

var = connection()

def getMatriz():
    cur = var.cursor()
    cur.execute('select * from cursos;')
    matriz = cur.fetchall()

    cur.execute('select mc.cod_curso,d.cod_disc ,d.nome_disc  from disciplinas d join matriz_cursos mc on d.cod_disc = mc.cod_disc ;')
    teste = cur.fetchall()
    
    print("[")
    
    for i in range(len(matriz)):
        part1 = """ 
        {
            "curso" : {
                "id": %d,
                "name" : "%s"
            },
            "disciplinas" : [
        """ % (matriz[i][0], matriz[i][1])
        print(part1, end="")


        disciplinas = [teste[j] for j in range(len(teste)) if teste[j][0] == matriz[i][0]]

        for idx, disc in enumerate(disciplinas):

            part2 = """
                {"id": %d, "name": "%s"}%s
            """ % (disc[1], disc[2], "," if idx < len(disciplinas) - 1 else "")
            print(part2, end="")

        if i == len(matriz) - 1:
            part3 = """
            ]
        }
        """
        else:
            part3 = """
            ]
        },
        """
        print(part3, end="")

    print("]")


def getProfessor():
    cur = var.cursor()
    cur.execute('select p.id_professor , p.nome_professor , p.dep_id  , d.dep_id, d.nome_dep  from professor p left join departamento d on d.chefe_dep_id = p.id_professor ;;')
    prof = cur.fetchall()
    
    cur.execute('''
    SELECT 
        p.id_professor, 
        pa.cod_disc, 
        d.nome_disc,
        (SELECT nome_curso FROM cursos c WHERE c.cod_curso = pa.id_curso) AS nome_curso,
        pa.ano, 
        pa.semestre
    FROM professor_aulas pa
    JOIN professor p ON p.id_professor = pa.id_professor
    JOIN disciplinas d ON d.cod_disc = pa.cod_disc;
    ''')

    prof_disc = cur.fetchall()
    
    cur.execute("""SELECT DISTINCT p.id_professor, tcc.id_tcc
    FROM alunos_tcc tcc
    RIGHT JOIN professor p ON p.id_professor = tcc.id_professor;""")
    prof_tcc = cur.fetchall()
    
    print("[")
    for i in range(len(prof)):
        if prof[i][3] is None:
            part1 = """
             {
                "id": %d , 
                "nome" : "%s",
                "dep" : %d, 
                "chef_dep" : "%s",
                "dep_chefe" : "%s",
                "disciplinas" : [
            """ % (prof[i][0], prof[i][1], prof[i][2], "null" , "null")
            print(part1, end="")
        else:
            part1 = """
             {
                "id": %d , 
                "nome" : "%s",
                "dep" : %d, 
                "chef_dep" : %d,
                "dep_chefe" : "%s",
                "disciplinas" : [
            """ % (prof[i][0], prof[i][1], prof[i][2], prof[i][3], prof[i][4])
            print(part1, end="")

        
        disciplinas = [
            """
                {
                    "id" : %d,
                    "nome_disc" : "%s", 
                    "nome_curso" : "%s",
                    "ano" : %d,
                    "semestre" : %d
                }""" % (prof_disc[j][1], prof_disc[j][2], prof_disc[j][3], prof_disc[j][4], prof_disc[j][5])
            for j in range(len(prof_disc)) if prof_disc[j][0] == prof[i][0]
        ]

        
        print(",".join(disciplinas))
        print("],")

        
        if prof_tcc[i][1] is None:
            part3 = """
                "tcc_id" : "%s"
            }""" % ("NULL")
            print(part3, end="")
        else:
            part3 = """
                "tcc_id" : %d
            }""" % (prof_tcc[i][1])
            print(part3, end="")

        
        if i < len(prof) - 1:
            print(",")  

    print("]")
            
def getAluno():
    cur = var.cursor()
    cur.execute('''
    SELECT DISTINCT 
        a.id_alunos, 
        a.nome_aluno, 
        ac.id_curso, 
        c.nome_curso
    FROM aluno a
    LEFT JOIN alunos_cursando ac ON a.id_alunos = ac.id_aluno
    RIGHT JOIN cursos c ON c.cod_curso = ac.id_curso;
    ''')
    aluno_curso = cur.fetchall()
    
    cur = var.cursor()
    cur.execute('''
        select a.id_alunos , ac.cod_disc ,d.nome_disc ,ac.ano, ac.semestre ,ac.nota  from aluno a join alunos_cursando ac 
        on a.id_alunos = ac.id_aluno join disciplinas d 
        on d.cod_disc =ac.cod_disc 
    
    ''')
    aluno_disc = cur.fetchall()
    
    cur = var.cursor()
    cur.execute('''
        select a.id_alunos , at2.id_tcc  from alunos_tcc at2 join aluno a 
        on a.id_alunos = at2.id_aluno ;
    ''')
    aluno_tcc = cur.fetchall()
    
    print("[")
    for i in range(len(aluno_curso)):
        part1 = """
             {
                "id": %d,
                "nome": "%s",
                "curso": {
                    "id_curso": %d,
                    "curso": "%s"
                },
                "historico": [
        """ % ( aluno_curso[i][0], aluno_curso[i][1], aluno_curso[i][2], aluno_curso[i][3])
        print(part1, end="")

        historico_entries = []
        for j in range(len(aluno_disc)):
            if aluno_disc[j][0] == aluno_curso[i][0]:
                historico_entries.append("""
                    {
                        "id_disc": %d,
                        "nome_disc": "%s",
                        "ano_cursado": %d,
                        "semestre" : %d,
                        "nota_fin": %d
                    }
                """ % (aluno_disc[j][1], aluno_disc[j][2], aluno_disc[j][3], aluno_disc[j][4], aluno_disc[j][5]))

        print(",".join(historico_entries))
        print("],")

        if aluno_tcc[i][1] is not None:
            part3 = """
                "tcc": {
                    "id_tcc": %d
                }
            """ % aluno_tcc[i][1]
        else:
            part3 = """
                "tcc": {
                    "id_tcc": null
                }
            """
        print(part3, end="")

        if i < len(aluno_curso) - 1:
            print("},")
        else:
            print("}")

    print("]")

getAluno()

                                                       





