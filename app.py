import streamlit as st
import pandas as pd


if __name__ == "__main__":
    try:
        st.set_page_config(page_title="ISA 2025",
                           page_icon="icon.ico", layout="wide", initial_sidebar_state='auto')
        hide_footer_style = '''
        <style>
        header {visibility: hidden;}
        '''
        st.markdown(hide_footer_style, unsafe_allow_html=True)

        hide_menu_style = '''
        <style>
        #MainMenu {visibility: hidden;}
        '''
        st.markdown(hide_menu_style, unsafe_allow_html=True)

        with st.form("meu_questionario", clear_on_submit=True):
            st.header("QUESTIONÁRIO:")

            st.subheader("Dados colaborador(a):")
            nome_colaborador = st.text_input("Colaborador(a)")
            cpf_colaborador = st.text_input("CPF")

            st.subheader("Dados beneficiário(a):")
            nome_beneficiario = st.text_input("Beneficiário(a)")
            cpf_cnpj_beneficiario = st.text_input("CPF/CNPJ")
            idade_beneficiario = st.text_input(
                "Idade do/a responsavel e/ou proprietário/a (anos)")

            st.subheader("Local e identificação do imóvel rural:")
            geolocalizacao = st.text_input(
                "Geolocalização (coordenadas graus decimais) ")
            municipio = st.text_input("Nome do município")
            estado = st.text_input("Estado")
            nome_curso_dagua = st.text_input(
                "Nome do curso d'água principal mais próximo do imóvel rural")

            st.subheader("Posse da terra:")
            opcao_posse_terra = st.selectbox(
                'opções',
                ('Proprietário', 'Posseiro', 'Assentado',
                 'Arrendatário', 'Parceiro', 'Usufrutuário')
            )
            sucessao = st.radio(
                "Sucessão - processo sucessório da gestão do imóvel rural em andamento",
                help="Envolvimento dos filhos nos negócios; participação dos filhos em cursos de capacitação.",
                options=['Sim', 'Não'])
            participacao_mulher = st.radio(
                "Participação da mulher na gestão do imóvel rural",
                options=['Sim', 'Não'])

            st.subheader("Descrição do imóvel rural:")
            nome_imovel = st.text_input("Nome do imóvel rural")
            area_imovel = st.text_input("Área (ha)")
            agricultura_familiar = st.radio(
                "Enquadramento como Agricultura Familiar ( verificar se tem CAF)",
                options=['Sim', 'Não'])
            st.write(
                "Áreas não contíguas ao imóvel rural e/ou áreas de arrendamento que integram a renda do produtor")

            df_area_contigua = st.data_editor({
                "Identificação dos locais": [""],
                "Área (ha)": ["0"],
            })

            st.subheader("Uso e ocupação do solo no imovél rural:")
            df_ocupacao_solo = st.data_editor({
                "Descrição (Questionário)": ["Lavouras permanentes",
                                             "Lavouras temporárias",
                                             "Pastagens",
                                             "Silvicultura",
                                             "Área não agrícola",
                                             "Pousio",
                                             "Espelho/cursos d'água",
                                             "Vegetação nativa",
                                             "Áreas inaproveitáveis*"],
                "Uso atual Área (ha)": ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
            })

            st.subheader("Uso e ocupação do solo /app no imovél rural:")
            df_ocupacao_solo_car = st.data_editor({
                "Descrição (CAR)": ["Área correspondente ao uso consolidado",
                                    "Uso não consolidado / outros usos",
                                    "Pousio",
                                    "Espelho/cursos d'água",
                                    "Vegetação nativa",
                                    "Servidão administrativa*"],
                "Uso CAR (ha)": ["0", "0", "0", "0", "0", "0"],
            })
            st.write(
                "ÁREAS DE PRESERVAÇÃO PERMANENTE - APPs (CAR)")

            df_preservacao_car = st.data_editor({
                "Descrição": ["Área total de APPs",
                              "Área da APP a ser recuperada",
                              "Área de uso consolidado + vegetação nativa na APP"],
                "Aréa (ha)": ["0", "0", "0"],
            })

            st.subheader("Área de reserva legal (RL):")
            opcao_reserva_legal = st.selectbox(
                '% RL',
                ('20% do imóvel rural', '35% do imóvel rural', '80% do imóvel rural')
            )

            st.subheader("Recurso hídrico no imóvel rural:")
            df_recuro_hidrico = st.data_editor({
                "Descrição": ["Cursos d´água",
                              "Nascentes e olhos d'água perenes*",
                              "Lagos e lagoas naturais",
                              "Represas"],
                "Quantidade": [0, 0, 0, 0],
            })
            opcao_tipo_fonte_agua = st.selectbox(
                'Fonte de água utilizada no imóvel rural:',
                ("Superficial",
                 "Subterrânea*")
            )
            opcao_tem_problema_falta_agua = st.radio(
                'Problemas relacionados à qualidade e disponibilidade de água (para consumo humano e atividades)',
                options=["Sim",
                         "Não"]
            )
            especificar_problema_falta_agua = st.text_input("Especificar")

            st.subheader("Regularização ambiental do imóvel rural:")
            opcao_regularizacao_ambiental = st.radio(
                'Possui regularização do uso da água (outorga ou uso insignificante)',
                help="Outorga; ou cadastro de uso insignificante; ou cadastro na campanha 'água: faça uso legal'; ou cadastro de pequeno núcleo populacional rural.",
                options=["Sim",
                         "Não"]
            )
            opcao_licencimento_ambiental = st.radio(
                'Possui licenciamento ambiental ou certidão de não passível ou AAF',
                help='Certidão de não passível (dispensa de licenciamento), Autorização Ambiental de Funcionamento (AAF), Licenciamento Ambiental.',
                options=["Sim",
                         "Não"]
            )
            opcao_reserva_legal_regular = st.radio(
                'Possui regularização da Reserva Legal e das Áreas de Preservação Permanente',
                help='Cadastro Ambiental Rural - CAR.',
                options=["Sim",
                         "Não"]
            )

            st.subheader(
                "Pontos críticos")
            problemas_enfrentados = st.text_area(
                "Principais problemas enfrentados pelo produtor rural (na visão dele)")

            st.header("INDICADORES:")

            st.subheader(
                "Índices de produtividade e preços de venda")
            st.write(
                "Renda bruta anual estimada de atividades agrossilvipastoris no imóvel rural")
            df_renda_bruta = st.data_editor({
                "Descrição das atividades agrícolas, pecuárias e florestais": ["", "", ""],
                "Valor estimado anual (R$)": ["", "", ""],
            })
            st.write(
                "Principais atividades executadas no imóvel rural")
            descricao_atividade_rural = st.text_input(
                "Descrição das atividades")
            produtividade_rural_anual = st.text_input(
                "Produtividade média atual")
            preco_anual_venda_rural = st.text_input(
                "Preço médio de venda  (R$/unidade de venda)")

            st.subheader(
                "Diversidade de renda")
            st.write(
                "Renda bruta anual estimada de outras atividades gerada dentro do imóvel rural. Exemplo de outras atividades: Turismo, artesanato, agroindústria, produção de cachaça, alimentos processados, etc.")
            df_renda_bruta_outras_atividades = st.data_editor({
                "Descrição das atividades": ["", "", ""],
                "Valor estimado no ano (R$)": ["", "", ""],
            })
            st.write(
                "Renda bruta anual estimada fora imóvel rural. De todas as rendas das pessoas com vínculo direto com o estabelecimento (locação de máquinas, emprego fora do estabelecimento, prestação de serviços, etc.)")
            valor_outras_atividades_pensao_ajuda = st.text_input(
                "Pensão, aposentadoria, ajudas financeiras (R$)")
            valor_outras_atividades_prestacao_servico = st.text_input(
                "Outras atividades/prestação de serviços (R$)")

            st.subheader(
                "Serviços básicos disponíveis para o imóvel rural")
            qt_residencia_imovel = st.text_input(
                "Total de residências no imóvel rural")
            st.write(
                "Serviços básicos disponíveis OBS: Escolha uma opção: 1 (atende satisfatoriamente); 0,5 (parcialmente); 0 (inexistente)")
            df_servico_basico = st.data_editor({
                "Serviços disponíveis": ["Disponibilidade de água (quantidade e qualidade)",
                                         "Acesso a energia elétrica",
                                         "Acesso regular para escoamento da produção",
                                         "Acesso ao serviço de saúde (PSF)",
                                         "Acesso regular ao transporte escolar",
                                         "Segurança no campo",
                                         "Internet",
                                         "Coleta pública de lixo"],
                "Residência rural": ["", "", "", "", "", "", "", ""],
                "Outras residência": ["", "", "", "", "", "", "", ""],
            })
            st.write(
                "Produção própria de alimentos (para imóveis rurais menores que 4 MF). Escolha uma opção: 1 (atende satisfatoriamente); 0,5 (parcialmente); 0 (inexistente) ")
            df_procucao_alimento = st.data_editor({
                "Tipo alimentos": ["Hortaliças, grãos e tubérculos",
                                   "Pomar",
                                   "Criação de animais (carne, leite, ovos)"],
                "Residência rural": ["", "", ""],
                "Outras residência": ["", "", ""],
            })

            st.subheader(
                "Escolaridade & cursos direcionados às principais atividades")
            st.write(
                "Grau de escolaridade. Marque o nº de pessoas em cada campo")
            df_escolaridade = st.data_editor({
                "Grau de escolaridade": ["Número de adultos no imóvel rural",
                                         "Menos de 9 anos de estudo",
                                         "Ensino Fundamental completo",
                                         "Ensino Médio completo",
                                         "Curso superior"],
                "Integrantes da família com vínculo direto": [0, 0, 0, 0, 0],
                "Trabalhadores permanentes": [0, 0, 0, 0, 0],
            })

            st.write(
                "Cursos direcionados às principais atividades geradas no imóvel rural. Marque o nº de pessoas em cada campo")
            df_cursos_rurais = st.data_editor({
                "Cursos direcionados às principais atividades geradas no imóvel rural": [
                    "Capacitação curta temporada. Nº de pessoas que fizeram cursos de especialização direcionados às atividades.",
                    "Capacitação longa temporada. Nº de pessoas que fizeram cursos técnicos em agropecuária ou afins."],
                "Integrantes da família com vínculo direto": [0, 0],
                "Trabalhadores permanentes": [0, 0],
            })

            st.write(
                "Frequência da rede de ensino dos dependentes. Marque o nº de pessoas em cada campo. OBS: *** Dependentes que residem no estabelecimento (até o 2º grau).")
            df_frequencia_rede_ensino = st.data_editor({
                "Frequência da rede de ensino dos dependentes": [
                    "Número de dependentes no imóvel rural***",
                    "Frequenta rede de ensino."],
                "Dependentes (6 a 18 anos) dos integrantes***": [0, 0],
                "Dependentes (6 a 18 anos) de trabalhadores residentes***": [0, 0],
            })

            st.subheader(
                "Ocupação & emprego")
            st.write(
                "Cumprimento da Legislação Trabalhista. Marque o nº de pessoas em cada campo")
            df_cumprimento_legistacao_trabalhista = st.data_editor({
                "Cumprimento da Legislação Trabalhista": [
                    "Número de funcionários no imóvel rural",
                    "Registro de funcionários (carteira de trabalho)",
                    "Pagamento de hora extra / banco de horas* / ausência de hora extra"],
                "Contratação efetiva ": [0, 0, 0],
                "Contratação temporária ": [0, 0, 0],
            })

            st.write(
                "Adoção de benefícios / observância das recomendações/determinações do Ministério do Trabalho. Marque o nº de pessoas em cada campo")
            df_beneficios_ministerio_trabalho = st.data_editor({
                "Adoção de benefícios / observância das recomendações/determinações do Ministério do Trabalho": [
                    "Acima de 1 salário mínimo",
                    "Auxílio alimentação",
                    "Auxílio moradia",
                    "Auxílio educação e transporte",
                    "Participação nos lucros",
                    "Seguro contra acidentes",
                    "Acesso a lazer",
                    "Espaço para cultivo de alimentos "],
                "Contratação efetiva ": [0, 0, 0, 0, 0, 0, 0, 0],
                "Contratação temporária ": [0, 0, 0, 0, 0, 0, 0, 0],
            })

            st.subheader(
                "Gestão do empreendimento")
            st.write(
                "* Não considerar assistência técnica de revendas de insumos.")

            acesso_assistencia_tecnica = st.selectbox(
                'Acesso à assistência técnica (particular ou pública)*',
                ("atende satisfatoriamente",
                 "parcialmente",
                 "inexistente")
            )
            participacao_assistencia_tecnica = st.selectbox(
                'Participação - formas associativas',
                ("ativa",
                 "passiva")
            )
            regularizacao_ambiental = st.selectbox(
                'Regularização ambiental (Uso da água, CAR e Licenciamento)',
                ("atende satisfatoriamente",
                 "parcialmente",
                 "inexistente")
            )
            st.write(
                "Regularização ambiental (Uso da água, CAR e Licenciamento).")
            usa_credito_regularizacao_ambiental = st.selectbox(
                'Utiliza crédito para investimento',
                ("atende satisfatoriamente",
                 "parcialmente",
                 "inexistente")
            )

            usa_custeio_regularizacao_ambiental = st.selectbox(
                'Utiliza crédito para custeio',
                ("atende satisfatoriamente",
                 "parcialmente",
                 "inexistente")
            )

            usa_credito_comercializacao = st.selectbox(
                'Utiliza crédito para comercialização',
                ("atende satisfatoriamente",
                 "parcialmente",
                 "inexistente")
            )

            st.subheader(
                "Comercialização & inovação")
            st.write(
                "Comercialização")
            busca_informacoes_comercializacao = st.radio(
                "Busca informação para comercialização / diversificar compradores",
                options=["Sim",
                         "Não"])
            gera_produtos_certificados = st.radio(
                "Gera produtos certificados e/ou mercado institucional",
                options=["Sim",
                         "Não"])
            st.write(
                "Inovação")

            usa_tecnicas_inovadoras = st.radio(
                "Adoção de técnicas inovadoras*",
                help='* Conceito, ideia, prática ou tecnologia, percebidas como nova pelo indivíduo e/ou grupo social. Conhecimento científico e tecnológico transformados em boas práticas.',
                options=["Sim",
                         "Não"])

            descricao_tecnicas_inovadoras = st.text_input(
                "Descrição das tecnicas inovadoras.")
            tem_potencial_inovador = st.radio(
                "Capacidade de inovação ou liderança na comunidade",
                options=["Sim",
                         "Não"])
            descricao_potencial_inovador = st.text_input(
                "Descrição potêncial inovador ou lideraça.")

            st.write(
                "Práticas regenerativas (opcional)")

            usa_bioinsumos = st.radio(
                "Uso de bioinsumos nas áreas de produção agropecuária	",
                options=["Sim",
                         "Não"])

            porcentagem_bioinsumos = st.text_input(
                "Porcentagem de bioinsumos.", help="Caso afirmativo, qual a proporção da área de produção que adota esta prática (%)")
            tem_planta_cobertura = st.radio(
                "Uso de plantas de cobertura / plantas perenes para sombreamento**	",
                options=["Sim",
                         "Não"])
            porcentagem_planta_cobertura = st.text_input(
                "Porcentagem de plata cobertura", help="Caso afirmativo, qual a proporção da área de produção que adota esta prática (%)")

            st.subheader(
                "Gerenciamento de resíduos e efluentes gerados no imóvel rural")
            st.write(
                "Esgoto residências - destinação")
            df_destinacao_residuos = st.data_editor({
                "Tipos": ["Esgoto residências - destinação",
                          "Lixo domiciliar e das atividades - destinação"],
                "Residência rural": ["", ""],
                "Outras residência": ["", ""],
            })

            porcentagem_residuos_solidos_organicos = st.text_input(
                "*Resíduos sólidos orgânicos - compostagem e/ou reaproveitamento no campo", help="Preenchimento obrigatório")

            porcentagem_efluente_liquido = st.text_input(
                "Efluentes líquidos (quando existentes) - tratamento / destinação adequada", help="Deixar o campo em branco quando não houver geração de efluentes líquidos e/ou gasosos")

            porcentagem_efluente_gasosos = st.text_input(
                "Efluentes gasosos (quando existentes) - tratamento / destinação adequada", help="Deixar o campo em branco quando não houver geração de efluentes líquidos e/ou gasosos")
            tem_pontos_criticos_gestao_efluentes = st.radio(
                "Imóvel rural possui pontos críticos com relação à gestão de resíduos e efluentes",
                options=["Sim",
                         "Não"])
            descricao_pontos_criticos_gestao_efluentes = st.text_input(
                "Caso afirmativo - Especificar", help="Preenchimento caso a resposta anterior seja 'Sim'")

            st.subheader(
                "Estado de conservação das estradas que cortam e margeiam o imóvel rural")
            st.write(
                "Avaliação do estado de conservação e drenagem ")
            porcentagem_presenca_declividade = st.text_input(
                "Presença de declividade transversal ou abaulamento das estradas", help="Porcentual das estradas (%)")
            porcentagem_presenca_enxuradas = st.text_input(
                "Presença de lombadas para desvio de enxurrada", help="Porcentual das estradas (%)")
            porcentagem_presenca_caixa_infiltracao = st.text_input(
                "Presença de caixas de infiltração", help="Porcentual das estradas (%)")

            st.write(
                "Conservação das estradas")
            porcentagem_presenca_buraco_estradas = st.text_input(
                "Presença de buracos nas estradas", help="Porcentual das estradas (%)")
            porcentagem_presenca_erosao_estradas = st.text_input(
                "Presença de sulcos de erosão nas estradas", help="Porcentual das estradas (%)")

            st.write(
                "imóvel rural possui algum ponto crítico nas estradas*")
            tem_pontos_criticos_nas_estradas = st.radio(
                "imóvel rural possui algum ponto crítico nas estradas*",
                options=["Sim",
                         "Não"])
            descricao_pontos_criticos_estradas = st.text_input(
                "*Situação crítica - ESPECIFICAR*", help="Caso a resposta anterior seeja 'Sim'")

            st.subheader(
                "Vegetação nativa - fitofisionomias e estado de conservação")
            st.write(
                "Estágios sucessionais da vegetação nativa")
            fitofisionomias = st.data_editor({
                "Fitofisionomias (selecione)": ["Mata de galeria",
                                                "Vereda",
                                                "Mata atlântica/mata seca",
                                                "Vegetação de caatinga"],
                "Estágio avançado (área ha)": ["", "", "", ""],
                "Estágio médio (área ha)": ["", "", "", ""],
                "Estágio inicial (área ha)": ["", "", "", ""],
            })
            st.write(
                "Nº de fragmentos com vegetação nativa (no imóvel rural)")
            n_fragmento_vegetacao_nativa = st.text_input(
                "Unidade", help="Nº de fragmentos com vegetação nativa (no imóvel rural)")
            tem_vegetacao_nativa_junto_imoveis_visinhos = st.radio(
                "Fragmento(s) tem conexão com a vegetação nativa de imóveis rurais vizinhos",
                options=["Sim",
                         "Não"])
            tem_aceiro_munutencao_anual = st.radio(
                "Fragmento(s) protegidos do pastoreio e do fogo (aceiros com manutenção anual)",
                options=["Sim",
                         "Não"])

            # Every form must have a submit button.
            submitted = st.form_submit_button("Salvar")
            if submitted:
                if 'data' not in st.session_state:
                    st.session_state.data = pd.DataFrame(columns=['nome_colaborador',
                                                                  'cpf_colaborador',
                                                                  'nome_beneficiario',
                                                                  'cpf_cnpj_beneficiario',
                                                                  'idade_beneficiario',
                                                                  'geolocalizacao',
                                                                  'municipio',
                                                                  'estado',
                                                                  'nome_curso_dagua',
                                                                  'opcao_posse_terra',
                                                                  'sucessao',
                                                                  'participacao_mulher',
                                                                  'nome_imovel',
                                                                  'area_imovel',
                                                                  'agricultura_familiar',
                                                                  'df_area_contigua',
                                                                  'df_ocupacao_solo',
                                                                  'df_ocupacao_solo_car',
                                                                  'df_preservacao_car',
                                                                  'opcao_reserva_legal',
                                                                  'df_recuro_hidrico',
                                                                  'opcao_tipo_fonte_agua',
                                                                  'opcao_tem_problema_falta_agua',
                                                                  'especificar_problema_falta_agua',
                                                                  'opcao_regularizacao_ambiental',
                                                                  'opcao_licencimento_ambiental',
                                                                  'opcao_reserva_legal_regular',
                                                                  'problemas_enfrentados',
                                                                  "df_renda_bruta",
                                                                  "descricao_atividade_rural",
                                                                  "produtividade_rural_anual",
                                                                  "preco_anual_venda_rural",
                                                                  "df_renda_bruta_outras_atividades",
                                                                  "valor_outras_atividades_pensao_ajuda",
                                                                  "valor_outras_atividades_prestacao_servico",
                                                                  "qt_residencia_imovel",
                                                                  "df_servico_basico",
                                                                  "df_procucao_alimento",
                                                                  "df_escolaridade",
                                                                  "df_cursos_rurais",
                                                                  "df_frequencia_rede_ensino",
                                                                  "df_cumprimento_legistacao_trabalhista",
                                                                  "df_beneficios_ministerio_trabalho",
                                                                  "acesso_assistencia_tecnica",
                                                                  "participacao_assistencia_tecnica",
                                                                  "regularizacao_ambiental",
                                                                  "usa_credito_regularizacao_ambiental",
                                                                  "usa_custeio_regularizacao_ambiental",
                                                                  "usa_credito_comercializacao",
                                                                  "busca_informacoes_comercializacao",
                                                                  "gera_produtos_certificados",
                                                                  "usa_tecnicas_inovadoras",
                                                                  "descricao_tecnicas_inovadoras",
                                                                  "tem_potencial_inovador",
                                                                  "descricao_potencial_inovador",
                                                                  "usa_bioinsumos",
                                                                  "porcentagem_bioinsumos",
                                                                  "tem_planta_cobertura",
                                                                  "porcentagem_planta_cobertura",
                                                                  "df_destinacao_residuos",
                                                                  "porcentagem_residuos_solidos_organicos",
                                                                  "porcentagem_efluente_liquido",
                                                                  "porcentagem_efluente_gasosos",
                                                                  "tem_pontos_criticos_gestao_efluentes",
                                                                  "descricao_pontos_criticos_gestao_efluentes",
                                                                  "porcentagem_presenca_declividade",
                                                                  "porcentagem_presenca_enxuradas",
                                                                  "porcentagem_presenca_caixa_infiltracao",
                                                                  "porcentagem_presenca_buraco_estradas",
                                                                  "porcentagem_presenca_erosao_estradas",
                                                                  "tem_pontos_criticos_nas_estradas",
                                                                  "descricao_pontos_criticos_estradas",
                                                                  "fitofisionomias",
                                                                  "n_fragmento_vegetacao_nativa",
                                                                  "tem_vegetacao_nativa_junto_imoveis_visinhos",
                                                                  "tem_aceiro_munutencao_anual"])

                dados = {'nome_colaborador': nome_colaborador,
                         'cpf_colaborador': cpf_colaborador,
                         'nome_beneficiario': nome_beneficiario,
                         'cpf_cnpj_beneficiario': cpf_cnpj_beneficiario,
                         'idade_beneficiario': idade_beneficiario,
                         'geolocalizacao': geolocalizacao,
                         'municipio': municipio,
                         'estado': estado,
                         'nome_curso_dagua': nome_curso_dagua,
                         'opcao_posse_terra': opcao_posse_terra,
                         'sucessao': sucessao,
                         'participacao_mulher': participacao_mulher,
                         'nome_imovel': nome_imovel,
                         'area_imovel': area_imovel,
                         'agricultura_familiar': agricultura_familiar,
                         'df_area_contigua': str(df_area_contigua),
                         'df_ocupacao_solo': str(df_ocupacao_solo),
                         'df_ocupacao_solo_car': str(df_ocupacao_solo_car),
                         'df_preservacao_car': str(df_preservacao_car),
                         'opcao_reserva_legal': opcao_reserva_legal,
                         'df_recuro_hidrico': str(df_recuro_hidrico),
                         'opcao_tipo_fonte_agua': opcao_tipo_fonte_agua,
                         'opcao_tem_problema_falta_agua': str(opcao_tem_problema_falta_agua),
                         'especificar_problema_falta_agua': especificar_problema_falta_agua,
                         'opcao_regularizacao_ambiental': str(opcao_regularizacao_ambiental),
                         'opcao_licencimento_ambiental': str(opcao_licencimento_ambiental),
                         'opcao_reserva_legal_regular': str(opcao_reserva_legal_regular),
                         'problemas_enfrentados': problemas_enfrentados,
                         "df_renda_bruta": str(df_renda_bruta),
                         "descricao_atividade_rural": descricao_atividade_rural,
                         "produtividade_rural_anual": produtividade_rural_anual,
                         "preco_anual_venda_rural": preco_anual_venda_rural,
                         "df_renda_bruta_outras_atividades": str(df_renda_bruta_outras_atividades),
                         "valor_outras_atividades_pensao_ajuda": valor_outras_atividades_pensao_ajuda,
                         "valor_outras_atividades_prestacao_servico": valor_outras_atividades_prestacao_servico,
                         "qt_residencia_imovel": qt_residencia_imovel,
                         "df_servico_basico": str(df_servico_basico),
                         "df_procucao_alimento": str(df_procucao_alimento),
                         "df_escolaridade": str(df_escolaridade),
                         "df_cursos_rurais": str(df_cursos_rurais),
                         "df_frequencia_rede_ensino": str(df_frequencia_rede_ensino),
                         "df_cumprimento_legistacao_trabalhista": str(df_cumprimento_legistacao_trabalhista),
                         "df_beneficios_ministerio_trabalho": str(df_beneficios_ministerio_trabalho),
                         "acesso_assistencia_tecnica": acesso_assistencia_tecnica,
                         "participacao_assistencia_tecnica": participacao_assistencia_tecnica,
                         "regularizacao_ambiental": regularizacao_ambiental,
                         "usa_credito_regularizacao_ambiental": usa_credito_regularizacao_ambiental,
                         "usa_custeio_regularizacao_ambiental": usa_custeio_regularizacao_ambiental,
                         "usa_credito_comercializacao": usa_credito_comercializacao,
                         "busca_informacoes_comercializacao": busca_informacoes_comercializacao,
                         "gera_produtos_certificados": gera_produtos_certificados,
                         "usa_tecnicas_inovadoras": usa_tecnicas_inovadoras,
                         "descricao_tecnicas_inovadoras": descricao_tecnicas_inovadoras,
                         "tem_potencial_inovador": tem_potencial_inovador,
                         "descricao_potencial_inovador": descricao_potencial_inovador,
                         "usa_bioinsumos": usa_bioinsumos,
                         "porcentagem_bioinsumos": porcentagem_bioinsumos,
                         "tem_planta_cobertura": tem_planta_cobertura,
                         "porcentagem_planta_cobertura": porcentagem_planta_cobertura,
                         "df_destinacao_residuos": str(df_destinacao_residuos),
                         "porcentagem_residuos_solidos_organicos": porcentagem_residuos_solidos_organicos,
                         "porcentagem_efluente_liquido": porcentagem_efluente_liquido,
                         "porcentagem_efluente_gasosos": porcentagem_efluente_gasosos,
                         "tem_pontos_criticos_gestao_efluentes": tem_pontos_criticos_gestao_efluentes,
                         "descricao_pontos_criticos_gestao_efluentes": descricao_pontos_criticos_gestao_efluentes,
                         "porcentagem_presenca_declividade": porcentagem_presenca_declividade,
                         "porcentagem_presenca_enxuradas": porcentagem_presenca_enxuradas,
                         "porcentagem_presenca_caixa_infiltracao": porcentagem_presenca_caixa_infiltracao,
                         "porcentagem_presenca_buraco_estradas": porcentagem_presenca_buraco_estradas,
                         "porcentagem_presenca_erosao_estradas": porcentagem_presenca_erosao_estradas,
                         "tem_pontos_criticos_nas_estradas": tem_pontos_criticos_nas_estradas,
                         "descricao_pontos_criticos_estradas": descricao_pontos_criticos_estradas,
                         "fitofisionomias": fitofisionomias,
                         "n_fragmento_vegetacao_nativa": n_fragmento_vegetacao_nativa,
                         "tem_vegetacao_nativa_junto_imoveis_visinhos": tem_vegetacao_nativa_junto_imoveis_visinhos,
                         "tem_aceiro_munutencao_anual": tem_aceiro_munutencao_anual}

                df = pd.DataFrame(dados, index=[0])
                st.session_state.data = pd.concat(
                    [st.session_state.data, df], ignore_index=True)

                st.write("Gravado com sucesso!")

        st.write("Fim formulário!")

        st.write('## Tabela resultado: ')

        if 'data' in st.session_state:
            st.write(st.session_state.data)

        st.write("## Download")
        if 'data' in st.session_state:
            st.download_button(
                "📥 Download", st.session_state.data.to_csv(index=False), "data.csv", mime="text/csv")

    except Exception as e:
        st.error(f'Erro: {e}')
