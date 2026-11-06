# import streamlit as st
# from src.components.header import header_home
# from src.components.footer import footer_home
# from src.ui.base_layout import style_base_layout, style_background_home
# def home_screen():
#     header_home()
#     style_base_layout()
#     style_background_home()
#     col1, col2 = st.columns(2, gap="large")

#     with col1:
#         st.header("Student")
#         st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDPom79fAPYqZMY3x_qEIEkE-vBSF3suvNZnnKkvFhJmsQkhhsbAPk6ofV&s=10", width=150)
#         if st.button('Student Portal',type='primary', icon=':material/arrow_outward:'):
#             st.session_state['login_type'] = 'student'
#             st.rerun()
#     with col2:
#         st.header("Teacher")
#         st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRLDo1Gpcs5LUzuGfXMCkwumiKG2xe28WeXsubAuKoYTiI0FUO7g4mIM4&s=10", width=150)
#         if st.button('Teacher Portal',type='primary', icon=':material/arrow_outward:', ):
#             st.session_state['login_type'] = 'teacher'
#             st.rerun()
#     footer_home()









import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    style_base_layout()
    style_background_home()
    
    # Custom Header text change to "AI Attendance Classroom"
    st.markdown(
        """
        <div style="text-align: center; padding-bottom: 2rem;">
            <h1>🎓 AI Attendance Classroom</h1>
            <p>Smart, automated attendance tracking for students and teachers</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("Student")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDPom79fAPYqZMY3x_qEIEkE-vBSF3suvNZnnKkvFhJmsQkhhsbAPk6ofV&s=10", width=150)
        # Fixed icon syntax or replaced with a reliable icon string
        if st.button('Student Portal', type='primary', icon='↗', key='student_btn'):
            st.session_state['login_type'] = 'student'
            st.rerun()
            
    with col2:
        st.header("Teacher")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRLDo1Gpcs5LUzuGfXMCkwumiKG2xe28WeXsubAuKoYTiI0FUO7g4mIM4&s=10", width=150)
        # Fixed icon syntax or replaced with a reliable icon string
        if st.button('Teacher Portal', type='primary', icon='↗', key='teacher_btn'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
            
    footer_home()