#include "Matrix.h"
#include <iomanip>
#include <iostream>
using namespace std;

Matrix::Matrix(int r, int c)
{
	this-> nrows = r;
	this-> ncols = c;
	array = new double* [nrows];
	for (int i = 0; i < nrows; i++)
		array[i] = new double [ncols];
}

Matrix Matrix::mult(const Matrix m) const
{
	
	if (this->ncols != m.nrows)
	{
		throw "nrows != columuns error";
		exit(0);
	}

	Matrix C = Matrix(this->nrows, m.ncols);
	for (int i = 0; i < this->nrows; i++){
		for (int j = 0; j < m.ncols; j++){
			C.array[i][j] = 0;
			for (int k = 0; k < m.nrows; k++){
				C.array[i][j] += this->array[i][k] * m.array[k][j];
			}
		}
	}
	return C;
}

void Matrix::read()
{
	for (int i = 0; i < this->nrows; i++)
		for (int j = 0; j < this->ncols; j++)
			cin >> array[i][j];

}
void Matrix::print(int width)
{
	for (int i = 0; i < nrows; i++)
	{
		for (int j = 0; j < ncols; j++)
			cout << setw(width) << array[i][j];
		cout << endl;
	}
}