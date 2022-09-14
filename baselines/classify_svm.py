#! /usr/bin/env python3

import json, os
import sklearn.svm, sklearn.feature_extraction.text, sklearn.utils, sklearn.linear_model

# the path to the folder where the wikipedia dumps are extracted, i.e. the folder containing eml_texts, fur_texts etc.
DATAPATH="../../itdi/experiment/"
# the path to the folder where the dev and test sets are located
TESTPATH="../task"

def load_all_training_data():
	varieties = sorted([x.replace("_texts", "") for x in os.listdir(DATAPATH) if x.endswith("_texts")])
	print("  Considered varieties: " + ", ".join(varieties))
	all_x, all_y = [], []
	for id in varieties:
		x = load_training_data(id)
		y = [id.upper() for _ in x]
		all_x.extend(x)
		all_y.extend(y)
	print(f"  {len(all_x)} instances in total with {len(all_y)} labels")
	return all_x, all_y

def load_training_data(id):
	instances = set()
	filename = f"{DATAPATH}/{id}_texts/AA/wiki_00"
	f = open(filename, 'r', encoding='utf-8')
	for line in f:
		data = json.loads(line)
		text = data["text"]
		if text.strip() == "":
			continue
		textlines = [x.strip() for x in text.split("\n") if x.strip() != ""]
		instances.update(textlines)
	print(f"  - {len(instances)} training instances extracted for {id}")
	return list(instances)

def load(id):
	if id == "dev":
		filename = f"{TESTPATH}/dev.txt"
	elif id == "test":
		filename = f"{TESTPATH}/test_gold_standard.txt"
	x, y = [], []
	for line in open(filename, 'r', encoding='utf-8'):
		x.append(line.split("\t")[1].strip())
		y.append(line.split("\t")[0].strip())
	print(f"  {len(x)} {id} instances loaded")
	return x, y

def save_results(prediction, filename):
	f = open(filename, 'w')
	for p in prediction:
		f.write(p + "\n")
	f.close()

def classify(train_x, train_y, dev_x, test_x, cl_type, vec_type, ngrams=(1,1), maxiter=500):
	if vec_type == "tfidf":
		vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(analyzer='char', ngram_range=ngrams, min_df=10)
	elif vec_type == "count":
		vectorizer = sklearn.feature_extraction.text.CountVectorizer(analyzer='char', ngram_range=ngrams, min_df=10)
	else:
		raise NotImplementedError(f"  Unknown vectorizer {vec_type}")
	
	if cl_type == "svm":
		cl = sklearn.svm.LinearSVC(max_iter=maxiter, verbose=True)
	elif cl_type == "logreg":
		cl = sklearn.linear_model.LogisticRegression(penalty='l2', multi_class='multinomial', solver='lbfgs', max_iter=maxiter, verbose=True)
	else:
		raise NotImplementedError(f"  Unknown classifier {cl_type}")

	print("    Training")
	train_x_grams = vectorizer.fit_transform(train_x)
	cl.fit(train_x_grams, train_y)
	#print(cl)

	print("    Predicting dev set")
	dev_x_grams = vectorizer.transform(dev_x)
	dev_pred = cl.predict(dev_x_grams)

	print("    Predicting test set")
	test_x_grams = vectorizer.transform(test_x)
	test_pred = cl.predict(test_x_grams)
	return dev_pred, test_pred

def evaluate(s, prediction, gold):
	total = 0
	correct = 0
	for p_example, g_example in zip(prediction, gold):
		total += 1
		correct += int(p_example == g_example)
	print("    {}:  {} examples, {} correct, {:.2f}% accuracy".format(s, total, correct, 100*correct/total))


if __name__ == "__main__":
	print("Load data")
	train_x, train_y = load_all_training_data()
	train_x_s, train_y_s = sklearn.utils.shuffle(train_x, train_y)
	dev_x, dev_y = load('dev')
	test_x, test_y = load('test')
	print()

	vectorizer = "tfidf"
	classifier = "svm"
	maxiter = 500

	# UNIGRAMS
	ngrams = (1,1)
	print("  Train unigram classifier")
	dev_y_pred, test_y_pred = classify(train_x_s, train_y_s, dev_x, test_x, classifier, vectorizer, ngrams, maxiter)
	evaluate("Dev set", dev_y_pred, dev_y)
	save_results(dev_y_pred, f'result_baseline2_dev.txt')
	evaluate("Test set", test_y_pred, test_y)
	save_results(test_y_pred, f'result_baseline2_test.txt')

	# 1-4-GRAMS
	ngrams = (1,4)
	print("  Train 1-4-grams classifier")
	dev_y_pred, test_y_pred = classify(train_x_s, train_y_s, dev_x, test_x, classifier, vectorizer, ngrams, maxiter)
	evaluate("Dev set", dev_y_pred, dev_y)
	save_results(dev_y_pred, f'result_baseline3_dev.txt')
	evaluate("Test set", test_y_pred, test_y)
	save_results(test_y_pred, f'result_baseline3_test.txt')
	
# Accuracies:            DEV     TEST
# svm/tfidf/1-grams      70.82%  46.58%  (converged)
# svm/tfidf/1-4-grams    89.41%  75.20%  (converged)
