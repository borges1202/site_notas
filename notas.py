import streamlit as st

try:
  #Titulo.
  st.title("Calculadora de notas.")

  #Sidebar para escolher a materia
  with st.sidebar:
    st.header('Escolha a Materia')
    materia = st.selectbox('Escolha uma opção', ['','Matematica', 'Biologia', 'Fisica', 'Lingua Portuguesa',
  'Arte', 'Historia', 'Quimica', 'Geografia', 'Ingles', 'Filosofia/Sociologia']).upper()

  #Se a materia não for escolhida, vai aparece 'esperando a materia'.
  if materia == '':
    st.write('esperando a materia...')

  #Caso materia seja escolhida o codigo sera executado normalmente.
  else:
    st.write("Coloque as informaçoes nos campos a baixo.")
    
    #Pegando as info necessarias
    total_provas = st.number_input('Quantidade de provas:',min_value=1, max_value=3)

    #Pegando a soma das provas da P1 e fazendo o Calculo.
    if total_provas == 1:
      p1 = st.number_input(f'Digite sua nota total da p1')
    else:
      p1 = st.number_input(f'Digite sua nota total da p1 (A soma das {total_provas} provas):')
    p1_nota_final = p1/total_provas

    #Pegando a nota da P2.
    p2 = st.number_input('Digite sua nota da p2:', min_value=0.0, max_value=10.0)

    #Calculando a media final.
    nota_final = (p1_nota_final+p2)/2
    if p1 == 0 or p2 == 0:
      st.write('esperando os valores...')
    else:
      st.write(f'Sua media final em {materia} foi e igual a {nota_final:.2f}')
except:
  st.error('Seu navegador não suporta o site')
