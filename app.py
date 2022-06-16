import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio
#from re import template

pio.templates.default = "plotly_dark"

st.set_page_config(layout="wide")

#Create header
st.write("""# TWG Radar Chart Generator""")
st.write("""## How it works""")
st.write("Put in your stats on the sidebar, then a radar chart similar to TWG should be generated."
         "Depending if I got around to it, there may be additional features such as plot customisation options.")

#Create and name sidebar
#https://docs.streamlit.io/library/api-reference/widgets/st.number_input

st.sidebar.header('Select your stats!')

with st.sidebar:
    attack_bonus = st.number_input('Insert your Attack Bonus', min_value = 5)
    st.write('Your Attack Bonus is ', attack_bonus)

    ddi = st.number_input('Insert your DDI', min_value = 5)
    st.write('Your DDI is ', ddi)

    health_points = st.number_input('Insert your Health Points', min_value = 100, value = 500)
    st.write('Your Health Points is ', health_points)

    stamina = st.number_input('Insert your Stamina', min_value = 100, value = 1000)
    st.write('Your Stamina is ', stamina)

    dodge = st.number_input('Insert your Dodge', min_value = 5)
    st.write('Your Dodge is ', dodge)

    block = st.number_input('Insert your Block', min_value = 5)
    st.write('Your Block is ', block)

    bleed_bonus = st.number_input('Insert your Bleed Bonus', min_value = 5)
    st.write('Your Bleed Bonus is ', bleed_bonus)

    stamina_reducer = st.number_input('Insert your Stamina Reducer', min_value = 5)
    st.write('Your Stamina Reducer is ', stamina_reducer)

    damage_reducer = st.number_input('Insert your Damage Reducer', min_value = 5)
    st.write('Your Damage Reducer is ', damage_reducer)

    sdi = st.number_input('Insert your SDI', min_value = 5)
    st.write('Your SDI is ', sdi)

    sub_bonus = st.number_input('Insert your Sub Bonus', min_value = 5)
    st.write('Your Sub Bonus is ', sub_bonus)

    escape_sub = st.number_input('Insert your Escape Sub', min_value = 5)
    st.write('Your Attack Bonus is ', escape_sub)

stat_values = [
        attack_bonus + ddi,  # Attack
        round((health_points + stamina)/20, 0), # Vitality 
        block + dodge, # Defense 
        bleed_bonus + ddi, # Damage
        stamina_reducer + damage_reducer, # Resistance
        sdi + sub_bonus, # Submission
        escape_sub + escape_sub # Sub Defense
        ]
    
stat_names = ['Attack', 'Vitality', 'Defense', 'Damage', 'Resistance', 'Submission', 'Sub Defense']

fig = go.Figure(data=go.Scatterpolar(
  r = stat_values,
  theta = stat_names,
  fill = 'toself'
))

fig.update_layout(
  polar = dict(
    radialaxis = dict(
      visible = True, showticklabels = False
    ),
    angularaxis = dict(direction = 'clockwise')
  ),
  showlegend = False
)

st.plotly_chart(fig, use_container_width=True)






