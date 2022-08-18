from flask import Flask, render_template, url_for, request
import calc as Calc_DB
import pandas as pd
import os

app = Flask('app')

#Calc_DB.create_db()

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')
  

@app.route('/lista_pac')
def lista_pac():

  read_db = Calc_DB.read_all()

  lista_pacientes = []
  for cont in range(0, len(read_db['ID'])):
    lista_pacientes.append([read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont]])

  return render_template('lista-pacientes.html', read_db=read_db, lista_pacientes=lista_pacientes, tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)


@app.route('/edite_pac/<page_id>')
def edite_pac(page_id):

  read_db_id = Calc_DB.read_id(page_id)

  read_id = []
  for read in range(0, len(read_db_id['ID'])):
    read_id = [page_id,read_db_id['NAME'].loc[read],read_db_id['AGE'].loc[read],read_db_id['GEN'].loc[read],read_db_id['CPF'].loc[read],read_db_id['P_PAC'].loc[read],read_db_id['A_PAC'].loc[read]]

  #read_db_id = Calc_DB.ed_data(read_id[0], read_id[1],read_id[2], read_id[3], read_id[4], read_id[5], read_id[6])

  return render_template('edite-itens.html', read_id=read_id)

@app.route('/create_p')
def create_p():
  return render_template('cria-paciente.html')
    

@app.route('/add_data', methods=['POST', 'GET'])
def add_data():
  if request.method == 'POST':
    result = request.form
    name = result['name-paciente']
    age = result['age-paciente']
    gen = result['gen-paciente']
    cpf = result['cpf-paciente']
    p_pac = result['p-paciente']
    a_pac = result['a-paciente']

    '''print('>>>>NOME>>>>', name)
    print('>>>>AGE>>>>', age)
    print('>>>>AGE>>>>', gen)
    print('>>>>CPF>>>', cpf)
    print('>>>>P_PAC>>>', p_pac)
    print('>>>>A_PAC>>>>', a_pac)'''

    Calc_DB.add_pac(name,age, gen, cpf, p_pac, a_pac)

    read_db = Calc_DB.read_all()

    lista_pacientes = []
    for cont in range(0, len(read_db['ID'])):
      lista_pacientes.append([read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont]])

    return render_template('lista-pacientes.html', lista_pacientes=lista_pacientes)


@app.route('/edite_data', methods=['POST', 'GET'])
def edite_data():
  if request.method == 'POST':
    result = request.form
    id_name = result['read-id']
    print(':::::::::>>: ',id_name)
    name = result['name-paciente']
    age = result['age-paciente']
    gen = result['gen-paciente']
    cpf = result['cpf-paciente']
    p_pac = result['p-paciente']
    a_pac = result['a-paciente']

    Calc_DB.ed_data(id_name, name,age, gen, cpf, p_pac, a_pac)

    read_db = Calc_DB.read_all()

    lista_pacientes = []
    for cont in range(0, len(read_db['ID'])):
      lista_pacientes.append([read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont]])

    return render_template('lista-pacientes.html', lista_pacientes=lista_pacientes)


@app.route('/del_data/<page_id>')
def del_data(page_id):

  #Calc_DB.del_data(page_id)

  read_db = Calc_DB.read_all()

  lista_pacientes = []
  for cont in range(0, len(read_db['ID'])):
    lista_pacientes.append([read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont]])

  return render_template('lista-pacientes.html', lista_pacientes=lista_pacientes)

#app.run(host='0.0.0.0', port=8080, debug=True)
app.run(host='0.0.0.0', port='5000', debug=True)

#CRUD - Create, Read, Update and Delete