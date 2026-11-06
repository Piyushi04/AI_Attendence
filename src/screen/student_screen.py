


# import streamlit as st

# from src.ui.base_layout import style_background_dashboard, style_base_layout
# from src.components.header import header_dashboard
# from src.components.footer import footer_dashboard
# from PIL import Image
# import numpy as np
# from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
# from src.pipelines.voice_pipeline import get_voice_embedding
# from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
# from src.components.subject_card import subject_card
# import time
# from src.components.dialog_enroll import enroll_dialog




# def student_dashboard():
#     # Safely get student data from session state
#     if 'student_data' not in st.session_state:
#         st.error("Session expired. Please log in again.")
#         return

#     student_data = st.session_state.student_data
#     student_id = student_data['student_id']

#     c1, c2 = st.columns(2, vertical_alignment='center', gap='large')

#     with c1:
#         header_dashboard()

#     with c2:
#         st.subheader(f"Welcome, {student_data['name']}")
#         if st.button("Logout", type='secondary', key='loginbackbtn'):
#             st.session_state['is_logged_in'] = False
#             if 'student_data' in st.session_state:
#                 del st.session_state.student_data
#             st.rerun()

#     # Load data using student_id
#     with st.spinner('Loading your enrolled subjects..'):
#         subjects = get_student_subjects(student_id)
#         logs = get_student_attendance(student_id)

#     stats_map = {}
#     for log in logs:
#         sid = log['subject_id']
#         if sid not in stats_map:
#             stats_map[sid] = {"total": 0, "attended": 0}
#         stats_map[sid]['total'] += 1
        
#         if log.get('is_present'):
#             stats_map[sid]['attended'] += 1

#     cols = st.columns(2)
#     for i, sub_node in enumerate(subjects):
#         sub = sub_node['subjects']
#         sid = sub['subject_id']
#         stats = stats_map.get(sid, {"total": 0, "attended": 0})

#         # Passing student_id and sid as default arguments to avoid scoping errors
#         def unenroll_button(s_id=student_id, sub_id=sid):
#             if st.button("Unenroll from this course", type='tertiary', key=f"unenroll_{sub_id}", use_container_width=True):
#                 unenroll_student_to_subject(s_id, sub_id)
#                 st.success("Successfully unenrolled!")
#                 time.sleep(1)
#                 st.rerun()

#         with cols[i % 2]:
#             subject_card(
#                 name=sub['name'],
#                 code=sub['subject_code'],
#                 section=sub['section'],
#                 stats=[
#                     ('📅', 'Total', stats['total']),
#                     ('✅', 'Attended', stats['attended']),
#                 ],
#                 footer_callback=unenroll_button
#             )

#     footer_dashboard()



# def student_screen():

#     style_background_dashboard()
#     style_base_layout()

#     # Initialize registration flag
#     show_registration = False

#     if "student_data" in st.session_state:
#         student_dashboard()
#         return


#     c1, c2 = st.columns(2, vertical_alignment='center', gap='large')
#     with c1:
#         header_dashboard()
#     with c2:
#         if st.button("Go back to Home", type='secondary', key='loginbackbtn'):
#             st.session_state['login_type'] = None
#             st.rerun()

#     st.header('Login using FaceID')
#     st.write("") # spacing alternative

#     photo_source = st.camera_input("Position your face in the center")

#     if photo_source:
#         img = np.array(Image.open(photo_source))

#         with st.spinner('AI is scanning...'):
#             detected, all_ids, num_faces = predict_attendance(img)

#         if num_faces == 0:
#             st.warning('Face not found!')
#         elif num_faces > 1:
#             st.warning('Multiple faces found')
#         else:
#             if detected:
#                 student_id = list(detected.keys())[0]
#                 all_students = get_all_students()
#                 student = next((s for s in all_students if s['student_id'] == student_id), None)

#                 if student:
#                     st.session_state.is_logged_in = True
#                     st.session_state.user_role = 'student'
#                     st.session_state.student_data = student
#                     st.toast(f"Welcome Back {student['name']}")
#                     time.sleep(1)
#                     st.rerun()
#                 else:
#                     pass
#             else:
#                 st.info('Face not recognized! You might be a new student!')
#                 show_registration = True

#     if show_registration:
#         with st.container(border=True):
#             st.header('Register new Profile')
#             new_name = st.text_input("Enter your name", placeholder='E.g. Hamza Rizvi')

#             st.subheader('Optional : Voice Enrollment')
#             st.info("Enroll your for voice only attendance")

#             audio_data = None

#             try:
#                 audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
#             except Exception:
#                 st.error('Audio Data failed!')

#             if st.button('Create Account', type='primary'):
#                 if new_name:
#                     with st.spinner('Creating profile..'):
#                         img = np.array(Image.open(photo_source))
#                         encodings = get_face_embeddings(img)
#                         if encodings:
#                             face_emb = encodings[0].tolist()

#                             voice_emb = None
#                             if audio_data:
#                                 voice_emb = get_voice_embedding(audio_data.read())

#                             response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

#                             if response_data:
#                                 train_classifier()
#                                 st.session_state.is_logged_in = True
#                                 st.session_state.user_role = 'student'
#                                 st.session_state.student_data = response_data[0]
#                                 st.toast(f'Profile Created! Hi {new_name}!')
#                                 time.sleep(1)
#                                 st.rerun()
#                             else:
#                                 st.error('Couldnt capture your facial features for registration')
#                         else:
#                             st.error('Couldnt capture your facial features for registration')
#                 else:
#                     st.warning('Please enter your name!')

#     footer_dashboard()
































































import streamlit as st
import time
import numpy as np
from PIL import Image

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import (
    get_all_students, 
    create_student, 
    get_student_subjects, 
    get_student_attendance, 
    unenroll_student_to_subject
)
from src.components.subject_card import subject_card
from src.components.dialog_enroll import enroll_dialog


def student_dashboard():
    if 'student_data' not in st.session_state:
        st.error("Session expired. Please log in again.")
        return

    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    top_col1, top_col2 = st.columns([3, 1], vertical_alignment='center')

    with top_col1:
        header_dashboard()

    with top_col2:
        st.markdown(f"### 👋 Welcome, **{student_data['name']}**")
        if st.button("🚪 Logout", type='secondary', key='logout_btn', use_container_width=True):
            st.session_state['is_logged_in'] = False
            if 'student_data' in st.session_state:
                del st.session_state.student_data
            st.rerun()

    st.markdown("---")

    with st.spinner('Loading your enrolled subjects...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    st.subheader("📚 Enrolled Subjects")
    
    if not subjects:
        st.info("You are not currently enrolled in any subjects.")
    else:
        cols = st.columns(2)
        for i, sub_node in enumerate(subjects):
            sub = sub_node['subjects']
            sid = sub['subject_id']
            stats = stats_map.get(sid, {"total": 0, "attended": 0})

            def unenroll_button(s_id=student_id, sub_id=sid):
                if st.button("🗑️ Unenroll from course", type='tertiary', key=f"unenroll_{sub_id}", use_container_width=True):
                    unenroll_student_to_subject(s_id, sub_id)
                    st.success("Successfully unenrolled!")
                    time.sleep(1)
                    st.rerun()

            with cols[i % 2]:
                with st.container(border=True):
                    subject_card(
                        name=sub['name'],
                        code=sub['subject_code'],
                        section=sub['section'],
                        stats=[
                            ('📅', 'Total Sessions', stats['total']),
                            ('✅', 'Attended', stats['attended']),
                        ],
                        footer_callback=unenroll_button
                    )

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns([3, 1], vertical_alignment='center')
    with c1:
        header_dashboard()
    with c2:
        if st.button("⬅️ Back to Home", type='secondary', key='loginbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.markdown("---")
    
    col_center, _ = st.columns([2, 1])
    show_registration = False
    
    with col_center:
        with st.container(border=True):
            st.header('📸 Student FaceID Login')
            st.caption("Center your face clearly inside the camera frame below to authenticate.")
            
            photo_source = st.camera_input("", key="face_id_camera")

            if photo_source:
                img = np.array(Image.open(photo_source))

                with st.spinner('🔍 AI is scanning facial features...'):
                    detected, all_ids, num_faces = predict_attendance(img)

                if num_faces == 0:
                    st.warning('⚠️ No face detected. Please position yourself clearly.')
                elif num_faces > 1:
                    st.warning('⚠️ Multiple faces detected! Please stay solo in the camera frame.')
                else:
                    if detected:
                        student_id = list(detected.keys())[0]
                        all_students = get_all_students()
                        student = next((s for s in all_students if s['student_id'] == student_id), None)

                        if student:
                            st.session_state.is_logged_in = True
                            st.session_state.user_role = 'student'
                            st.session_state.student_data = student
                            st.toast(f"Welcome back, {student['name']}! 🎉")
                            time.sleep(1)
                            st.rerun()
                    else:
                        st.info('👤 Face not recognized. If you are a new student, complete registration below!')
                        show_registration = True

    if show_registration:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.header('📝 Register New Student Profile')
            st.caption("Complete your profile setup to register your FaceID and Voice signature.")
            
            new_name = st.text_input("Full Name", placeholder='E.g. Hamza Rizvi')

            st.markdown("### 🎙️ Optional: Voice Enrollment")
            st.caption("Record your voice to enable backup voice-recognition attendance.")

            audio_data = None
            try:
                audio_data = st.audio_input('Record a short phrase (e.g., "I am present, My name is Akash.")')
            except Exception:
                st.error('Audio input service failed to initialize.')

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button('✨ Create Account & Finish Registration', type='primary', use_container_width=True):
                if new_name:
                    with st.spinner('Registering profile and saving embeddings...'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(
                                new_name, 
                                face_embedding=face_emb, 
                                voice_embedding=voice_emb
                            )

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Welcome aboard, {new_name}!')
                                time.sleep(1)
                                st.rerun()
                            else:
                                st.error('Failed to save profile. Please try capturing again.')
                        else:
                            st.error('Could not extract facial features. Please ensure proper lighting.')
                else:
                    st.warning('Please enter your full name before submitting!')

    footer_dashboard()