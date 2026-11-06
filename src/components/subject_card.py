
import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
  # 1. Build the main card HTML
  html = f"""
    <div style="background:white; border-left: 8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid #e2e8f0; margin-bottom: 10px;">
        <h3 style="margin:0; color: #1e293b; font-size: 1.5rem;">{name}</h3>
        <p style="color:#64748b; margin:10px 0;">
            Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px;">{code}</span> 
            &nbsp;&nbsp; Section : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px;">{section}</span>
        </p>
    """

  # 2. Append the stats inside the same HTML block if they exist
  if stats:
    html += '<div style="display:flex; gap:8px; flex-wrap:wrap; margin-top: 10px;">'
    for icon, label, value in stats:
      html += f'<div style="background: #EB459E10; padding:5px 12px; border-radius:12px; font-size:0.9rem;">{icon} <b>{value}</b> {label}</div>'
    html += '</div>'

  # Close the outer card div wrapper properly
  html += '</div>'

  # 3. Render everything at once with unsafe_allow_html=True
  st.markdown(html, unsafe_allow_html=True)

  if footer_callback:
    footer_callback()