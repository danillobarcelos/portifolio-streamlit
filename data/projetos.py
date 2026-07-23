PROJETOS = [
    {
        "titulo": "MapBiomas Brasil — Pipeline de Engenharia e Análise de Dados",
        "resumo": "Projeto de engenharia e análise de dados usando dados de área por classe de cobertura e uso da terra do MapBiomas Brasil.",
        "descricao": (
            "Pipeline de dados ponta a ponta, construído em Python, aplicado à base \"Uso e Cobertura da Terra - Bioma e Divisão Política\" do MapBiomas Brasil — dados de área (hectares) por classe de cobertura e uso da terra, cruzando bioma, estado e município, para o período de 1985 a 2024 (mais de 3 milhões de registros após tratamento). \n\n"
            "O projeto está dividido em duas frentes: Engenharia de Dados, estruturada segundo a arquitetura medalhão (Bronze - Prata - Ouro), cobrindo ingestão, padronização, tipagem, tradução de metadados para português e transformação de formato wide para long (unpivot) das 40 colunas de anos originais; e Análise de Dados, explorando os dados tratados para gerar insights sobre desmatamento, avanço da agropecuária, urbanização e transformação do uso da terra por bioma e estado. \n\n"
            "Todo o tratamento e as transformações foram feitos via SQL rodando em DuckDB, com cada camada validada (checagem de nulos, valores negativos e conservação de somas entre etapas de agregação) e exportada em formato Parquet, versionado no GitHub.\n\n"
            "Status atual: camadas Bronze, Prata e Ouro completas e versionadas. Em desenvolvimento: notebook de análise e visualização de insights (matplotlib)."
        ),
        "tecnologias": ["Python", "DuckDB", "Jupyter Notebook", "Pandas", "Matplotlib", "Git & GitHub", "Parquet"],
        "link_repo": "https://github.com/danillobarcelos/mapbiomas-pipeline", 
        "link_demo": "",
    },
    {
        "titulo": "Insurance Data Analysis",
        "resumo": "Análise de dados sobre seguro de vida, saúde, automóveis, casa e viagens",
        "descricao": (
            "Projeto em Power BI com análises sobre apólices de seguro de Viagem, Saúde, Automóveis, Vida e de Casa. Os dados foram obtidos através do Bootcamp \"Complete Data Analyst Bootcamp From Basics To Advanced\" da Udemy. \n\n"
            "O Dashboard apresenta uma página inicial com possibilidade de filtrar os dados por Gênero, número de Solicitação de Pedido, ID do cliente. Além disso, há uma segunda página onde foi possível entender e aplicar o conceito de Drill Through. Os dados foram conectados ao Power BI atráves do Banco de Dados Microsoft SQL Server. \n\n"
            "Uma terceira página foi adicionada com uma nova tabela no formato xlsx. Essa tabela contém algumas avaliações do serviço prestado pela empresa. Usando Python, foi criado um script que lê a tabela e classifica o Feedback de cada cliente de forma númerica, proporcionando um Score do Sentimento do Cliente. Foram usados a biblioteca Pandas, VaderSentiment e Openpyxl.\n\n"
            "Além de publicado, foi também trabalhado as funcionalidades de conexão do Banco de Dados com o serviço do Power BI e de agendamento de atualizações. Foi possível também criar e gerenciar funções dentro do Dashboard, permitindo visualizações filtradas para diferentes publicos."
        ),
        "tecnologias": ["Python", "Pandas", "Power BI", "SQL", "Excel"],
        "link_repo": "https://github.com/danillobarcelos/Insurance-Data-Analysis",
        "link_demo": "https://app.powerbi.com/groups/21dea8c1-418b-4c8f-b4a5-93adef3f27c5/reports/a2e56b1a-9364-4498-91b2-d92b8392e2ce?ctid=f310b526-e195-4805-a55e-67e28f2fefdb&pbi_source=linkShare&bookmarkGuid=e89296ed-2f09-4ab3-ab39-175aeddec1ef", 
    },
    {
        "titulo": "Análise de Preços de Placa de Vídeo",
        "resumo": "Coleta, tratamento e analise de dados por meio de Web Scraping",
        "descricao": ("Este projeto tem como objetivo realizar a coleta, tratamento e análise exploratória de dados (EDA) de preços de placas de vídeo anunciadas no Mercado Livre.\n\n"
        "Os dados foram obtidos por meio de web scraping com Python, seguidos de limpeza, organização e análises estatísticas e visuais, com o intuito de identificar padrões de preços, comportamento das lojas e possíveis relações entre avaliações e valores dos produtos."
        ),
        "tecnologias": ["Python", "Requests ", "BeautifulSoup", "Seaborn", "Matplotlib"],
        "link_repo": "https://github.com/danillobarcelos/mercado-livre-precos",
        "link_demo": "",
    },
]
