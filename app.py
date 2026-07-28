import numpy as np
import streamlit as st
from PIL import Image

from recomendation.recipe_api import getrecipe
from model.predict import predict_freshness


st.set_page_config(
    page_title="Food Freshness Detector",
    page_icon="🥗",
    layout="centered"
)

#########################------header-------#################################
#############################################################################

st.title("Food Freshness Detector")

st.caption(
    "Upload or capture a photo of any fruit, vegetable or frozen item to identify its freshness and get suggestions to ensure its safety."
)

########################--------sidebar------------------###############################

st.sidebar.header("Food Information")

foodtype = st.sidebar.text_input(
    "Food name",
    placeholder="e.g. Tomato, Banana, Apple",
    help="Used to provide recipe recommendations once the freshness is confirmed."
)

confidencethreshold = st.sidebar.slider(
    "Confidence Threshold",
    0.50,
    1.00,
    0.70,
    0.05
)

########################--------Image Input------------------###############################

uploadedfile = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)


image = None

if uploadedfile is not None:
    image = Image.open(uploadedfile).convert("RGB")


########################--------Prediction------------------###############################

if image is not None:

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    imageary = np.array(image)

    with st.spinner("Predicting image..."):
        label, confidence, prediction = predict_freshness(imageary)

    st.divider()

    st.subheader("Prediction")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Freshness", label)

    with col2:
        st.metric("Confidence", f"{confidence * 100:.2f}%")

    st.progress(float(confidence))

    ########################--------Confidence Check------------------###############################

    if confidence < confidencethreshold:
        st.warning(
            "Prediction confidence is very low.\n\n"
            "Please upload another image with:\n"
            "- Better lighting\n"
            "- Clear focus\n"
            "- Food centered in the image"
        )
        st.stop()

    ########################--------Freshness Result------------------###############################

    if label == "Fresh":
        st.success("✅ Food is Fresh.")

    elif label == "Medium":
        st.warning("⚠️ Food is moderately fresh. Consume it soon.")

    else:
        st.error("❌ Food appears to be rotten. Not recommended for consumption.")

    ########################--------Recipe Recommendation------------------###############################

    if label != "Rotten":

        if foodtype.strip() == "":

            st.info(
                "Enter the food name in the sidebar to receive recipe recommendations."
            )

        else:

            st.divider()

            st.subheader("🍽 Recommended Recipes")

            try:
                with st.spinner("Finding recipes..."):
                    recipes = getrecipe(foodtype)
            except RuntimeError as e:
                recipes = []
                st.error(
                    "Recipe search isn't configured yet: "
                    f"{e}\n\n"
                    "Get a free key at https://spoonacular.com/food-api "
                    "and set it as the SPOONACULAR_API_KEY environment variable."
                )

            if recipes:

                for recipe in recipes:

                    st.markdown(f"### {recipe.get('title', 'Untitled recipe')}")

                    if recipe.get("image"):
                        st.image(recipe["image"], width=250)

                    if "usedIngredientCount" in recipe:
                        st.write(
                            f"Ingredients Used: {recipe['usedIngredientCount']}"
                        )

                    st.write("---")

            elif foodtype.strip() != "" and not recipes:
                st.info("No recipes found. Try a different food name.")

else:
    st.info("📤 Upload or capture an image to begin.")
