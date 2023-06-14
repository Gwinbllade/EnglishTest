#include <iostream>
#include <fstream>
#include <string>
#include <random>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

class Question {
private:
    string ukrWord;
    string engWord1;
    string engWord2;
    string engWord3;
    int correctAnswer;

public:
    Question(string ukrWord, string engWord1, string engWord2, string engWord3, int correctAnswer) {
        this->ukrWord = ukrWord;
        this->engWord1 = engWord1;
        this->engWord2 = engWord2;
        this->engWord3 = engWord3;
        this->correctAnswer = correctAnswer;
    }

    string getFormattedString() const {
        string formattedString = ukrWord + " " + engWord1 + " " + engWord2 + " " + engWord3 + " " + to_string(correctAnswer);
        return formattedString;
    }
};

class Word {
private:
    string ukrWord;
    string engWord;

public:
    Word() {
        ukrWord = "";
        engWord = "";
    }

    Word(string u, string e) {
        this->ukrWord = u;
        this->engWord = e;
    }

    string getEngWord() const {
        return this->engWord;
    }

    string getUkrWord() const {
        return this->ukrWord;
    }
};

class WordTranslationQuiz {
private:
    string fileName;
    vector<Question> questions;
    vector<Word> words;
    int questionCount;

public:
    WordTranslationQuiz(string fileName, int questionCount) {
        this->fileName = fileName;
        this->questionCount = questionCount;
    }

    void ReadFile() {
        ifstream file(this->fileName);

        if (file.is_open()) {
            vector<string> lines;
            string line;
            string text1;
            string text2;
            string delimiter = " - ";

            // Read all lines from the file
            while (getline(file, line)) {
                // Divide the line into two words
                size_t delimiterPos = line.find(delimiter);
                if (delimiterPos != string::npos) {
                    // Get the first part of the line before the delimiter
                    text1 = line.substr(0, delimiterPos);
                    // Get the second part of the line after the delimiter
                    text2 = line.substr(delimiterPos + delimiter.length());
                }

                Word w = Word(text1, text2);
                this->words.push_back(w);
            }

            file.close();

            // Shuffle the words randomly
            random_device rd;
            mt19937 gen(rd());
            shuffle(this->words.begin(), this->words.end(), gen);

            this->words.resize(this->questionCount);
        }
        else {
            cout << "Error: Unable to open the file." << endl;
        }
    }

    void GenerateQuestions() {
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<int> distr(0, 2);

        ofstream outputFile("D:\\osnov.prog\\Lab10\\Ansver.txt");
        if (!outputFile.is_open()) {
            cout << "Error: Unable to open the output file." << endl;
            return;
        }

        for (const Word& word : this->words) {
            vector<string> shuffledWords(3);

            // Generate unique options
            set<string> uniqueWords;
            uniqueWords.insert(word.getEngWord());  // Add the correct word to uniqueWords
            while (uniqueWords.size() < 3) {
                string randomWord = this->words[gen() % this->words.size()].getEngWord();
                uniqueWords.insert(randomWord);
            }

            // Shuffle all words
            copy(uniqueWords.begin(), uniqueWords.end(), shuffledWords.begin());
            shuffle(shuffledWords.begin(), shuffledWords.end(), gen);

            // Find the index of the correct word
            int correctIndex = 0;
            for (int i = 0; i < 3; i++) {
                if (shuffledWords[i] == word.getEngWord()) {
                    correctIndex = i;
                    break;
                }
            }

            // Swap the correct word with the last word
            swap(shuffledWords[correctIndex], shuffledWords[2]);

            outputFile << word.getUkrWord() << " " << shuffledWords[0] << " " << shuffledWords[1] << " " << shuffledWords[2] << " " << endl;
        }

        outputFile.close();
    }


};

int main() {
    system("chcp 1251");
    string filePath = "D:\\osnov.prog\\Lab10\\Test.txt";
    int questionCount = 3;
    WordTranslationQuiz quiz(filePath, questionCount);
    quiz.ReadFile();
    quiz.GenerateQuestions();

    return 0;
}
