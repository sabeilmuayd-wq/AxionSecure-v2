import streamlit as st
import datetime

# --- إعدادات النظام ---
st.set_page_config(page_title="Logistics Manager", page_icon="📈", layout="centered")

# --- نظام الحماية بالـ PIN ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_access():
    if not st.session_state["authenticated"]:
        st.title("🛡️ System Locked")
        pin = st.text_input("Security Code (PIN)", type="password")
        if st.button("Unlock"):
            if pin == "1920":  # يمكنك تغيير هذا الرقم السري
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Access Denied")
        return False
    return True

if check_access():
    st.sidebar.title("Admin Console")
    menu = st.sidebar.radio("Navigation", ["Protection", "Project Sheith", "Assets"])

    if menu == "Protection":
        st.header("🛡️ Active Protection Protocols")
        st.info("قم بتفعيل الدرع يومياً عند الفجر والمغرب")
        
        if st.button("Activate Morning Shield (🌅)"):
            st.success("تم تفعيل جدار الحماية الصباحي. (الفاتحة، الكرسي، المعوذات)")
            
        if st.button("Activate Night Shield (🌇)"):
            st.warning("تم تفعيل بروتوكول الحجب المسائي. (خواتيم البقرة، الكرسي)")

    elif menu == "Project Sheith":
        st.header("🏥 Medical Logistics: Sheith")
        st.write("**Status:** In Transit to Kampala")
        st.progress(60)
        
        st.subheader("📋 Doctor's Brief (Copy for Clinic)")
        st.code("Patient: Sheith (4y). Case: Post-circumcision complications, Urinary retention. Priority: Pediatric Urology.", language="text")

    elif menu == "Assets":
        st.header("💰 Financial Tracking")
        balance = st.number_input("Available Cash (UGX)", value=0)
        st.metric("Safe Liquidity", f"{balance} UGX")

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()
