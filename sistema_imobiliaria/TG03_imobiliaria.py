import os
import datetime

class Cliente:
  cpf= ''
  nome = ''
  data_nascimento = ''
  salario = ''
  email = ''
  telefone = ''
#----------------------------------------------
class Imovel:
  codigo = ''
  descricao =''
  endereco = ''
  tipo = ''
  valor_aluguel = '' 
#----------------------------------------------
class Aluguel:
  cpf = ''
  codigo = ''
  data = ''
  fiador =''
  valor =''
#----------------------------------------------
def remover_item(lista, indice):
  i = indice
  while i < len(lista) - 1:
    lista[i] = lista[i + 1]
    i = i + 1
  lista.pop()
#----------------------------------------------
def busca_cliente(lista, val):
  i = 0
  while i < len(lista):
    if lista[i].cpf == val:
      return 1 
    i += 1
  return -1
#----------------------------------------------
def busca_imoveis(lista, val):
  i = 0
  while i < len(lista):
    if lista[i].codigo == val:
      return 1 
    i += 1
  return -1 
#----------------------------------------------   
def busca_aluguel(aluguel, val):
  i = 0
  while i < len(aluguel):
    if aluguel[i].data == val:
      return 1 
    i += 1
  return -1 
#-----------------------------------------------
def busca_indice_cliente(lista, elem):
  i = 0
  while i < len(lista):
    if lista[i].cpf == elem:
        return i
    i = i + 1
  return -1
#----------------------------------------------
def busca_indice_imovel(lista, elem):
  i = 0
  while i < len(lista):
    if lista[i].codigo == elem:
        return i
    i = i + 1
  return -1
#----------------------------------------------
def remover_cliente(clientes):
  cli_cpf = input("Informe o CPF a ser removido: ")
  indice = busca_indice_cliente(clientes, cli_cpf)
  if indice != -1:
    remover_item(clientes, indice)
    print("Cliente removido com sucesso!")
  else:
    print("\nCliente CPF " + cli_cpf + " nao encontrado!")
#----------------------------------------------
def remover_imovel(imoveis):
  imv_codigo = input("Informe o Codigo do imovel a ser removido: ")
  indice = busca_indice_imovel(imoveis, imv_codigo)
  if indice != -1:
    remover_item(imoveis, indice)
    print("Imovél removido com sucesso!")
  else:
    print("\nImovel codigo: " + imv_codigo + " nao encontrado!")
#----------------------------------------------
def remover_aluguel(alugueis):
  alug_codigo = input("Informe o Codigo do imovel a ser removido: ")
  indice = busca_indice_imovel(alugueis, alug_codigo)
  if indice != -1:
    remover_item(alugueis, indice)
    print("Imovél removido com sucesso!")
  else:
    print("\nImovel codigo: " + alug_codigo + " nao encontrado!")
#----------------------------------------------    
def alterar_aluguel(alugueis):
  alug_codigo = input("Informe o codigo a ser pesquisado: ")
  indice = busca_indice_imovel(alugueis, alug_codigo)
  if indice != -1:
    print('Informe os novos dados:')
    alug_codigo = input('Nro do codigo: ')
    alugueis[indice].codigo = alug_codigo
    alug_cpf = input('CPF: ')
    alugueis[indice].cpf = alug_cpf
    alug_data =  input('Data de entrada: ')
    alugueis[indice].data  = alug_data
    alug_fiador = input('Fiador: ')
    alugueis[indice].fiador = alug_fiador
    alug_valo = input('Valor do aluguel: ')
    alugueis[indice].valor =  alug_valo    
    print('Cliente atualizado com sucesso!')
  else:
    print("\nCliente : " + alug_codigo + " nao encontrado!")
#----------------------------------------------
def alterar_imovel(imoveis):
  codigo_imovel = input("Informe o codigo a ser pesquisado: ")
  indice = busca_indice_imovel(imoveis, codigo_imovel)
  if indice != -1:
    print('Informe os novos dados:')
    imv_codigo = input('Nro do codigo: ')
    imoveis[indice].codigo = imv_codigo
    imv_descri = input('Descrição: ')
    imoveis[indice].descricao = imv_descri
    imv_endereco =  input('Endereço: ')
    imoveis[indice].endereco  = imv_endereco
    imv_tipo = input('Tipo: ')
    imoveis[indice].tipo = imv_tipo
    imv_valor = input('Valor: ')
    imoveis[indice].valor_aluguel = imv_valor    
    print('Cliente atualizado com sucesso!')
  else:
    print("\nCliente : " + codigo_imovel + " nao encontrado!")
#----------------------------------------------
def alterar_cliente(clientes):
  cpf_pesquisar = input("Informe o CPF: ")
  indice = busca_indice_cliente(clientes, cpf_pesquisar)
  if indice != -1:
    print('Informe os novos dados:')
    cli_nome = input('Nome do Cliente: ')
    clientes[indice].nome = cli_nome
    cli_cpf = input('CPF: ')
    clientes[indice].cpf = cli_cpf
    cli_dn =  input('Data de nascimento: ')
    clientes[indice].data_nascimento  = cli_dn
    cli_salario = input('Renda: ')
    clientes[indice].salario = cli_salario
    cli_email = input('Email: ')
    clientes[indice].email = cli_email
    cli_tel = input('Telefone: ')
    clientes[indice].telefone = cli_tel
    print('Cliente atualizado com sucesso!')
  else:
    print("\nCliente : " + cpf_pesquisar + " nao encontrado!")
#----------------------------------------------
def pesquisar_cliente(clientes):
    cpf_pesquisar = input("Informe o CPF: ")
    indice = busca_indice_cliente(clientes, cpf_pesquisar)
    if indice != -1:
      cli_nome = clientes[indice].nome
      cli_cpf =   clientes[indice].cpf
      cli_dn =  clientes[indice].data_nascimento  
      cli_salario = clientes[indice].salario
      cli_email = clientes[indice].email
      cli_tel = clientes[indice].telefone 
      print('Cliente: ' + cli_nome +'\nCPF: '+ cli_cpf + '\nData de Nascimento: ' + cli_dn + '\nRenda: ' + cli_salario + '\nE-mail: ' + cli_email + '\nTelefone: ' + cli_tel +'\n'+'-'*40)
    else:
        print("\nCliente : " + cpf_pesquisar + " nao encontrado!")
#----------------------------------------------
def pesquisar_imovel(imoveis):
    codigo_imovel = input("Informe o codigo a ser pesquisado: ")
    indice = busca_indice_imovel(imoveis, codigo_imovel)
    if indice != -1:
      imv_codigo = imoveis[indice].codigo
      imv_descri= imoveis[indice].descricao
      imv_endereco = imoveis[indice].endereco
      imv_tipo = imoveis[indice].tipo
      imv_valor = imoveis[indice].valor_aluguel      
      print('Codigo: ' + imv_codigo +'\nDescrição: '+ imv_descri + '\nEndereço: ' + imv_endereco + '\nTipo: ' + imv_tipo + '\nValor aluguel: ' + imv_valor)  
    else:
        print("\n Imovel " + codigo_imovel + " nao encontrado!")
#----------------------------------------------  
def pesquisar_aluguel(alugueis):
  alug_codigo = input("Informe o codigo a ser pesquisado: ")
  indice = busca_indice_imovel(alugueis, alug_codigo)
  if indice != -1:
    alug_codigo = alugueis[indice].codigo
    alug_cpf = alugueis[indice].cpf
    alug_data = alugueis[indice].data
    alug_fiador= alugueis[indice].fiador
    alug_valor = alugueis[indice].valor      
    print('Codigo do Imovel: ' + alug_codigo +'\nCPF do Cliente: '+ alug_cpf + '\nData de entrada: ' + alug_data+ '\nFiadores: ' + alug_fiador + '\nValor aluguel: ' + alug_valor)  
  else:
    print("\n Codigo do Imovel " + alug_codigo + " nao encontrado!")
#---------------------------------------------           
def listar_aluguel(alugueis):
  for i in alugueis:
    print('Cpf cliente: ' + i.cpf+'\nCódigo do imóvel: '+ i.codigo + '\nData de entrada: ' + i.data + '\nFiador: ' + i.fiador + '\nValor do aluguel: ' + i.valor +'\n'+'-'*40)  
#----------------------------------------------
def listar_imoveis(imoveis):
  for i in imoveis:
    print('Codigo: ' + i.codigo +'\nDescrição: '+ i.descricao + '\nEndereço: ' + i.endereco + '\nTipo: ' + i.tipo + '\nValor aluguel: ' + i.valor_aluguel +'\n'+'-'*40)      
#----------------------------------------------
def listar_clientes(clientes):
  for i in clientes:
    print('Cliente: ' + i.nome +'\nCPF: '+ i.cpf+ '\nData de Nascimento: ' + i.data_nascimento + '\nRenda: ' + i.salario + '\nE-mail: ' + i.email + '\nTelefone: ' + i.telefone +'\n'+'-'*40) 
#----------------------------------------------
def inserir_aluguel(alugueis):
  cond =''
  resp = -1
  alug = Aluguel()
  alug_codigo=  input('Informe o codigo do imovel: ')
  if busca_imoveis(alugueis, alug_codigo) == -1:
    alug.codigo = alug_codigo    
    while resp != 1:
      alug_cpf = input('Informe o CPF do cliente: ')
      if busca_cliente(alugueis, alug_cpf)== -1:
        alug.cpf = alug_cpf
        break
      else:
        print("\nCPF " + alug_cpf + " já está cadastrado!")
      cond =(input('Deseja continuar? s/n: '))
      if cond != 's':
        return             
    while resp != 1:
      alug_data = input('Informe a data de entrada: ')
      if busca_aluguel(alugueis, alug_data) == -1:
        alug.data = alug_data
        break
      else:
        print("\nData " + alug_data + " já está cadastrada!")
      cond =input('Deseja continuar? s/n: ')
      if cond != 's':
        return       
    
    alug.fiador = input('Informe o fiador: ')
    alug.valor =input('informe o valor do aluguel: ')
    alugueis.append(alug)
    print("\nAluguel do imovél: " + alug_codigo +" cadastrado com sucesso!" )
  else:
    print("\n Imovel codigo: " + alug_codigo + " já está alugado!")
#----------------------------------------------
def inserir_imoveis(imoveis):
  imv_codigo = input('Informe o codigo: ')
  if busca_imoveis(imoveis, imv_codigo) == -1:
    imv = Imovel()
    imv.codigo = imv_codigo
    imv.descricao= input('Informe a descrição: ')   
    imv.endereco = input('Informe o endereço: ')
    imv.valor_aluguel = input('Informe o valor do aluguel: ')
    imv.tipo =input('informe o tipo: ')
    imoveis.append(imv)
    print("\nImovél: " + imv_codigo +" cadastrado com sucesso!" )
  else:
    print("\nCodigo Imovel: " + imv_codigo + " já está cadastrado!")
#----------------------------------------------
def inserir_clientes(clientes):
  cli_cpf = input('Informe o CPF: ')
  if busca_cliente(clientes, cli_cpf) == -1:
    c = Cliente()
    c.cpf = cli_cpf
    c.nome= input('Informe o Nome do Cliente:')
    c.data_nascimento = input('Informe Data de Nascimento: ')   
    c.salario = input('Informe Renda:')
    c.email = input('Informe o e-mail:')
    c.telefone =input('Informe Telefone:')
    clientes.append(c)
    print("\nCPF: " + cli_cpf +" cadastrado com sucesso!" )
  else:
    print("\nCPF " + cli_cpf + " já está cadastrado!")
#----------------------------------------------
def relatorio_imovel(imoveis):
  tipo = input('Informe Tipo: ')
  for i in imoveis:
    if i.tipo == tipo:
      print('Codigo: ' + i.codigo +'\nDescrição: '+ i.descricao + '\nEndereço: ' + i.endereco + '\nTipo: ' + i.tipo + '\nValor aluguel: ' + i.valor_aluguel +'\n'+'-'*40)     
#----------------------------------------------
def relatorio_cliente(clientes):
  valor1= int(input('Informe valor 1: '))
  valor2 = int(input('Informe valor 2: '))
  print()
  for i in clientes:
    cont = int(i.salario)    
    if cont >= valor1 and cont <= valor2:
      cli_nome = i.nome 
      cli_cpf =  i.cpf
      cli_dn =  i.data_nascimento  
      cli_salario = i.salario
      cli_email = i.email
      cli_tel = i.telefone 
      print('Cliente: '+ cli_nome +'\nCPF: '+ cli_cpf + '\nData de Nascimento: ' + cli_dn + '\nRenda: ' + cli_salario + '\nE-mail: ' + cli_email + '\nTelefone: ' + cli_tel +'\n'+'-'*40)    
#----------------------------------------------
def relatorio_aluguel(alugueis):
  data1 =input("informe a data1: ")
  data2 =input("informe a data2: ")
  data1 = trans_data(data1)
  data2 = trans_data(data2)

  for i in alugueis:
    dt = trans_data(i.data)
    if dt >= data1 and dt <=data2:
     print('Cpf cliente: ' + i.cpf+'\nCódigo do imóvel: '+ i.codigo + '\nData de entrada: ' + i.data + '\nFiador: ' + i.fiador + '\nValor do aluguel: ' + i.valor +'\n'+'-'*40)   
#----------------------------------------------
def trans_data(elen):
  lista = elen.split('/')  
  dia = int(lista[0])
  mes = int(lista[1])
  ano = int(lista[2])
  data = datetime.date(ano, mes, dia)
  return data
#----------------------------------------------
def submenu_relatorios():
  print()
  print("Gerenciar Relatorios:")
  print("   Dados Clientes..............1")
  print("   Dados Imoveis...............2")
  print("   Dados Alugueis..............3")
  print("Voltar.........................0")
  op = input("-> ")
  return op
#----------------------------------------------
def gerenciador_submenu_relatorios(alugueis, clientes, imoveis):
  opcao = 'x'
  while opcao != '0':
    opcao = submenu_relatorios()
    if opcao == '1':
      relatorio_cliente(clientes)
    elif opcao == '2':
      relatorio_imovel(imoveis)  
    elif opcao == '3':
      relatorio_aluguel(alugueis)
    elif opcao == '0':  
      print()
    else:
      print("Opcao invalida!!! Escolha novamente!")
#----------------------------------------------
def existe_arquivo(arquivo):
    import os
    if os.path.exists(arquivo):
      return True
    else:
      False
#----------------------------------------------
def escreve_arquivo_clientes(clientes, arquivo_clientes):
    arq = open (arquivo_clientes, 'w')
    for c in clientes:
        arq.write(c.cpf + ';' + c.nome + ";" + c.data_nascimento + ";" + c.salario + ';' + c.email + ';' + c.telefone)        
    arq.close()
#----------------------------------------------
def le_arquivo_clientes(arquivo_clientes):
  clientes = []

  if existe_arquivo(arquivo_clientes):
    arq = open(arquivo_clientes, 'r')
    for linha in arq:   
      infos = linha.split(';')      
      c = Cliente() 
      c.cpf = infos[0]
      c.nome = infos[1]
      c.data_nascimento = infos[2]
      c.salario = infos[3]
      c.email = infos[4]
      c.telefone = infos[5]
      clientes.append(c)
    arq.close()
  return clientes
#----------------------------------------------
def escreve_arquivo_imoveis(imoveis, arquivo_imoveis):
    arq = open (arquivo_imoveis, 'w')
    for i in imoveis:
        arq.write ( i.codigo + ';' + i.descricao + ";" + i.endereco + ";" + i.tipo + ';' + i.valor_aluguel)        
    arq.close()
#----------------------------------------------
def le_arquivo_imoveis(arquivo_imoveis):
  imoveis = []
  if existe_arquivo(arquivo_imoveis):
    arq = open(arquivo_imoveis, 'r')
    for linha in arq:   
      infos = linha.split(';')      
      i = Imovel() 
      i.codigo = infos[0]
      i.descricao = infos[1]
      i.endereco = infos[2]
      i.tipo = infos[3]
      i.valor_aluguel = infos[4]      
      imoveis.append(i)
    arq.close()
  return imoveis
#----------------------------------------------
def escreve_arquivo_alugueis(alugueis, arquivo_alugueis):
    arq = open (arquivo_alugueis, 'w')
    for a in alugueis:
        arq.write ( a.cpf + ';' + a.codigo + ";" + a.data + ";" + a.fiador + ';' + a.valor)        
    arq.close()
#----------------------------------------------    
def le_arquivo_alugueis(arquivo_alugueis):
  alugueis = []
  if existe_arquivo(arquivo_alugueis):
    arq = open(arquivo_alugueis, 'r')
    for linha in arq:   
      infos = linha.split(';')      
      a = Aluguel() 
      a.codigo = infos[0]
      a.cpf = infos[1]
      a.data = infos[2]
      a.fiador = infos[3]
      a.valor = infos[4]      
      alugueis.append(a)
    arq.close()
  return alugueis
#----------------------------------------------
def submenu_alugueis():
  print()
  print("Gerenciar Alugueis:")
  print("   Cadastrar...................1")
  print("   Alterar.....................2")
  print("   Listar......................3")
  print("   Pesquisar...................4")
  print("   Remover.....................5")
  print("Voltar.........................0")
  op = input("-> ")
  return op
#----------------------------------------------
def gerenciador_submenu_alugueis(alugueis):
  opcao = 'x'
  while opcao != '0':
    opcao = submenu_alugueis()
    if opcao == '1':
      inserir_aluguel(alugueis)
    elif opcao == '2':
      pesquisar_aluguel(alugueis) 
    elif opcao == '3':
      listar_aluguel(alugueis)
    elif opcao == '4':
      pesquisar_aluguel(alugueis)
    elif opcao == '5':
      remover_aluguel(alugueis)
    elif opcao == '0':  
      print()
    else:
      print("Opcao invalida!!! Escolha novamente!")
#----------------------------------------------
def submenu_imoveis():
  print()
  print("Gerenciar Imoveis:")
  print("   Cadastrar...................1")
  print("   Alterar.....................2")
  print("   Listar......................3")
  print("   Pesquisar...................4")
  print("   Remover.....................5")
  print("Voltar.........................0")
  op = input("-> ")
  return op
#----------------------------------------------
def gerenciador_submenu_imoveis(imoveis):
  opcao = 'x'
  while opcao != '0':
    opcao = submenu_imoveis()
    if opcao == '1':
      inserir_imoveis(imoveis) 
    elif opcao == '2':
      alterar_imovel(imoveis)
    elif opcao == '3':
      listar_imoveis(imoveis)      
    elif opcao == '4':
      pesquisar_imovel(imoveis)       
    elif opcao == '5':
      remover_imovel(imoveis)
    elif opcao == '0':  
      print()
    else:
      print("Opcao invalida!!! Escolha novamente!")
#----------------------------------------------
def submenu_clientes():
  print()
  print("Gerenciar Cliente:")
  print("   Cadastrar...................1")
  print("   Alterar.....................2")
  print("   Listar......................3")
  print("   Pesquisar...................4")
  print("   Remover.....................5")
  print("Voltar.........................0")
  op = input("-> ")
  return op
#----------------------------------------------
def gerenciador_submenu_clientes(clientes):
  opcao = 'x'
  while opcao != '0':
    opcao = submenu_clientes()
    if opcao == '1':
      inserir_clientes(clientes)
    elif opcao == '2':
      alterar_cliente(clientes) 
    elif opcao == '3':
      listar_clientes(clientes)
    elif opcao == '4':
      pesquisar_cliente(clientes)    
    elif opcao == '5':
      remover_cliente(clientes)
    elif opcao == '0':  
      print()
    else:
      print("Opcao invalida!!! Escolha novamente!")
#----------------------------------------------
def menu():
  print()
  print("Gerenciar: ")
  print("   Clientes....................1")
  print("   Imoveis.....................2")
  print("   Aluguéis....................3")
  print("   Relatorios..................4")
  print("Sair do Programa...............0")
  op = input("-> ")
  return op
#----------------------------------------------
def main():

  clientes =[]
  imoveis = []
  alugueis = [] 

  arquivo_clientes = "dados_clientes.txt" 
  arquivo_imoveis = "dados_imoveis.txt"
  arquivo_alugueis = "dados_alugueis.txt"
  clientes = le_arquivo_clientes(arquivo_clientes)
  imoveis= le_arquivo_imoveis(arquivo_imoveis)
  alugueis= le_arquivo_alugueis(arquivo_alugueis)
  opcao = 'x'
  while opcao != '0':
    opcao = menu()
    if opcao == '1':
      gerenciador_submenu_clientes(clientes)
    elif opcao == '2':
      gerenciador_submenu_imoveis(imoveis)
    elif opcao == '3':
      gerenciador_submenu_alugueis(alugueis) 
    elif opcao == '4':
      gerenciador_submenu_relatorios(alugueis, clientes, imoveis)
    elif opcao == '0':
      escreve_arquivo_clientes(clientes, arquivo_clientes)
      escreve_arquivo_imoveis(imoveis, arquivo_imoveis)
      escreve_arquivo_alugueis(alugueis, arquivo_alugueis)
      print("Obrigado por usar nosso programa!!!")
    else:
      print("Opcao invalida!!! Escolha novamente!")
#----------------------------------------------

main()
