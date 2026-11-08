import streamlit as st

# 1. إعداد عنوان الصفحة والتصميم
st.set_page_config(page_title="المارش الأخضر", page_icon="🛡️", layout="centered")

# 2. واجهة التطبيق الرئيسية
st.title("🛡️ منظومة المارش الأخضر")
st.write("غرفة التحكم المركزية - فريق العمل الميداني")

st.divider()

# 3. قسم كتابة المحتوى والوسائط
st.subheader("✍️ تجهيز المنشور:")
post_content = st.text_area("اكتب نص المنشور أو الخبر هنا:", placeholder="ابدأ الكتابة...", height=150)

uploaded_file = st.file_uploader("📁 أرفق صورة أو فيديو قصير:", type=["png", "jpg", "jpeg", "mp4"])

if uploaded_file is not None:
    if uploaded_file.type.startswith('image'):
        st.image(uploaded_file, caption='معاينة الصورة', use_column_width=True)
    elif uploaded_file.type.startswith('video'):
        st.video(uploaded_file)

st.divider()

# 4. تحديد وجهات النشر
st.subheader("🌐 تحديد وجهات النشر:")
col1, col2 = st.columns(2)
with col1:
    publish_to_fb = st.checkbox("فيسبوك (الصفحات المربوطة)")
with col2:
    send_to_telegram = st.checkbox("غرفة تيليجرام المركزية")

st.divider()

# 5. زر النشر والتنفيذ
if st.button("🚀 إطلاق ونشر فوري للمحتوى", type="primary"):
    if not post_content and not uploaded_file:
        st.warning("⚠️ يرجى كتابة محتوى أو إرفاق ملف قبل النشر!")
    else:
        st.info("🕒 جاري إرسال المحتوى إلى الشبكة...")
        st.success("✅ تم إرسال المحتوى بنجاح إلى الوجهات المحددة!")
