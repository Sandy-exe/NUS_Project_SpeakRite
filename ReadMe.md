# Ideas

## Whisper Model

Whisper is a Transformer-based encoder-decoder model used for ASR (Automatic Speech Recognition). It converts sequences from one domain (like speech audio) into sequences in another domain (like text). The WhisperProcessor pre-processes the audio inputs and post-processes the model outputs.

Whisper is an end-to-end speech recognition model developed by OpenAI, using an encoder-decoder Transformer architecture. It processes audio in 30-second chunks, converting them into log-Mel spectrograms for the encoder, and the decoder predicts the corresponding text. Unlike models trained on specific datasets, Whisper was trained on a large, diverse dataset, making it more robust across various datasets, even though it may not outperform specialized models on specific benchmarks. Notably, Whisper is effective at learning speech-to-text translation, especially for non-English languages, and outperforms the state-of-the-art on the CoVoST2 to English translation task in a zero-shot setting.

## HuBERT

HuBERT operates by using an offline k-means clustering step to learn the structure of spoken input. It predicts the correct cluster for masked audio segments, effectively learning the underlying patterns in the speech data.

**Problem:** HuBERT relies on k-means clustering to generate pseudo-labels for pre-training, and poor clustering quality can lead to inaccurate labels.

**Impact:** This can hinder model performance, especially when dealing with accented datasets.

**Potential Solution:** Potential solutions include improving the clustering algorithm or using more diverse training data.

## Wav2Vec

Wav2Vec, developed by Facebook AI for Automatic Speech Recognition (ASR), is trained in two phases: self-supervised learning and supervised fine-tuning. The model learns to understand and represent speech audio, similar to how word embeddings represent text. It does this by processing unlabeled audio data. The key advantage of Wav2Vec 2.0 is its ability to learn good speech representations from a large amount of unlabeled data. This allows it to achieve state-of-the-art results even with a small amount of labeled data. It uses Word Error Rate (WER) to measure the performance of ASR models.

**Problem:** Training Wav2Vec models is computationally intensive, necessitating high-performance hardware and considerable training duration.

**Impact:** This could restrict the model's accessibility to individuals or organizations with limited resources.

**Potential Solution:** Possible solutions could involve the use of cloud-based computing resources or optimizing the model to improve efficiency.

## Datasets

1. [AI4Bharat/Svarah](https://github.com/AI4Bharat/Svarah)
2. [Mozilla Common Voice](https://commonvoice.mozilla.org/en/datasets)

## Code Explanation

1. The `speech2txt.ipynb` has the code for training and loading the trained model from my own drive.
2. `SpeakRite.ipynb` has the code for the project we did in NUS (My Contribution is on ASR models).
3. The trained model is available at my HuggingFace Model link: [Santhosh-kumar/ASR](https://huggingface.co/Santhosh-kumar/ASR)