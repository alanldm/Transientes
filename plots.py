import streamlit as st
st. set_page_config(layout="wide")
import matplotlib.pyplot as plt
import calc

st.title("Cálculo de Transientes")

col1, col2 = st.columns(2)

with col1:
    vs = st.text_input("Informe a tensão da fonte (Vs): ")
    zs = st.text_input("Informe a impedância da fonte (Rs): ")
    z0 = st.text_input("Informe a impedância característica da linha (Z0): ")
    zl = st.text_input("Informe a impedância da carga (Zl): ")
    vp = st.text_input("Informe a velocidade de propagação na linha (Vp): ")
    l = st.text_input("Informe o comprimento da linha (l): ")
    f = st.text_input("Informe o tempo máximo da análise (f): ")
    tipo = st.radio("Informe o tipo de análise", ("Início da linha", "Meio da linha", "Fim da linha"), horizontal=True)
    go = st.button("Calcular")

with col2:
    if go==True:
        tl = calc.t_l(float(zl), float(z0))
        ts = calc.t_s(float(zs), float(z0))
        t = calc.time(float(l), float(vp))
        v0 = calc.v_0(float(vs), float(z0), float(zs))
        vl = calc.v_l(float(vs), float(z0), float(zl))

        if tipo=="Meio da linha":
            i = float(t/2)
            p = float(t)
        elif tipo=="Fim da linha":
            i = float(t)
            p = float(2*t)
        else:
            i = float(0)
            p = float(2*t)

        st.markdown("Resultados: ")
        st.text(f"tl = {str(tl)}")
        st.text(f"ts = {str(ts)}")
        st.text(f"t = {str(t)}ns")
        st.text(f"v0 = {str(v0)}V")
        st.text(f"vl = {str(vl)}V")

        result = calc.calc_ten(v0, int(i), int(f), p, t, tl, ts)

        fig, ax = plt.figure()

        ax.plot(result[1], result[0])

        st.pyplot(fig)
