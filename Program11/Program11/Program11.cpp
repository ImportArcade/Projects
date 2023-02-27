#include <iostream>
#include <vector>
using namespace std;

void isReflexive(vector<vector<bool>> mat, bool* check) {
	for (int i = 0; i < mat.size(); i++) {
		for (int j = 0; j < mat.size(); j++) {
			if (i == j && mat[i][j] == 0) {
				*check = false;
			}
		}
	}
}

void isIrreflexive(vector<vector<bool>> mat, bool* check) {
	for (int i = 0; i < mat.size(); i++) {
		for (int j = 0; j < mat.size(); j++) {
			if (i == j && mat[i][j] == 1) {
				*check = false;
			}
		}
	}
}

void isSymmetric(vector<vector<bool>> mat, bool* check) {
	for (int i = 0; i < mat.size(); i++) {
		for (int j = 0; j < mat.size(); j++) {
			if (mat[i][j] != mat[j][i]) {
				*check = false;
			}
		}
	}
}

void isAntisymmetric(vector<vector<bool>> mat, bool* check) {
	for (int i = 0; i < mat.size(); i++) {
		for (int j = 0; j < mat.size(); j++) {
			if (i != j) {
				if (mat[i][j] == 1 && mat[j][i] == 1) {
					*check = false;
				}
			}
		}
	}
}

void isAsymmetric(vector<vector<bool>> mat, bool* check) {
	for (int i = 0; i < mat.size(); i++) {
		for (int j = 0; j < mat.size(); j++) {
			if (i != j) {
				if (mat[i][j] == 1 && mat[j][i] == 1) {
					*check = false;
				}
			}
		}
	}
}

void printMatrix(vector<vector<bool>> mat) {
	for (int i = 0; i < mat.size(); i++) {
		for (int j = 0; j < mat[i].size(); j++) {
			cout << mat[i][j] << ' ';
		}
		cout << endl;
	}
}

void finalProduct(bool refcheck, bool ircheck, bool symcheck, bool asymcheck, bool anticheck) {
	if (!refcheck && !ircheck && !symcheck && !asymcheck && !anticheck) {
		cout << "None";
	}
	for (int i = 0; i < 5; i++) {
		if (refcheck) {
			cout << "Reflexive, ";
			refcheck = false;
		}
		else if (ircheck) {
			cout << "Irreflexive, ";
			ircheck = false;
		}
		else if (symcheck) {
			cout << "Symmetric, ";
			symcheck = false;
		}
		else if (asymcheck) {
			cout << "Asymmetric, ";
			asymcheck = false;
		}
		else if (anticheck) {
			cout << "Antisymmetric, ";
			anticheck = false;
		}
	}
}

int main() {
	bool isreflexive = true;
	bool isirreflexive = true;
	bool issymmetric = true;
	bool isantisymmetric = true;
	bool isasymmetric = false;
	int i, j = 0;
	vector<vector<bool>> matOne = { {0, 1, 1, 1},{1, 0, 0, 0},{1, 0, 0, 0}, {1, 0, 0, 0} }; //Symmetric and Irreflexive
	vector<vector<bool>> matTwo = { {1, 0, 0, 0},{0, 1, 0, 0},{0, 0, 1, 0}, {0, 0, 0, 1} }; //Reflexive and Antisymmetric
	vector<vector<bool>> matThree = { {1, 0, 0, 1},{0, 0, 1, 1},{1, 0, 1, 0}, {0, 0, 0, 0} }; //None
	vector<vector<bool>> matFour = { {1, 1, 0, 1},{1, 1, 1, 0},{0, 1, 1, 1}, {1, 0, 1, 1} }; //Symmetric and Reflexive


	//Check Matrix One
	printMatrix(matOne);
	isReflexive(matOne, &isreflexive);
	isIrreflexive(matOne, &isirreflexive);
	isSymmetric(matOne, &issymmetric);
	isAntisymmetric(matOne, &isantisymmetric);
	if (isantisymmetric && isirreflexive) {
		isAsymmetric(matOne, &isasymmetric);
	}

	cout << "Matrix 1: ";
	finalProduct(isreflexive, isirreflexive, issymmetric, isasymmetric, isantisymmetric);
	cout << endl;

	isreflexive = true;
	isirreflexive = true;
	issymmetric = true;
	isantisymmetric = true;
	isasymmetric = false;

	//Check Matrix Two
	printMatrix(matTwo);
	isReflexive(matTwo, &isreflexive);
	isIrreflexive(matTwo, &isirreflexive);
	isSymmetric(matTwo, &issymmetric);
	isAntisymmetric(matTwo, &isantisymmetric);
	if (isantisymmetric && isirreflexive) {
		isAsymmetric(matTwo, &isasymmetric);
	}
	

	cout << "Matrix 2: ";
	finalProduct(isreflexive, isirreflexive, issymmetric, isasymmetric, isantisymmetric);
	cout << endl;

	isreflexive = true;
	isirreflexive = true;
	issymmetric = true;
	isantisymmetric = true;
	isasymmetric = false;

	//Check Matrix Three
	printMatrix(matThree);
	isReflexive(matThree, &isreflexive);
	isIrreflexive(matThree, &isirreflexive);
	isSymmetric(matThree, &issymmetric);
	isAntisymmetric(matThree, &isantisymmetric);
	if (isantisymmetric && isirreflexive) {
		isAsymmetric(matThree, &isasymmetric);
	}

	cout << "Matrix 3: ";
	finalProduct(isreflexive, isirreflexive, issymmetric, isasymmetric, isantisymmetric);
	cout << endl;

	isreflexive = true;
	isirreflexive = true;
	issymmetric = true;
	isantisymmetric = true;
	isasymmetric =false;

	//Check Matrix Four
	printMatrix(matFour);
	isReflexive(matFour, &isreflexive);
	isIrreflexive(matFour, &isirreflexive);
	isSymmetric(matFour, &issymmetric);
	isAntisymmetric(matFour, &isantisymmetric);
	if (!isantisymmetric && isirreflexive) {
		isAsymmetric(matFour, &isasymmetric);
	}

	cout << "Matrix 4: ";
	finalProduct(isreflexive, isirreflexive, issymmetric, isasymmetric, isantisymmetric);
	cout << endl;
}