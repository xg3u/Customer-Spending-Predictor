import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
import json

# Page configuration
st.set_page_config(
    page_title="Customer Spending Score Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'language' not in st.session_state:
    st.session_state.language = 'en'
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'
if 'age' not in st.session_state:
    st.session_state.age = 35
if 'income' not in st.session_state:
    st.session_state.income = 50000
if 'membership_years' not in st.session_state:
    st.session_state.membership_years = 5
if 'purchase_frequency' not in st.session_state:
    st.session_state.purchase_frequency = 25
if 'prediction_made' not in st.session_state:
    st.session_state.prediction_made = False
if 'score' not in st.session_state:
    st.session_state.score = None

# Translations dictionary
translations = {
    'en': {
        'title': 'Customer Spending Score Predictor',
        'subtitle': 'Predict customer value and get actionable business insights',
        'customer_info': 'Customer Information',
        'age': 'Age',
        'age_label': 'Select customer age',
        'age_help': 'Age of the customer in years',
        'annual_income': 'Annual Income',
        'income_label': 'Enter annual income ($)',
        'income_help': "Customer's annual income in USD",
        'membership_years': 'Membership Years',
        'membership_label': 'Years as member',
        'membership_help': 'Number of years the customer has been a member',
        'purchase_frequency': 'Purchase Frequency',
        'frequency_label': 'Purchases per year',
        'frequency_help': 'Number of purchases made per year',
        'predict_button': 'Predict Spending Score',
        'input_summary': 'Input Summary',
        'feature_analysis': 'Feature Analysis',
        'feature': 'Feature',
        'value': 'Value',
        'years': 'years',
        'purchases_per_year': 'purchases/year',
        'analyzing': 'Analyzing customer data...',
        'prediction_results': 'Prediction Results',
        'spending_score': 'Spending Score',
        'out_of': 'out of 100',
        'customer_category': 'Customer Category',
        'above_average': 'Above Average',
        'below_average': 'Below Average',
        'quick_stats': 'Quick Stats',
        'income_level': 'Income Level',
        'high': 'High',
        'moderate': 'Moderate',
        'low': 'Low',
        'loyalty': 'Loyalty',
        'strong': 'Strong',
        'growing': 'Growing',
        'new': 'New',
        'business_recommendation': 'Business Recommendation',
        'recommended_actions': 'Recommended Actions',
        'high_value': 'High Value Customer',
        'medium_value': 'Medium Value Customer',
        'low_value': 'Low Value Customer',
        'high_value_rec': 'Target with VIP offers, exclusive deals, and personalized premium services. Consider loyalty rewards program.',
        'medium_value_rec': 'Engage with targeted promotions and upselling opportunities. Focus on increasing purchase frequency.',
        'low_value_rec': 'Focus on retention strategies, entry-level offers, and building engagement through educational content.',
        'welcome_msg': 'Please enter customer information in the sidebar and click \'Predict Spending Score\' to get started!',
        'how_it_works': 'How It Works',
        'enter_data': 'Enter Data',
        'enter_data_desc': 'Input customer demographics and behavioral data',
        'ai_analysis': 'AI Analysis',
        'ai_analysis_desc': 'Linear regression model predicts spending potential',
        'get_insights': 'Get Insights',
        'get_insights_desc': 'Receive actionable business recommendations',
        'copyright': 'All rights reserved',
        'developed_by': 'Developed by: Mishal Al-Shammari',
        'language': 'Language',
        'theme': 'Theme',
        'light_mode': 'Light Mode',
        'dark_mode': 'Dark Mode',
        'high_rec_1': 'Offer exclusive VIP membership benefits',
        'high_rec_2': 'Provide personalized shopping experiences',
        'high_rec_3': 'Early access to new products and sales',
        'high_rec_4': 'Dedicated customer support channel',
        'high_rec_5': 'Premium loyalty rewards program',
        'medium_rec_1': 'Send targeted promotional emails',
        'medium_rec_2': 'Offer bundle deals and discounts',
        'medium_rec_3': 'Implement referral program',
        'medium_rec_4': 'Create urgency with limited-time offers',
        'medium_rec_5': 'Encourage repeat purchases with rewards',
        'low_rec_1': 'Welcome discount for next purchase',
        'low_rec_2': 'Educational content about products',
        'low_rec_3': 'Engagement through social media',
        'low_rec_4': 'Simple loyalty point system',
        'low_rec_5': 'Regular newsletter with tips and deals'
    },
    'ar': {
        'title': 'متنبئ درجة إنفاق العملاء',
        'subtitle': 'توقع قيمة العملاء واحصل على رؤى عملية قابلة للتنفيذ',
        'customer_info': 'معلومات العميل',
        'age': 'العمر',
        'age_label': 'اختر عمر العميل',
        'age_help': 'عمر العميل بالسنوات',
        'annual_income': 'الدخل السنوي',
        'income_label': 'أدخل الدخل السنوي (دولار)',
        'income_help': 'الدخل السنوي للعميل بالدولار الأمريكي',
        'membership_years': 'سنوات العضوية',
        'membership_label': 'سنوات كعضو',
        'membership_help': 'عدد السنوات التي كان فيها العميل عضواً',
        'purchase_frequency': 'تكرار الشراء',
        'frequency_label': 'المشتريات في السنة',
        'frequency_help': 'عدد المشتريات التي تمت في السنة',
        'predict_button': 'توقع درجة الإنفاق',
        'input_summary': 'ملخص المدخلات',
        'feature_analysis': 'تحليل الميزات',
        'feature': 'الميزة',
        'value': 'القيمة',
        'years': 'سنوات',
        'purchases_per_year': 'مشتريات/سنة',
        'analyzing': 'جاري تحليل بيانات العميل...',
        'prediction_results': 'نتائج التوقع',
        'spending_score': 'درجة الإنفاق',
        'out_of': 'من 100',
        'customer_category': 'فئة العميل',
        'above_average': 'فوق المتوسط',
        'below_average': 'تحت المتوسط',
        'quick_stats': 'إحصائيات سريعة',
        'income_level': 'مستوى الدخل',
        'high': 'مرتفع',
        'moderate': 'متوسط',
        'low': 'منخفض',
        'loyalty': 'الولاء',
        'strong': 'قوي',
        'growing': 'متنامي',
        'new': 'جديد',
        'business_recommendation': 'التوصية التجارية',
        'recommended_actions': 'الإجراءات الموصى بها',
        'high_value': 'عميل ذو قيمة عالية',
        'medium_value': 'عميل ذو قيمة متوسطة',
        'low_value': 'عميل ذو قيمة منخفضة',
        'high_value_rec': 'استهدف بعروض VIP وصفقات حصرية وخدمات مميزة شخصية. فكر في برنامج مكافآت الولاء.',
        'medium_value_rec': 'تفاعل مع العروض الترويجية المستهدفة وفرص البيع الإضافي. ركز على زيادة تكرار الشراء.',
        'low_value_rec': 'ركز على استراتيجيات الاحتفاظ والعروض الأولية وبناء المشاركة من خلال المحتوى التعليمي.',
        'welcome_msg': 'يرجى إدخال معلومات العميل في الشريط الجانبي والنقر على \'توقع درجة الإنفاق\' للبدء!',
        'how_it_works': 'كيف يعمل',
        'enter_data': 'إدخال البيانات',
        'enter_data_desc': 'أدخل البيانات الديموغرافية والسلوكية للعميل',
        'ai_analysis': 'تحليل الذكاء الاصطناعي',
        'ai_analysis_desc': 'نموذج الانحدار الخطي يتوقع إمكانات الإنفاق',
        'get_insights': 'احصل على رؤى',
        'get_insights_desc': 'تلقى توصيات تجارية قابلة للتنفيذ',
        'copyright': 'جميع الحقوق محفوظة',
        'developed_by': 'تطوير: مشعل الشمري',
        'language': 'اللغة',
        'theme': 'المظهر',
        'light_mode': 'الوضع النهاري',
        'dark_mode': 'الوضع الليلي',
        'high_rec_1': 'تقديم مزايا عضوية VIP حصرية',
        'high_rec_2': 'توفير تجارب تسوق مخصصة',
        'high_rec_3': 'الوصول المبكر للمنتجات والتخفيضات الجديدة',
        'high_rec_4': 'قناة دعم عملاء مخصصة',
        'high_rec_5': 'برنامج مكافآت ولاء مميز',
        'medium_rec_1': 'إرسال رسائل ترويجية مستهدفة',
        'medium_rec_2': 'تقديم عروض حزم وخصومات',
        'medium_rec_3': 'تطبيق برنامج الإحالة',
        'medium_rec_4': 'خلق شعور بالإلحاح مع عروض محدودة',
        'medium_rec_5': 'تشجيع الشراء المتكرر بالمكافآت',
        'low_rec_1': 'خصم ترحيبي للشراء التالي',
        'low_rec_2': 'محتوى تعليمي عن المنتجات',
        'low_rec_3': 'التفاعل عبر وسائل التواصل الاجتماعي',
        'low_rec_4': 'نظام نقاط ولاء بسيط',
        'low_rec_5': 'نشرة إخبارية منتظمة مع نصائح وعروض'
    }
}

t = translations[st.session_state.language]

def get_inline_css():
    """Generate inline CSS with maximum contrast and proper RTL support"""
    is_dark = st.session_state.theme == 'dark'
    is_rtl = st.session_state.language == 'ar'
    
    # Color schemes optimized for maximum contrast
    if is_dark:
        # Dark mode: Deep navy/slate with bright text
        bg_primary = '#0a0f1e'
        bg_secondary = '#151b2e'
        bg_card = '#1a2238'
        text_primary = '#ffffff'
        text_secondary = '#e2e8f0'
        border_color = '#2d3748'
        accent_color = '#06b6d4'
        accent_hover = '#0891b2'
        dropdown_bg = '#1a2238'
        dropdown_text = '#ffffff'
        dropdown_hover_bg = '#2d3748'
    else:
        # Light mode: Clean whites with dark text
        bg_primary = '#f8fafc'
        bg_secondary = '#ffffff'
        bg_card = '#ffffff'
        text_primary = '#0f172a'
        text_secondary = '#475569'
        border_color = '#cbd5e1'
        accent_color = '#3b82f6'
        accent_hover = '#2563eb'
        dropdown_bg = '#ffffff'
        dropdown_text = '#0f172a'
        dropdown_hover_bg = '#f1f5f9'
    
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Inter:wght@400;500;600;700;900&display=swap');
    
    /* Global app direction and theme */
    .stApp {{
        direction: {'rtl' if is_rtl else 'ltr'} !important;
        background-color: {bg_primary} !important;
        color: {text_primary} !important;
        font-family: {'Cairo, sans-serif' if is_rtl else 'Inter, sans-serif'} !important;
    }}
    
    /* Main container */
    [data-testid="stAppViewContainer"] {{
        background-color: {bg_primary} !important;
    }}
    
    /* Sidebar with proper borders and colors */
    [data-testid="stSidebar"] {{
        background-color: {bg_secondary} !important;
        border-{'left' if is_rtl else 'right'}: 3px solid {border_color} !important;
        box-shadow: {'3px' if is_rtl else '-3px'} 0 20px rgba(0,0,0,0.15) !important;
    }}
    
    [data-testid="stSidebar"] * {{
        color: {text_primary} !important;
    }}
    
    [data-testid="stSidebar"] label {{
        color: {text_primary} !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        margin-bottom: 8px !important;
        display: block !important;
    }}
    
    /* Section dividers with gradient */
    .sidebar-divider {{
        height: 2px !important;
        background: linear-gradient(90deg, transparent, {accent_color}, transparent) !important;
        margin: 24px 0 !important;
        border: none !important;
        opacity: 0.5 !important;
    }}
    
    /* CRITICAL: Selectbox styling with maximum contrast */
    [data-baseweb="select"] {{
        background-color: {dropdown_bg} !important;
        border: 3px solid {border_color} !important;
        border-radius: 10px !important;
        min-height: 50px !important;
    }}
    
    [data-baseweb="select"] > div {{
        background-color: {dropdown_bg} !important;
        color: {dropdown_text} !important;
        font-weight: 900 !important;
        font-size: 1.15rem !important;
        padding: 12px 16px !important;
        min-height: 50px !important;
        display: flex !important;
        align-items: center !important;
    }}
    
    [data-baseweb="select"] svg {{
        fill: {dropdown_text} !important;
        width: 24px !important;
        height: 24px !important;
    }}
    
    /* Dropdown menu with perfect visibility */
    [data-baseweb="popover"] {{
        background-color: {dropdown_bg} !important;
        border: 3px solid {accent_color} !important;
        box-shadow: 0 25px 50px rgba(0, 0, 0, {'0.7' if is_dark else '0.25'}) !important;
        border-radius: 12px !important;
        margin-top: 8px !important;
    }}
    
    [role="listbox"] {{
        background-color: {dropdown_bg} !important;
        padding: 8px !important;
    }}
    
    [role="option"] {{
        background-color: {dropdown_bg} !important;
        color: {dropdown_text} !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        padding: 18px 20px !important;
        border-radius: 8px !important;
        margin: 4px 0 !important;
        border: 2px solid transparent !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
    }}
    
    [role="option"]:hover {{
        background-color: {dropdown_hover_bg} !important;
        color: {accent_color} !important;
        border-color: {accent_color} !important;
        transform: translateX({'-6px' if is_rtl else '6px'}) scale(1.02) !important;
        box-shadow: 0 4px 12px rgba({accent_color.replace('#', '')}, 0.3) !important;
    }}
    
    [aria-selected="true"] {{
        background-color: {accent_color} !important;
        color: white !important;
        border-color: {accent_hover} !important;
        font-weight: 900 !important;
    }}
    
    /* Number input with proper contrast */
    [data-testid="stNumberInput"] input {{
        background-color: {bg_card} !important;
        color: {text_primary} !important;
        border: 2px solid {border_color} !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        padding: 14px 16px !important;
        min-height: 50px !important;
    }}
    
    [data-testid="stNumberInput"] input:focus {{
        border-color: {accent_color} !important;
        box-shadow: 0 0 0 3px {accent_color}33 !important;
    }}
    
    /* Slider with RTL support */
    .stSlider {{
        padding: 15px 0 !important;
    }}
    
    .stSlider [data-baseweb="slider"] {{
        direction: ltr !important;
    }}
    
    .stSlider [role="slider"] {{
        background-color: {accent_color} !important;
        border: 4px solid {accent_hover} !important;
        width: 24px !important;
        height: 24px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2) !important;
    }}
    
    .stSlider > div > div > div {{
        background-color: {accent_color} !important;
        height: 6px !important;
    }}
    
    .stSlider > div > div > div > div {{
        background-color: {border_color} !important;
        height: 6px !important;
    }}
    
    /* Headers with proper weights */
    h1, h2, h3, h4, h5, h6 {{
        color: {text_primary} !important;
        font-family: {'Cairo, sans-serif' if is_rtl else 'Inter, sans-serif'} !important;
        font-weight: 900 !important;
        text-shadow: {'none' if is_dark else '0 1px 2px rgba(0,0,0,0.05)'} !important;
    }}
    
    p, span, div {{
        color: {text_primary} !important;
    }}
    
    /* Button with gradient */
    .stButton > button {{
        background: linear-gradient(135deg, {accent_color} 0%, {accent_hover} 100%) !important;
        color: white !important;
        border: none !important;
        padding: 20px 40px !important;
        font-size: 1.25rem !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        box-shadow: 0 10px 30px rgba({accent_color.replace('#', '')}, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        width: 100% !important;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 0 15px 40px rgba({accent_color.replace('#', '')}, 0.5) !important;
    }}
    
    /* Card containers with borders */
    .element-container {{
        color: {text_primary} !important;
    }}
    
    [data-testid="stMetricValue"] {{
        color: {text_primary} !important;
        font-size: 2rem !important;
        font-weight: 900 !important;
    }}
    
    [data-testid="stMetricLabel"] {{
        color: {text_secondary} !important;
        font-weight: 700 !important;
    }}
    
    /* Info box with proper styling */
    .stAlert {{
        background-color: {bg_card} !important;
        border: 2px solid {accent_color} !important;
        border-radius: 12px !important;
        color: {text_primary} !important;
        padding: 20px !important;
    }}
    
    /* Dataframe styling */
    [data-testid="stDataFrame"] {{
        background-color: {bg_card} !important;
        border: 2px solid {border_color} !important;
        border-radius: 12px !important;
    }}
    
    [data-testid="stDataFrame"] table {{
        background-color: {bg_card} !important;
        color: {text_primary} !important;
    }}
    
    [data-testid="stDataFrame"] thead tr th {{
        background-color: {bg_secondary} !important;
        color: {text_primary} !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        padding: 16px !important;
        border-bottom: 3px solid {accent_color} !important;
    }}
    
    [data-testid="stDataFrame"] tbody tr td {{
        color: {text_primary} !important;
        font-weight: 600 !important;
        padding: 14px !important;
        border-bottom: 1px solid {border_color} !important;
    }}
    
    /* How it works cards */
    .how-it-works-card {{
        background-color: {bg_card} !important;
        border: 2px solid {border_color} !important;
        border-radius: 16px !important;
        padding: 32px 24px !important;
        margin: 16px 8px !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(0,0,0,{'0.3' if is_dark else '0.1'}) !important;
    }}
    
    .how-it-works-card:hover {{
        transform: translateY(-8px) !important;
        border-color: {accent_color} !important;
        box-shadow: 0 12px 32px rgba(0,0,0,{'0.4' if is_dark else '0.15'}) !important;
    }}
    
    .how-it-works-card h3 {{
        color: {text_primary} !important;
        font-size: 1.4rem !important;
        font-weight: 800 !important;
        margin: 16px 0 !important;
    }}
    
    .how-it-works-card p {{
        color: {text_secondary} !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
    }}
    
    .emoji-large {{
        font-size: 3.5rem !important;
        margin-bottom: 8px !important;
    }}
    
    /* Recommendation cards */
    .recommendation-card {{
        background-color: {bg_card} !important;
        border: 3px solid {border_color} !important;
        border-radius: 16px !important;
        padding: 32px !important;
        margin: 24px 0 !important;
        box-shadow: 0 8px 24px rgba(0,0,0,{'0.3' if is_dark else '0.1'}) !important;
    }}
    
    .recommendation-card.high-value {{
        border-color: #10b981 !important;
        background: linear-gradient(135deg, {bg_card}, {'#10b98115' if is_dark else '#d1fae5'}) !important;
    }}
    
    .recommendation-card.medium-value {{
        border-color: #f59e0b !important;
        background: linear-gradient(135deg, {bg_card}, {'#f59e0b15' if is_dark else '#fef3c7'}) !important;
    }}
    
    .recommendation-card.low-value {{
        border-color: #ef4444 !important;
        background: linear-gradient(135deg, {bg_card}, {'#ef444415' if is_dark else '#fee2e2'}) !important;
    }}
    
    .recommendation-card h3 {{
        color: {text_primary} !important;
        font-size: 1.8rem !important;
        margin-bottom: 16px !important;
    }}
    
    .recommendation-card p {{
        color: {text_primary} !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
    }}
    
    .recommendation-card h4 {{
        color: {text_primary} !important;
        font-size: 1.3rem !important;
        margin: 24px 0 12px 0 !important;
    }}
    
    .recommendation-card ul {{
        margin: 12px 0 !important;
        padding-{'right' if is_rtl else 'left'}: 24px !important;
    }}
    
    .recommendation-card li {{
        color: {text_primary} !important;
        font-size: 1.05rem !important;
        line-height: 1.8 !important;
        margin: 12px 0 !important;
    }}
    
    /* Footer */
    .footer {{
        background-color: {bg_card} !important;
        border-top: 3px solid {border_color} !important;
        padding: 32px 24px !important;
        margin-top: 64px !important;
        text-align: center !important;
        border-radius: 16px 16px 0 0 !important;
    }}
    
    .footer p {{
        color: {text_primary} !important;
        font-size: 1rem !important;
        margin: 8px 0 !important;
    }}
    
    .footer strong {{
        color: {accent_color} !important;
        font-weight: 800 !important;
    }}
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {{
        [data-testid="stSidebar"] {{
            width: 100% !important;
        }}
        
        .stButton > button {{
            padding: 16px 32px !important;
            font-size: 1.1rem !important;
        }}
        
        [role="option"] {{
            padding: 16px 18px !important;
            font-size: 1rem !important;
        }}
        
        .how-it-works-card {{
            margin: 12px 0 !important;
        }}
        
        .recommendation-card {{
            padding: 24px !important;
        }}
    }}
    
    /* Smooth transitions */
    * {{
        transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease !important;
    }}
    
    /* Remove default streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """

# Apply inline CSS
st.markdown(get_inline_css(), unsafe_allow_html=True)

col_lang, col_theme = st.columns([1, 1])

with col_lang:
    lang_options = ['English', 'العربية']
    current_lang_index = 0 if st.session_state.language == 'en' else 1
    lang_option = st.selectbox(
        t['language'],
        options=lang_options,
        index=current_lang_index,
        key='lang_select'
    )
    
    new_language = 'ar' if lang_option == 'العربية' else 'en'
    if new_language != st.session_state.language:
        st.session_state.language = new_language
        st.rerun()

with col_theme:
    theme_options = [t['light_mode'], t['dark_mode']]
    current_theme_index = 0 if st.session_state.theme == 'light' else 1
    theme_option = st.selectbox(
        t['theme'],
        options=theme_options,
        index=current_theme_index,
        key='theme_select'
    )
    
    new_theme = 'dark' if theme_option == t['dark_mode'] else 'light'
    if new_theme != st.session_state.theme:
        st.session_state.theme = new_theme
        st.rerun()

# Mock Linear Regression Prediction Function
def predict_spending_score(age, income, membership_years, purchase_frequency):
    """Mock Linear Regression model for predicting spending score (0-100)"""
    age_norm = (age - 18) / (70 - 18)
    income_norm = min(income / 200000, 1.0)
    membership_norm = membership_years / 20
    frequency_norm = purchase_frequency / 100
    
    score = (
        10 + 
        (age_norm * 15) + 
        (income_norm * 35) + 
        (membership_norm * 20) + 
        (frequency_norm * 30)
    )
    
    noise = np.random.normal(0, 2)
    score = score + noise
    score = max(0, min(100, score))
    
    return round(score, 2)

def get_recommendation(score):
    """Generate business recommendation based on spending score"""
    if score >= 70:
        return {
            'category': t['high_value'],
            'recommendation': t['high_value_rec'],
            'actions': [t['high_rec_1'], t['high_rec_2'], t['high_rec_3'], t['high_rec_4'], t['high_rec_5']],
            'class': 'high-value',
            'emoji': '🎯'
        }
    elif score >= 40:
        return {
            'category': t['medium_value'],
            'recommendation': t['medium_value_rec'],
            'actions': [t['medium_rec_1'], t['medium_rec_2'], t['medium_rec_3'], t['medium_rec_4'], t['medium_rec_5']],
            'class': 'medium-value',
            'emoji': '💡'
        }
    else:
        return {
            'category': t['low_value'],
            'recommendation': t['low_value_rec'],
            'actions': [t['low_rec_1'], t['low_rec_2'], t['low_rec_3'], t['low_rec_4'], t['low_rec_5']],
            'class': 'low-value',
            'emoji': '🔍'
        }

# Header
st.markdown(f"<h1 style='text-align: center;'>💰 {t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size: 1.2rem; font-weight: 600; opacity: 0.9;'>{t['subtitle']}</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(f"### 📝 {t['customer_info']}")
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    st.markdown(f"#### 👤 {t['age']}")
    age = st.slider(
        t['age_label'],
        min_value=18,
        max_value=70,
        value=st.session_state.age,
        help=t['age_help'],
        key='age_slider'
    )
    st.session_state.age = age
    
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    st.markdown(f"#### 💵 {t['annual_income']}")
    income = st.number_input(
        t['income_label'],
        min_value=0,
        max_value=500000,
        value=st.session_state.income,
        step=5000,
        help=t['income_help'],
        key='income_input'
    )
    st.session_state.income = income
    
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    st.markdown(f"#### 🎖️ {t['membership_years']}")
    membership_years = st.slider(
        t['membership_label'],
        min_value=0,
        max_value=20,
        value=st.session_state.membership_years,
        help=t['membership_help'],
        key='membership_slider'
    )
    st.session_state.membership_years = membership_years
    
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    st.markdown(f"#### 🛒 {t['purchase_frequency']}")
    purchase_frequency = st.slider(
        t['frequency_label'],
        min_value=0,
        max_value=100,
        value=st.session_state.purchase_frequency,
        help=t['frequency_help'],
        key='frequency_slider'
    )
    st.session_state.purchase_frequency = purchase_frequency
    
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    predict_button = st.button(f"🎯 {t['predict_button']}", key='predict_btn')

if predict_button:
    st.session_state.prediction_made = True
    with st.spinner(t['analyzing']):
        import time
        time.sleep(1)
        st.session_state.score = predict_spending_score(age, income, membership_years, purchase_frequency)

if not st.session_state.prediction_made:
    st.info(f"👋 {t['welcome_msg']}")
    
    st.markdown(f"<h2 style='text-align: center; margin-top: 3rem;'>📚 {t['how_it_works']}</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="how-it-works-card">
            <div class="emoji-large">📝</div>
            <h3>{t['enter_data']}</h3>
            <p>{t['enter_data_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="how-it-works-card">
            <div class="emoji-large">🤖</div>
            <h3>{t['ai_analysis']}</h3>
            <p>{t['ai_analysis_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="how-it-works-card">
            <div class="emoji-large">💡</div>
            <h3>{t['get_insights']}</h3>
            <p>{t['get_insights_desc']}</p>
        </div>
        """, unsafe_allow_html=True)

else:
    score = st.session_state.score
    recommendation = get_recommendation(score)
    
    st.markdown(f"<h2 style='text-align: center;'>📊 {t['prediction_results']}</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display spending score with gauge chart
    gauge_bg = "#1e293b" if st.session_state.theme == 'dark' else "#f8fafc"
    text_color = "#ffffff" if st.session_state.theme == 'dark' else "#0f172a"
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': t['spending_score'], 'font': {'size': 28, 'weight': 'bold', 'color': text_color}},
        delta={'reference': 50, 'increasing': {'color': "#10b981"}},
        number={'font': {'size': 50, 'weight': 'bold', 'color': text_color}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 2, 'tickcolor': "#cbd5e1"},
            'bar': {'color': "#3b82f6" if score >= 50 else "#f59e0b"},
            'bgcolor': gauge_bg,
            'borderwidth': 3,
            'bordercolor': "#cbd5e1",
            'steps': [
                {'range': [0, 40], 'color': '#fee2e2'},
                {'range': [40, 70], 'color': '#fef3c7'},
                {'range': [70, 100], 'color': '#d1fae5'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=80, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Cairo, sans-serif' if st.session_state.language == 'ar' else 'Inter, sans-serif'}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Input summary and feature analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### 📋 {t['input_summary']}")
        summary_df = pd.DataFrame({
            t['feature']: [
                f"👤 {t['age']}",
                f"💵 {t['annual_income']}",
                f"🎖️ {t['membership_years']}",
                f"🛒 {t['purchase_frequency']}"
            ],
            t['value']: [
                f"{age} {t['years']}",
                f"${income:,}",
                f"{membership_years} {t['years']}",
                f"{purchase_frequency} {t['purchases_per_year']}"
            ]
        })
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown(f"### 📊 {t['feature_analysis']}")
        feature_contributions = {
            t['age']: 25.0,
            t['annual_income']: 32.7,
            t['membership_years']: 25.0,
            t['purchase_frequency']: 25.0
        }
        
        fig2 = go.Figure(data=[
            go.Bar(
                x=list(feature_contributions.keys()),
                y=list(feature_contributions.values()),
                marker_color=['#3b82f6', '#10b981', '#f59e0b', '#ef4444'],
                text=[f"{v}%" for v in feature_contributions.values()],
                textposition='outside',
                textfont={'size': 14, 'weight': 'bold', 'color': text_color}
            )
        ])
        
        fig2.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis={'showgrid': False, 'tickfont': {'size': 12, 'color': text_color}},
            yaxis={'showgrid': True, 'gridcolor': '#e5e7eb', 'tickfont': {'size': 12, 'color': text_color}},
            font={'family': 'Cairo, sans-serif' if st.session_state.language == 'ar' else 'Inter, sans-serif'}
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Business recommendation
    st.markdown(f"<h2 style='margin-top: 2rem;'>{recommendation['emoji']} {t['business_recommendation']}</h2>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="recommendation-card {recommendation['class']}">
        <h3>{recommendation['category']}</h3>
        <p style="font-size: 1.1rem; margin: 1rem 0;">{recommendation['recommendation']}</p>
        <h4>{t['recommended_actions']}</h4>
        <ul style="margin-top: 1rem;">
            {''.join([f'<li style="margin: 0.5rem 0;">{action}</li>' for action in recommendation['actions']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats
    st.markdown(f"### ⚡ {t['quick_stats']}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        income_level = t['high'] if income >= 75000 else t['moderate'] if income >= 40000 else t['low']
        st.metric(label=f"💰 {t['income_level']}", value=income_level)
    
    with col2:
        category = t['above_average'] if score >= 50 else t['below_average']
        st.metric(label=f"📈 {t['customer_category']}", value=category)
    
    with col3:
        loyalty_level = t['strong'] if membership_years >= 10 else t['growing'] if membership_years >= 3 else t['new']
        st.metric(label=f"🎯 {t['loyalty']}", value=loyalty_level)

# Footer
st.markdown(f"""
<div class="footer">
    <p style="font-size: 1.1rem;"><strong>⚡ Streamlit</strong> | <strong>🤖 Linear Regression</strong> | <strong>📊 Data Science</strong></p>
    <p style="margin-top: 1.5rem; font-size: 1.05rem; font-weight: 700;">{t['developed_by']}</p>
    <p style="margin-top: 0.5rem; font-size: 0.95rem;">© 2025 {t['developed_by'].split(': ')[1]} | {t['copyright']}</p>
</div>
""", unsafe_allow_html=True)
