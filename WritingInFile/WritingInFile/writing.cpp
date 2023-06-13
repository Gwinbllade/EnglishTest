#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class Vocabluary
{
private:
	string word;
	string translation;

public:

	string Words()
	{
		return word;
	}

	string Translation()
	{
		return translation;
	}

	void FileName(string filename)
	{
		cout << "Enter the name of the file: ";
		cin >> filename;
	}


	string EditNameFile(const string& filename)
	{
		return "D:\\Курсова за 1,5 дня\\"+ filename + ".bin";
	}

	void WriteWordsInFile(const string& filename)
	{
		ofstream vocabuary;
		vocabuary.open(EditNameFile(filename), ios::binary);

		if (!vocabuary.is_open()){
			cout << "File not open!" << endl;
		}

		int error = 0;
		
		while (error != 1)
		{
			cout << "Write a word: ";
			cin >> word;
			if (word == "1") {
				error = 1;
				break;
			}
			cout << endl;
			vocabuary << word << endl;

			cout << "Write a translation: ";
			cin >> translation;
			cout << endl;
			vocabuary << translation << endl;
		}
		cout << "File created" << endl;
	}
};


int main()
{
	Vocabluary object;
	string filename;

	object.FileName(filename);
	object.WriteWordsInFile(filename);

	return 0;
}