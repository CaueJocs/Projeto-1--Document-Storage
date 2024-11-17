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
    
    for i in range(len(prof)):
        print(prof[i][0])
        print(prof[i][1])
        print(prof[i][2])
        
        if prof[i][3] == 'None':
            print("Null")
        else:
            print(prof[i][3])
    
getProfessor()




