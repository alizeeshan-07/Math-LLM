import streamlit as st
from langchain import OpenAI, LLMMathChain

llm = OpenAI(openai_api_key="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", temperature=0)
llm_math = LLMMathChain.from_llm(llm, verbose=True)


st.set_page_config(page_title="Math with LLMs", page_icon="	:triangular_ruler:")
def main():
    st.title("Math Query")
    query = st.text_input("Enter your math query")
    if st.button("Calculate"):
        result = llm_math.run(query)
        st.write("Result:", result)

if __name__ == "__main__":
    main()