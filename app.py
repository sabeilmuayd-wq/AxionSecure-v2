import streamlit as st
import datetime

# --- إعدادات النظام الذكي ---
st.set_page_config(page_title="Axion Intelligence v3", page_icon="🧠", layout="centered")

# --- تنسيق احترافي للهواتف ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; background-color: #004d40; color: white; font-weight: bold; }
    .status-card { padding: 15px; border-radius: 10px; border-left: 5px solid #004d40; background-color: #f9f9f9; margin-bottom: 10px; }
    .emergency-btn { background-color: #d32f2f !important; }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الحماية الذكي ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.header("🔐 الدخول للنظام الذكي")
    pin = st.text_input("رمز الوصول الخاص (PIN)", type="password")
    if st.button("فتح النظام"):
        if pin == "1920":
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("رمز غير صحيح")
else:
    # --- شريط التنقل الذكي ---
    st.sidebar.title("🧠 ذكاء أكسيون")
    tab = st.sidebar.radio("المهام الحالية:", ["التحصين الرقمي", "مساعد التشخيص", "محرك الأصول", "طوارئ كمبالا"])

    # 1. التحصين الرقمي (الذكاء الروحي)
    if tab == "التحصين الرقمي":
        st.header("🛡️ بروتوكول الحماية النشط")
        time_now = datetime.datetime.now().hour
        if 4 <= time_now <= 10:
            st.info("💡 النظام يقترح: تفعيل **ورد الصباح** الآن.")
        elif 16 <= time_now <= 20:
            st.warning("💡 النظام يقترح: تفعيل **درع المساء** قبل تحرك الحافلة.")
        
        with st.expander("📖 عرض الأذكار كاملة"):
            st.markdown("""
            **ورد الصباح:** الفاتحة (7)، الكرسي (3)، الإخلاص والمعوذات (3)، بسم الله الذي لا يضر.. (3).
            **درع المساء:** الكرسي، خواتيم البقرة، حسبي الله لا إله إلا هو (7).
            """)

    # 2. مساعد التشخيص (Intelligence Triage)
    elif tab == "مساعد التشخيص":
        st.header("🏥 مساعد التشخيص الذكي")
        st.write("أجب لتقييم حالة شيث الآن:")
        
        pain_level = st.select_slider("مستوى الألم عند شيث (1-10):", options=range(1, 11))
        retention = st.radio("هل يتبول بانتظام؟", ["نعم", "بصعوبة شديدة", "لا يتبول أبداً"])
        
        if retention == "لا يتبول أبداً" or pain_level > 8:
            st.error("🚨 حالة طارئة: توجه لأقرب مستشفى فور وصولك كمبالا!")
        else:
            st.success("✅ الحالة مستقرة نسبياً: التزم بموعد مستشفى Uro Care.")

        st.divider()
        st.subheader("📋 Clinical Summary (English)")
        st.code(f"Patient: Sheith (4y). Status: Post-circ trauma. Pain: {pain_level}/10. Urine Retention: {retention}.", language="text")

    # 3. محرك الأصول (Asset Engine)
    elif tab == "محرك الأصول":
        st.header("💰 حاسبة أكسيون المالية")
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("المبلغ الحالي (UGX)", value=100000)
        with col2:
            rate = st.number_input("سعر الصرف (SDG لكل 1000 UGX)", value=1.5)
        
        converted = (amount / 1000) * rate
        st.metric("القيمة التقريبية بالجنيه السوداني", f"{converted:.2f} SDG")

    # 4. طوارئ كمبالا (Emergency Locator)
    elif tab == "طوارئ كمبالا":
        st.header("🚨 دليل الوصول السريع")
        st.markdown("""
        <div class="status-card">
        <b>🏥 مستشفى Uro Care (نانسانا):</b><br>
        هاتف: <a href="tel:+256393262132">+256 393 262 132</a><br>
        <b>🚕 تاكسي أوبر (Uber):</b> متاح 24 ساعة في كمبالا.
        </div>
        """, unsafe_allow_html=True)
        if st.button("📍 فتح موقع المستشفى على الخريطة"):
            st.write("استخدم الرابط في المتصفح: https://maps.app.goo.gl/uXv7m")

    # زر الخروج
    if st.sidebar.button("🔐 خروج آمن"):
        st.session_state["authenticated"] = False
        st.rerun()
