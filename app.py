import streamlit as st
from sentiment import SentimentAnalyzer
from PIL import Image


def analyze_game(name: str, image_path: str, analyzer: SentimentAnalyzer):
    st.header(name)
    st.image(
        [
            Image.open(image_path),
        ],
        width=500,
    )

    review: str = st.text_input(f"Describe your experience playing **{name}**")

    if review:
        sentiment: str = analyzer.analyze(review)
        st.write(f"Overall Feeling: {sentiment}")


def main():
    st.title("Game of The Year 2023")
    st.header("Review The Game of The Year 2023! 🕹️")

    placeholder = st.empty()
    placeholder.text("Loading...")
    sentiment_analyzer = SentimentAnalyzer()
    placeholder.empty()

    # Alan Wake
    alan_wake: str = "Alan Wake 2"
    alan_wake_img: str = "images/alan_wake.png"

    analyze_game(alan_wake, alan_wake_img, sentiment_analyzer)

    # Baldurs Gate 3
    baldur_gate: str = "Baldur's Gate 3"
    baldur_gate_img: str = "images/baldur_gate.png"

    analyze_game(baldur_gate, baldur_gate_img, sentiment_analyzer)

    # The Legend Of Zelda
    zelda: str = "The Legend of Zelda: Tears of the Kingdom"
    zelda_img: str = "images/zelda.png"

    analyze_game(zelda, zelda_img, sentiment_analyzer)

    # Spider Man 2
    spider_man: str = "Marvel's Spider-Man 2"
    spider_man_img: str = "images/spider.jpeg"

    analyze_game(spider_man, spider_man_img, sentiment_analyzer)

    # Super Mario Bros. Wonder
    mario: str = "Super Mario Bros. Wonder"
    mario_img: str = "images/mario.jpeg"

    analyze_game(mario, mario_img, sentiment_analyzer)


if __name__ == "__main__":
    main()
