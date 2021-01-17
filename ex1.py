import streamlit as st 
import sumy 
import nltk
import nltk; nltk.download('punkt')

# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


# Function for Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

def main():
	""" NLP Based App with Streamlit """

	# Title
	st.title("The WizKid App")
	st.subheader("This App Helps with Assignments and Report Writing")
	st.markdown("""
    	#### How to use 
         1. Highlight the text you want to summarize and copy
        (Be sure to select a lengthy Text of a single Prefered Topic)

         2. Paste into the space provided 

         3. Click Summarize
    	""")
	# Summarization
	if st.subheader("Summarize Your Text"):
		message = st.text_area("Enter Text")
	if st.button("Summarize"):
			summary_result = sumy_summarizer(message)
			st.success(summary_result)


	st.sidebar.subheader("About App")
	st.sidebar.text("Built by Olutayo Solana")
	st.sidebar.info("This is a prototype/proof of concept for the commercial viabilty of a product in this one's likeness")
	


if __name__ == '__main__':
	main()
