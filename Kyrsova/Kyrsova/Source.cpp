#include <iostream>
#include <fstream>
#include <string>

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

void readWordsFromFile(Node*& head, Node*& tail, const string& filename) {
    ifstream file(filename);
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

    freeMemory(head);

    return 0;
}


//  D:\\osnov.prog\\Lab10\\Training.txt

//  D:\\osnov.prog\\Lab10\\Lab10.txt