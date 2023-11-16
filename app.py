import streamlit as st
from sentiment import SentimentAnalyzer
from PIL import Image


def main():
    st.title("Game of The Year 2023")
    st.header("Review The Game of The Year 2023! 🕹️")
    st.subheader("By Gustavo de Oliveira & Lucas Ciziks")

    placeholder = st.empty()
    placeholder.text("Loading...")
    sentiment_analyzer = SentimentAnalyzer()
    placeholder.empty()

    # Alan Wake
    st.header("Alan Wake 2")
    st.image(
        [
            Image.open("images/alan_wake.png"),
        ],
        width=500,
    )

    alan_wake_review: str = st.text_input(
        "Describe your experience playing **Alan Wake 2**"
    )

    if alan_wake_review:
        alan_wake_sentiment: str = sentiment_analyzer.analyze(alan_wake_review)
        st.write(f"Overall Feeling: {alan_wake_sentiment}")

    # Baldurs Gate 3
    st.header("Baldur's Gate 3")
    st.image(
        [
            Image.open("images/baldur_gate.png"),
        ],
        width=400,
    )

    baldur_review: str = st.text_input(
        "Describe your experience playing **Baldur's Gate 3**"
    )

    if baldur_review:
        baldur_sentiment: str = sentiment_analyzer.analyze(baldur_review)
        st.write(f"Overall Feeling: {baldur_sentiment}")

    # Zelda
    st.header("The Legend of Zelda: Tears of the Kingdom")
    st.image(
        [
            Image.open("images/zelda.png"),
        ],
        width=400,
    )

    zelda_review: str = st.text_input(
        "Describe your experience playing **The Legend of Zelda: Tears of the Kingdom**"
    )

    if zelda_review:
        zelda_sentiment: str = sentiment_analyzer.analyze(zelda_review)
        st.write(f"Overall Feeling: {zelda_sentiment}")


if __name__ == "__main__":
    main()
