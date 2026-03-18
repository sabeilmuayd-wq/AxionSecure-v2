import streamlit as st
import datetime

# --- إعدادات الصفحة (تظهر في المتصفح) ---
st.set_page_config(page_title="نظام أكسيون الآمن", page_icon="🛡️", layout="centered")

# --- تنسيق واجهة الهاتف (CSS) ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 15px; height: 3.5em; background-color: #004d40; color: white; font-size: 18px; font-weight: bold; }
    .stHeader { color: #004d40; text-align: center; }
    .reportview-container { background: #f0f2f6; }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الحماية بكلمة السر (الـ PIN) ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def تسجيل_الدخول():
    if not st.session_state["authenticated"]:
        st.header("🛡️ نظام الحماية المشفر")
        st.subheader("يرجى إدخال رمز الوصول الآمن")
        
        رقم_سري = st.text_input("رمز الدخول (PIN)", type="password", help="أدخل الرمز المكون من 4 أرقام")
        
        if st.button("فتح النظام"):
            if رقم_سري == "1920": # كلمة السر المتفق عليها
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("⚠️ الرمز غير صحيح. حاول مجدداً.")
        return False
    return True

# --- تشغيل التطبيق بعد التحقق ---
if تسجيل_الدخول():
    
    # القائمة الجانبية للتنقل
    st.sidebar.title("🎛️ قائمة التحكم")
    الخيار = st.sidebar.radio("انتقل إلى:", ["درع التحصين", "ملف شيث الطبي", "إدارة الأموال"])

    # 1. قسم درع التحصين (Protection)
    if الخيار == "درع التحصين":
        st.header("🛡️ بروتوكولات الحماية اليومية")
        st.info("تفعيل هذه الأوراد يكسر عوارض التعطيل والسحر بإذن الله.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🌅 ورد الصباح"):
                st.success("✅ تم تفعيل درع الصباح")
                st.markdown("""
                **الأذكار المطلوبة:**
                * الفاتحة (7 مرات)
                * آية الكرسي (3 مرات)
                * الإخلاص والمعوذات (3 مرات)
                """)
                
        with col2:
            if st.button("🌇 ورد المساء"):
                st.warning("✅ تم تفعيل درع المساء")
                st.markdown("""
                **الأذكار المطلوبة:**
                * خواتيم سورة البقرة
                * آية الكرسي
                * أعوذ بكلمات الله التامات (3 مرات)
                """)

    # 2. قسم ملف شيث (Medical Brief)
    elif الخيار == "ملف شيث الطبي":
        st.header("🏥 ملف المريض: شيث")
        st.write("**الحالة الحالية:** في الطريق إلى كمبالا (Transit)")
        
        st.subheader("📝 ملخص للطبيب (جاهز للنسخ)")
        ملاحظة_الطبيب = """الاسم: شيث (4 سنوات).
التشخيص المبدئي: مضاعفات طهور جائر، احتباس بولي، صعوبة تبول.
المطلوب: عرض على استشاري مسالك بولية للأطفال فورا."""
        
        st.code(ملاحظة_الطبيب, language="text")
        
        st.info("💡 اعرض هذا الكود على الطبيب في مستشفى Uro Care لتسريع الإجراءات.")

    # 3. قسم إدارة الأموال (Finance)
    elif الخيار == "إدارة الأموال":
        st.header("💰 تتبع الميزانية (أكسيون)")
        المبلغ_المتوفر = st.number_input("المبلغ الحالي (شلن أوغندي)", value=0)
        المصاريف = st.number_input("مصاريف الرحلة والعلاج", value=0)
        
        صافي_المبلغ = المبلغ_المتوفر - المصاريف
        st.metric("الرصيد الآمن المتبقي", f"{صافي_المبلغ} UGX")

    # زر تسجيل الخروج للأمان
    st.sidebar.divider()
    if st.sidebar.button("🔒 خروج آمن"):
        st.session_state["authenticated"] = False
        st.rerun()

    # نصيحة الوعي المتغيرة
    st.divider()
    st.caption("💡 تذكر: أنت الآن 'حاكم' لقرارك، والوعي هو سلاحك الأقوى.")
