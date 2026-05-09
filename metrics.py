from nltk.translate.bleu_score import sentence_bleu

reference = [["turn", "your", "head"]]
candidate = ["turn", "your", "head"]

score = sentence_bleu(reference, candidate)

print("BLEU Score:", score)
