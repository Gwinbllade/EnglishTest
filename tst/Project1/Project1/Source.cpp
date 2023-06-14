#include <iostream>
#include <fstream>
#include <string>
#include <random>
#include <vector>


using namespace std;


class Question {
private:
    string ukrWord;
    string engWord1;
    string engWord2;
    string engWord3;
    int corectAnswer;


public:
    Question(string ukrWord, string engWord1, string engWord2, string engWord3, int corectAnswer) {
        this->ukrWord = ukrWord;
        this->engWord1 = engWord1;
        this->engWord2 = engWord2;
        this->engWord3 = engWord3;
        this->corectAnswer = corectAnswer;
    }

    string getFormattedString() const {
        string formattedString = ukrWord + " " + engWord1 + " " + engWord2 + " " + engWord3 + " " + to_string(corectAnswer);
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


    string getEngWord() {
        return this->engWord;
    }

    string getUkrWord() {
        return this->ukrWord;
    }
};


class WordTranslationQuiz {
private:
    string fileName;
    vector<Question> questions;
    vector<Word> words;
    int coutQuestion;


public:
    WordTranslationQuiz(string fileName, int coutQuestion) {
        this->fileName = fileName;
        this->coutQuestion = coutQuestion;
    }


    void ReadFile() {
        ifstream file(this->fileName);

        if (file.is_open()) {
            vector<string> lines;
            string line;
            string text1;
            string text2;
            string delimiter = " - ";

            // Зчитуємо всі рядки з файлу
            while (getline(file, line)) {


                // Ділимо рядок на два слова
                size_t delimiterPos = line.find(delimiter);
                if (delimiterPos != string::npos) {
                    // Отримуємо перший рядок до розділювача
                    text1 = line.substr(0, delimiterPos);
                    // Отримуємо другий рядок після розділювача
                    text2 = line.substr(delimiterPos + delimiter.length());
                }

                Word w = Word(text1, text2);

                this->words.push_back(w);
            }

            file.close();

            // Перемішуємо рядки випадковим чином
            random_device rd;
            mt19937 gen(rd());
            shuffle(this->words.begin(), this->words.end(), gen);

            this->words.resize(this->coutQuestion);
        }
        else {
            cout << "Error: Unable to open the file." << endl;
        }
    }

    
};


int main() {
    string path = "C:\\Users\\igorb\\OneDrive\\Рабочий стол\\test\\BD.txt";
    WordTranslationQuiz w = WordTranslationQuiz(path, 3);
    w.ReadFile();


    cout << "sdfdsf";
    return 0;
}
