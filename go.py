from connecting import connection

var = connection()

def getMatriz():
    cur = var.cursor()
    cur.execute('select * from cursos;')
    matriz = cur.fetchall()

    cur.execute('select mc.cod_curso,d.cod_disc ,d.nome_disc  from disciplinas d join matriz_cursos mc on d.cod_disc = mc.cod_disc ;')
    teste = cur.fetchall()
    
    print("{ ")
    
    for i in range(len(matriz)):
        part1 = """ 
        " %d" :{
            "curso" : {
                "id": %d,
                "name" : "%s"
            },
            "disciplinas" : [
        """ % (i + 1, matriz[i][0], matriz[i][1])
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

    print("}")


def getProfessor():
    cur = var.cursor()
    cur.execute('select p.id_professor , p.nome_professor , p.dep_id  , d.dep_id from professor p left join departamento d on d.chefe_dep_id = p.id_professor ;;')
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
    
    cur.execute('select p.id_professor ,tcc.id_tcc  from alunos_tcc tcc right join professor p on p.id_professor = tcc.id_professor; ')
    prof_tcc = cur.fetchall()
    
    print("{")
    for i in range(len(prof)):
        if prof[i][3] is None:
            part1 = """
            " %d": {
                "id": %d , 
                "nome" : "%s",
                "dep" : %d, 
                "chef_dep" : "%s",
                "disciplinas" : [
            """ % (i + 1, prof[i][0], prof[i][1], prof[i][2], "NULL")
            print(part1, end="")
        else:
            part1 = """
            " %d": {
                "id": %d , 
                "nome" : "%s",
                "dep" : %d, 
                "chef_dep" : %d,
                "disciplinas" : [
            """ % (i + 1, prof[i][0], prof[i][1], prof[i][2], prof[i][3])
            print(part1, end="")
        
        # Processar disciplinas
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
        
        # Imprimir disciplinas, separadas por vírgulas
        print(",".join(disciplinas))
        print("],")
        
        # Processar TCC
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
        
        # Adicionar vírgula ao final do professor, exceto no último
        if i < len(prof) - 1:
            print(",")  # Adicionar vírgula entre objetos do JSON
    
    print("}")
            
            
                            
                                              
                            
getProfessor()




