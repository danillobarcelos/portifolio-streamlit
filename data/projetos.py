"""
data/projetos.py

Este arquivo guarda os dados dos projetos do portfólio, separados da lógica
visual (que fica no app.py). Cada projeto é um dicionário dentro da lista
PROJETOS — assim, pra adicionar um projeto novo, você só acrescenta um
dicionário aqui, sem precisar tocar no código que desenha a página.

Por que uma lista de dicionários e não, por exemplo, uma classe?
Pra esse caso (dados simples, sem comportamento/métodos associados),
um dict já é suficiente e mais direto de ler. Se no futuro você quiser
adicionar validação (ex: garantir que 'titulo' nunca venha vazio) ou
métodos (ex: projeto.resumo()), aí faria sentido evoluir pra uma classe
ou um dataclass. Por enquanto, simplicidade > engenharia prematura.
"""

PROJETOS = [
    {
        "titulo": "Análise de Chamados de Suporte Técnico N1",
        "resumo": "Análise exploratória de chamados de uma central de suporte, "
                   "identificando padrões de tempo de resolução e principais causas.",
        "descricao": (
            "Projeto que simula uma base de chamados de suporte técnico N1 "
            "(o mesmo tipo de chamado que eu lido no dia a dia em uma provedora "
            "de internet) e aplica análise de dados para responder perguntas "
            "como: Quais são os motivos de chamado mais recorrentes? Qual o "
            "tempo médio de resolução por categoria? Existem picos de chamados "
            "em horários ou dias específicos da semana?\n\n"
            "O objetivo é mostrar como dados operacionais do suporte podem "
            "gerar insights práticos para a gestão da equipe, como "
            "redistribuição de turnos ou identificação de problemas recorrentes "
            "que merecem solução definitiva."
        ),
        "tecnologias": ["Python", "Pandas", "Power BI", "SQL"],
        "link_repo": "https://github.com/seu-usuario/analise-chamados-suporte",
        "link_demo": "",  # preencha se tiver um dashboard publicado
    },
    {
        "titulo": "Dashboard de Qualidade de Conexão de Rede",
        "resumo": "Dashboard interativo para monitorar indicadores de qualidade "
                   "de rede como latência, uptime e velocidade por região.",
        "descricao": (
            "Dashboard que consolida métricas de qualidade de conexão "
            "(latência, uptime, velocidade média) segmentadas por região e "
            "tipo de plano, permitindo identificar áreas com maior incidência "
            "de instabilidade.\n\n"
            "Os dados são tratados com SQL para consultas e agregações, e "
            "visualizados em um dashboard interativo, permitindo filtros "
            "dinâmicos por período e região. O projeto demonstra a aplicação "
            "de conhecimento técnico de redes (da minha experiência como "
            "suporte N1) junto com ferramentas de Análise de Dados."
        ),
        "tecnologias": ["SQL", "Power BI", "Python"],
        "link_repo": "https://github.com/seu-usuario/dashboard-qualidade-rede",
        "link_demo": "",
    },
]
