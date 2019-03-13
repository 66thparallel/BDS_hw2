/*  
 * Author: Jane Liu and Meng Li
 * Homework 2
 * Date of last modification: 11 March 2019
*/

import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class hw2 {

	public static void main(String[] args) throws IOException {
        // TODO code application logic here

        String token = new String();

        Scanner inFile1 = new Scanner(new File("src/C1/article01.txt")).useDelimiter("[.,:;()?!\"\\s]+");
        Scanner inFile2 = new Scanner(new File("src/stopwords.txt")).useDelimiter("[.,:;()?!\"\\s]+");

        List<String> article = new ArrayList<String>();
        List<String> stopwords = new ArrayList<String>();

        while (inFile1.hasNext()) {
            token = inFile1.next();
            article.add(token);
        }

        while (inFile2.hasNext()) {
            token = inFile2.next();
            stopwords.add(token);
        }

        inFile1.close();
        inFile2.close();
		
		// Removes all stop words from the array containing the text file
		article.removeAll(stopwords);		

		// Test to see if stopwords have been removed
		// System.out.println(article);

  }
}

// lemmatization class
public class StanfordLemmatizer {

    protected StanfordCoreNLP pipeline;

    public StanfordLemmatizer() {
        // Create StanfordCoreNLP object properties, with POS tagging
        // (required for lemmatization), and lemmatization
        Properties props;
        props = new Properties();
        props.put("annotators", "tokenize, ssplit, pos, lemma");

        // StanfordCoreNLP loads a lot of models, so you probably
        // only want to do this once per execution
        this.pipeline = new StanfordCoreNLP(props);
    }

    public List<String> lemmatize(String documentText)
    {
        List<String> lemmas = new LinkedList<String>();

        // create an empty Annotation just with the given text
        Annotation document = new Annotation(documentText);

        // run all Annotators on this text
        this.pipeline.annotate(document);

        // Iterate over all of the sentences found
        List<CoreMap> sentences = document.get(SentencesAnnotation.class);
        for(CoreMap sentence: sentences) {
        // Iterate over all tokens in a sentence
            for (CoreLabel token: sentence.get(TokensAnnotation.class)) {
                // Retrieve and add the lemma for each word into the list of lemmas
                lemmas.add(token.get(LemmaAnnotation.class));
            }
        }

        return lemmas;
    }
}

