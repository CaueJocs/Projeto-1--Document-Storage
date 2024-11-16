from connecting import connection

var = connection()

cur = var.cursor()
cur.execute('select d.cod_disc ,d.nome_disc,c.nome_curso  from cursos c join matriz_cursos mc on mc.cod_curso = c.cod_curso join disciplinas d on d.cod_disc = mc.cod_disc ;;')
rows = cur.fetchall()
var.commit()
var.close()

