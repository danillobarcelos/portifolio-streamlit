import streamlit as st
from data.projetos import PROJETOS

st.set_page_config(
    page_title="Danillo | Portifólio",
    page_icon="📊",
    layout="centered"
)

st.title("Danillo Fernandes Barcelos")
st.subheader("Suporte técnico em Redes -> Dados | Python • SQL • POWER BI")

st.write("Sou formado em Ciência da Computação e atuo atualmente como Suporte Técnico ao Cliente, com foco na resolução de problemas relacionados à conectividade, redes e serviços de telecomunicações. \n \n Tenho interesse em transição para a área de Dados, buscando aplicar meus conhecimentos em Python, SQL e Power BI para análise, organização e visualização de informações que apoiem a tomada de decisões. Atualmente, estou em constante desenvolvimento técnico por meio de estudos e projetos práticos voltados à análise de dados.")

st.divider()

st.subheader("Conhecimentos e contato")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Tecnologias**")
    st.markdown("- Python \n - SQL \n - Power BI")

with col2:
    st.markdown("**Contato**")
    st.markdown(
        "- [LinkedIn](https://www.linkedin.com/in/danillobarcelos/)\n"
        "- [GitHub](https://github.com/danillobarcelos)\n"
        "- danillofernandesb@gmail.com"
    )


st.divider()

st.subheader("Projetos")

for projeto in PROJETOS:
    with st.expander(f"**{projeto['titulo']}** \n {projeto['resumo']}"):
        st.write(projeto["descricao"])
        tecnologias_formatadas = " • ".join(projeto["tecnologias"])
        st.markdown(f"**Tecnologias:** {tecnologias_formatadas}")
        st.write("")

        if projeto["link_repo"]:
            st.markdown(f"[Veja o repositório no GitHub]({projeto['link_repo']})")
        if projeto["link_demo"]:
            st.markdown(f"Veja online]({projeto['link_demo']})")

st.divider()
st.caption("Feito com Python + Streamlit • Última atualização: 2026")