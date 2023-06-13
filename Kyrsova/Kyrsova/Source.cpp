#include <iostream>
#include <fstream>
#include <string>
#include <random>

using namespace std;

struct Word {
    string word;
    string translation;
};

struct Node {
    Word data;
    Node* prev = nullptr;
    Node* next = nullptr;
};

int TrueWriting(const Node& data)
{
    int counter = 0;
    string answer;

    cout << data.data.word << endl;
    cout << "Write a translation: ";
    cin >> answer;

    if (answer == data.data.translation)
    {
        return counter+1;
    }
    else {
        return counter;
    }

}

int ABCWriting(Node* head)
{
    int counter = 0;

    // Count the number of words in the linked list
    int wordCount = 0;
    Node* current = head;
    while (current != nullptr) {
        wordCount++;
        current = current->next;
    }

    // Generate random indices for selecting words
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distr(0, wordCount - 1);
    int indices[3];

    // Generate distinct indices
    indices[0] = distr(gen);
    indices[1] = distr(gen);
    while (indices[1] == indices[0]) {
        indices[1] = distr(gen);
    }
    indices[2] = distr(gen);
    while (indices[2] == indices[0] || indices[2] == indices[1]) {
        indices[2] = distr(gen);
    }

    // Determine the index for the correct answer (a, b, or c)
    uniform_int_distribution<int> answerDistr(0, 2);
    int correctIndex = answerDistr(gen);

    // Traverse the linked list to find the correct index and word
    current = head;
    int currentIndex = 0;
    while (current != nullptr) {
        if (currentIndex == indices[correctIndex]) {
            break;
        }
        currentIndex++;
        current = current->next;
    }

    // Get the correct word for displaying the question
    string correctWord = current->data.translation;

    // Traverse the linked list to the selected indices
    current = head;
    currentIndex = 0;
    while (current != nullptr) {
        if (currentIndex == indices[0] || currentIndex == indices[1] || currentIndex == indices[2]) {
            cout << (currentIndex == indices[0] ? "a) " : (currentIndex == indices[1] ? "b) " : "c) "));
            cout << current->data.word << endl;
        }

        current = current->next;
        currentIndex++;
    }

    // Get user's choice
    string choice;
    cout << "Choose the correct translation to " << correctWord << " (a, b, or c): ";
    cin >> choice;

    // Check if the chosen option is correct
    if (choice == "a" && correctIndex == 0) {
        counter++;
    }
    else if (choice == "b" && correctIndex == 1) {
        counter++;
    }
    else if (choice == "c" && correctIndex == 2) {
        counter++;
    }

    return counter;
}



void combineFunctions(Node* head)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distr(0, 1);

    int totalScore = 0;
    int totalQuestions = 0;

    Node* current = head;
    while (current != nullptr) {
        int randomFunc = distr(gen);
        cout << endl;
        if (randomFunc == 0) {
            int result = TrueWriting(*current);
            totalScore += result;
            totalQuestions++;
        }
        else {
            int result = ABCWriting(head);
            totalScore += result;
            totalQuestions++;
        }

        current = current->next;

    }

    cout << "Total Score: " << totalScore << "/" << totalQuestions << endl;
}



void readWordsFromFile(Node*& head, Node*& tail, const string& filename) {
    ifstream file(filename, ios::binary);
    if (file.is_open()) {
        string word;
        string translation;

        while (getline(file, word) && getline(file, translation)) {
            Word newWord = { word, translation };

            Node* newNode = new Node;
            newNode->data = newWord;
            newNode->prev = nullptr;
            newNode->next = nullptr;

            if (head == nullptr) {
                head = newNode;
                tail = newNode;
            }
            else {
                tail->next = newNode;
                newNode->prev = tail;
                tail = newNode;
            }
        }

        file.close();
        cout << "Words have been loaded from " << filename << endl;
    }
    else {
        cout << "Error: Unable to open the file." << endl;
    }
}

void displayWords(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        cout << current->data.word << " - " << current->data.translation << endl;
        current = current->next;
    }
}

void freeMemory(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }
}

int main()
{
    system("chcp 1251");
    system("cls");

    string filename;
    cout << "Enter the name of the file: ";
    cin >> filename;

    Node* head = nullptr;
    Node* tail = nullptr;

    readWordsFromFile(head, tail, filename);

    displayWords(head);

    cout << "\t\t\tStart test" << endl;
    combineFunctions(head);

    freeMemory(head);

    return 0;
}



//  D:\\osnov.prog\\Lab10\\Training.txt

//  D:\\osnov.prog\\Lab10\\Lab10.txt

//  D:\\Курсова за 1,5 дня\\Lab10.txt

//   D:\\osnov.prog\\Lab10\\.bin