# 💰 Customer Spending Score Predictor

A modern, bilingual (English/Arabic), mobile-responsive web application built with Streamlit to predict customer spending scores using Linear Regression.

## 🌟 Features

- **🌐 Bilingual Support**: Full English and Arabic language support with RTL layout
- **🎨 Dark/Light Mode**: Toggle between themes with optimized high-contrast color schemes
- **💾 Data Persistence**: Session state maintains inputs when switching languages/themes
- **Modern UI/UX**: Clean, professional interface with WCAG AA compliant contrast
- **Interactive Inputs**: Sidebar with sliders and number inputs for easy data entry
- **Real-time Prediction**: Instant spending score calculation (0-100 scale)
- **Visual Analytics**: 
  - Gauge chart showing spending score with color zones
  - Feature analysis bar chart with percentage contributions
  - Color-coded recommendation cards with gradient backgrounds
- **Business Intelligence**: Actionable recommendations with specific action items
- **Mobile Responsive**: Optimized for all device sizes (mobile, tablet, desktop)
- **RTL Slider Support**: Proper slider behavior in Arabic mode
- **Accessibility**: Maximum contrast ratios for perfect readability in both themes

## 🚀 Installation & Usage

### Prerequisites
- Python 3.8 or higher

### Setup

1. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. Run the application:
\`\`\`bash
streamlit run app.py
\`\`\`

3. Open your browser and navigate to `http://localhost:8501`

## 📊 Input Features

- **Age**: Customer age (18-70 years)
- **Annual Income**: Yearly income in USD
- **Membership Years**: Duration of membership (0-20 years)
- **Purchase Frequency**: Number of purchases per year (0-100)

## 🎯 Output

- **Spending Score**: 0-100 scale prediction with visual gauge
- **Customer Category**: High/Medium/Low value classification
- **Customer Segment**: 
  - **High Value (70-100)**: VIP treatment, exclusive offers
  - **Medium Value (40-69)**: Targeted promotions, upselling
  - **Low Value (0-39)**: Retention strategies, engagement
- **Business Recommendations**: 5 specific action items per segment
- **Quick Stats**: Income level, loyalty status, and category indicators

## 🧮 Model Logic

The application uses a mock Linear Regression model with positive correlations:
- Income: 35% weight
- Purchase Frequency: 30% weight
- Membership Years: 20% weight
- Age: 15% weight
- Base score: 10 points

## 🌍 Language Support

- **English**: Left-to-right (LTR) layout
- **العربية (Arabic)**: Right-to-left (RTL) layout with Cairo font

## 🎨 Theme Options

- **Light Mode**: Clean white backgrounds (#ffffff) with dark text (#0f172a) and blue accents (#3b82f6)
- **Dark Mode**: Deep navy backgrounds (#0a0f1e) with bright white text (#ffffff) and cyan accents (#06b6d4)

Both themes optimized for maximum contrast and readability with:
- Bold font weights (800-900) for all labels and options
- Large font sizes (1.1rem+) for dropdown menus
- Proper hover states with smooth transitions
- Visual feedback on all interactive elements

## 🆕 Latest Updates

- **Perfect Dropdown Contrast**: Maximum visibility for all dropdown menus in both themes
- **Session State Persistence**: Data remains when switching languages or themes
- **Enhanced Visual Separators**: Gradient dividers between all sidebar sections
- **Improved RTL Support**: Sliders maintain proper tracking in Arabic mode
- **Optimized Colors**: New color schemes for both light and dark modes
- **Enhanced Mobile Support**: Better touch targets and responsive layouts
- **Local Storage Support**: Added streamlit-cookies-manager for data retention

## 🛠️ Tech Stack

- **Streamlit**: Web framework
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical computations
- **Pandas**: Data handling
- **scikit-learn**: ML model foundation
- **streamlit-extras**: Enhanced UI components
- **streamlit-cookies-manager**: Local storage support
- **hydralit-components**: Advanced UI elements

## 📁 Project Structure

\`\`\`
customer-spending-predictor/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
├── DEPLOYMENT.md         # Deployment guide
├── assets/
│   └── style.css         # External CSS styles
└── .streamlit/
    └── config.toml       # Streamlit configuration
\`\`\`

## 🎯 How to Use

1. **Select Language**: Choose English or العربية from the dropdown (data persists when switching)
2. **Choose Theme**: Toggle between Light Mode or Dark Mode (predictions remain visible)
3. **Enter Customer Data** in the sidebar:
   - Adjust age slider (18-70 years)
   - Enter annual income (with proper formatting)
   - Set membership years (0-20 years)
   - Configure purchase frequency (0-100 purchases/year)
4. **Click "Predict Spending Score"** button
5. **Review Results**:
   - Analyze the spending score gauge (0-100)
   - Review feature contributions chart
   - Read color-coded business recommendations
   - Check quick statistics (income level, loyalty, category)

## 📝 Notes

This is a demonstration application using a mock linear regression model. For production use, replace the `predict_spending_score()` function with a trained scikit-learn model loaded from a pickle file.

## 🔮 Future Enhancements

- Upload trained model file (.pkl)
- Historical data visualization
- Batch prediction capability
- Export results to PDF/CSV
- A/B testing recommendations
- Database integration for customer history
- Advanced analytics dashboard
- Multi-user authentication

## 👨‍💻 Developer

**Developed by: Mishal Al-Shammari**  
**تطوير: مشعل الشمري**

## 📄 License

© 2025 All rights reserved | جميع الحقوق محفوظة

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by Linear Regression
- Charts by [Plotly](https://plotly.com/)
- Typography: Inter & Cairo fonts

---

**Built with ❤️ using Streamlit**
