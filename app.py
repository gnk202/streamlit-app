import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="현대자동차 인프라시스템",
    page_icon="🏢",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body {
        margin: 0;
        background: #f6f7f9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans KR", sans-serif;
    }

    .page {
        min-height: 100vh;
        padding: 24px 40px;
        box-sizing: border-box;
        position: relative;
        overflow: hidden;
    }

    .header-wrap {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .brand-wrap {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .brand-icon {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: linear-gradient(135deg, #13b5d1, #0b3b78);
        color: white;
        font-size: 22px;
        font-weight: 800;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .brand-text {
        font-size: 28px;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.5px;
    }

    .nav-wrap {
        display: flex;
        align-items: center;
        gap: 28px;
    }

    .nav-item {
        text-decoration: none;
        color: #1f2937;
        font-size: 18px;
        font-weight: 500;
    }

    .contact-btn {
        text-decoration: none;
        background: #0a3b78;
        color: white;
        padding: 14px 24px;
        border-radius: 999px;
        font-size: 17px;
        font-weight: 700;
    }

    .hero {
        min-height: calc(100vh - 90px);
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        position: relative;
    }

    .circle-left {
        position: absolute;
        left: 40px;
        top: 180px;
        width: 430px;
        height: 430px;
        border-radius: 50%;
        border: 1px solid rgba(15, 23, 42, 0.05);
    }

    .circle-right {
        position: absolute;
        right: 80px;
        bottom: 30px;
        width: 300px;
        height: 300px;
        border-radius: 50%;
        border: 1px solid rgba(15, 23, 42, 0.05);
    }

    .hero-content {
        position: relative;
        z-index: 2;
        margin-top: -40px;
    }

    .badge {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 10px 18px;
        border-radius: 999px;
        border: 1px solid #e5e7eb;
        background: #f8fafc;
        color: #64748b;
        font-size: 16px;
        font-weight: 500;
        margin-bottom: 28px;
    }

    .badge-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #34d399;
    }

    .hero-title {
        font-size: 76px;
        line-height: 1.08;
        font-weight: 850;
        color: #0f172a;
        letter-spacing: -2px;
        margin-bottom: 24px;
    }

    .blue {
        color: #0a3b78;
    }

    .hero-desc {
        font-size: 24px;
        line-height: 1.8;
        color: #7b8794;
        margin-bottom: 42px;
        font-weight: 500;
    }

    .btn-row {
        display: flex;
        justify-content: center;
        gap: 18px;
        flex-wrap: wrap;
    }

    .primary-btn {
        text-decoration: none;
        background: #0a3b78;
        color: white;
        padding: 18px 34px;
        border-radius: 999px;
        font-size: 20px;
        font-weight: 700;
        display: inline-block;
    }

    .secondary-btn {
        text-decoration: none;
        background: white;
        color: #111827;
        border: 1px solid #cbd5e1;
        padding: 18px 34px;
        border-radius: 999px;
        font-size: 20px;
        font-weight: 700;
        display: inline-block;
    }
</style>
</head>
<body>
    <div class="page">
        <div class="header-wrap">
            <div class="brand-wrap">
                <div class="brand-icon">H</div>
                <div class="brand-text">현대자동차 인프라시스템</div>
            </div>

            <div class="nav-wrap">
                <a class="nav-item" href="#">서비스</a>
                <a class="nav-item" href="#">소개</a>
                <a class="nav-item" href="#">연락처</a>
                <a class="contact-btn" href="#">문의하기</a>
            </div>
        </div>

        <div class="hero">
            <div class="circle-left"></div>
            <div class="circle-right"></div>

            <div class="hero-content">
                <div class="badge">
                    <span class="badge-dot"></span>
                    연구개발인프라지원시스템 운영 중
                </div>

                <div class="hero-title">
                    시설의 안전을,<br>
                    <span class="blue">시스템</span>으로 완성하다.
                </div>

                <div class="hero-desc">
                    공사 안전관리부터 자동 문서화까지,<br>
                    현대자동차 인프라건설의 모든 프로세스를 하나로.
                </div>

                <div class="btn-row">
                    <a class="primary-btn" href="#">서비스 살펴보기 →</a>
                    <a class="secondary-btn" href="#">담당자 연결</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)