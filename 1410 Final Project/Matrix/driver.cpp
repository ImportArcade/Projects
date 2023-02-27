#include <iostream>
#include <iomanip>
using namespace std;

class Matrix
{
private:
	int nrows = 0;
	int ncols = 0;
	double** array = nullptr;
public:
	Matrix(int r, int c);
	Matrix mult(const Matrix m) const;
	Matrix add(const Matrix m) const;
	void read();
	void print(int width = 6);
};
Matrix::Matrix(int r, int c)
{
	this->nrows = r;
	this->ncols = c;
	array = new double* [nrows];
	for (int i = 0; i < nrows; i++)
		array[i] = new double[ncols];
}

Matrix Matrix::mult(const Matrix m) const
{

	if (this->ncols != m.nrows)
	{
		throw "nrows != columuns error";
		exit(0);
	}

	Matrix C = Matrix(this->nrows, m.ncols);
	for (int i = 0; i < this->nrows; i++) {
		for (int j = 0; j < m.ncols; j++) {
			C.array[i][j] = 0;
			for (int k = 0; k < m.nrows; k++) {
				C.array[i][j] += this->array[i][k] * m.array[k][j];
			}
		}
	}
	return C;
}

Matrix Matrix::add(const Matrix m) const {

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

int main()
{
	Matrix a(2, 3);
	cout << "Input Matrix a: " << endl;
	a.read();
	cout << "Matrix a =" << endl;
	a.print();
	cout << endl;
	Matrix b(3, 2);
	cout << "Input Matrix b; " << endl;
	b.read();
	cout << "Matrix b =" << endl;
	b.print();
	cout << endl;
	cout << endl << endl << "a * b =" << endl;
	Matrix ab = a.mult(b);
	ab.print();
	cout << endl << endl << "b * a =" << endl;
	Matrix ba = b.mult(a);
	ba.print();
	return 0;
}