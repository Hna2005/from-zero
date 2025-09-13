import nltk

def download_words():
    """
    Ensure that the NLTK 'words' corpus is available.

    Checks if the 'words' corpus is already downloaded; if not, downloads it.
    Prints status messages to inform the user.
    """
    try:
        nltk.data.find("corpora/words.zip")
        print("NLTK 'words' corpus already available.")
    except LookupError:
        print("Downloading NLTK 'words' corpus...")
        nltk.download("words")
        print("Download finished.")


if __name__ == "__main__":
    download_words()
